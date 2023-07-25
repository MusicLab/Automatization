from PySide2 import QtWidgets, QtGui, QtCore
from PIL import Image
import sys
import os
from Presentacion import Presentacion_Main
from Presentacion.ui_interface import *
import psutil
import threading
import schedule
import time
from pystray import MenuItem, Icon, Menu
from pystray import MenuItem as item
from BLL import BLL_Request
from BLL import BLL_Fecha
from BLL import BLL_Cliente
from BLL import BLL_Informe
from BLL import BLL_Log
from BLL import BLL_Archivo
from DAL import DAL_Conexion
from tqdm import tqdm


app = QtWidgets.QApplication(sys.argv)

def is_already_running():
    current_process = psutil.Process()
    for process in psutil.process_iter():
        try:
            if process.name() == current_process.name() and process.pid != current_process.pid:
                # Hay otro proceso con el mismo nombre en ejecución
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def show_error():
    # Crea una ventana de error
    error_window = QtWidgets.QMessageBox()
    error_window.setWindowTitle("Error")
    error_window.setText("Ya hay una instancia de la aplicación en ejecución.")
    error_window.exec_()

#### -------------------------------------------------core--------------------------------###########

def hacer_informe(cliente, fecha_inicio, fecha_fin, tipo):
    try:
        informe = BLL_Informe.Informe(fecha_inicio, fecha_fin, cliente, tipo)
        informe.hacerInforme()
        BLL_Log.Log().escribir("Se realizo el informe con exito " , cliente.nombre, "Informar")
    except Exception as e:
        BLL_Log.Log().escribir("Hubo un problema para hacer el informe, probablemente no hay archivos CSV del cliente, error : " + str(e), cliente.nombre, "Error")


def doInforme(listaCliente):
    fecha = BLL_Fecha.Fecha()
    fechaFin = BLL_Fecha.Fecha().fechaFin()
    print(fecha.fechaInicio("diario"), fechaFin)

    
    with tqdm(total=len(listaCliente), desc="Procesando clientes") as pbar_clientes:
        for cliente in listaCliente:
            try:
                # informes mensuales
                if fecha.ahora().day == 1:
                    hacer_informe(cliente, fecha.fechaInicio("mensual"), fechaFin, "mensual")

                # informes semanales (el tipo de informe es mensual ya que todavia no se definio un template diferente para el informe semanal, por lo tanto se usa el mensual)
                if fecha.ahora().weekday() == 4 and cliente.periodicidad == "1":
                    hacer_informe(cliente, fecha.fechaInicio("semanal"), fechaFin, "semanal")

                # informes diarios
                if cliente.periodicidad == "0":
                    hacer_informe(cliente, fecha.fechaInicio("diario"), fechaFin, "diario")

                BLL_Log.Log().escribir("Se generó el informe correctamente", cliente.nombre, "Informar")
            except Exception as e:
                BLL_Log.Log().escribir("Hubo algun problema en la creacion de informe " + str(e), cliente.nombre, "Error")

            # Actualizar la barra de progreso para el procesamiento de los clientes
            pbar_clientes.update(1)


def doRequest(listaCliente):   
    fecha = BLL_Fecha.Fecha()
    semanal = False
    mensual = False
    request = BLL_Request.Request()
    print("entre a request")
    with tqdm(total=len(listaCliente)) as pbar:
        for cliente in listaCliente:
            print(cliente)
            
            try:
                if fecha.ahora().day == 1:
                    #lunes = 0, domingo = 6
                    if fecha.ahora().weekday() == 4:
                        #SE HACEN TODAS LAS REQUESTS
                        semanal = True
                        mensual = True
                        print("Hoy es mensual y semanal")
                    else: 
                        #SE HACEN LAS REQUESTS DIARIAS Y MENSUALES
                        mensual = True
                        print("Hoy es mensual")
                elif fecha.ahora().weekday() == 4:
                    #SE HACEN LAS REQUESTS DIARIAS Y SEMANALES
                    semanal = True
                    print("Hoy es semanal")
                print("Hoy es diario")
                # se hacen las request correspondientes
                request.ejecutarMapperLectura(fecha, semanal, mensual, cliente)
                BLL_Log.Log().escribir("Se realizaron las request de manera correcta ", cliente.nombre, "Informar")
                pbar.update(1)
            except Exception as e:
                BLL_Log.Log().escribir("Hubo algun problema en las request " + str(e), cliente.nombre, "Error")



def doRequestInforme():
    cliente = BLL_Cliente.Cliente()
    listaCliente = cliente.crearListaDB()

    # Crear un hilo para ejecutar la función doRequest
    request_thread = threading.Thread(target=doRequest, args=(listaCliente,))
    request_thread.start()

    # Crear un hilo para ejecutar la función doInforme
    informe_thread = threading.Thread(target=doInforme, args=(listaCliente,))
    informe_thread.start()

    # Esperar a que ambos hilos finalicen
    request_thread.join()
    informe_thread.join()

### -----------------------------------------------------------------------------------##################

def cleanup():
    # elimina los recursos utilizados por la aplicación
    icon.stop()
    root.deleteLater()
    app.quit()

def on_open(icon, item):
    root.show()
    root.activateWindow()

def on_exit(icon, item):
    cleanup()

def read_scheduleconf():
    with open(os.getcwd() + '//DATA//CONFIG//scheduleconf.txt', 'r') as f:
        scheduleconf = f.read().strip()
    return scheduleconf

def run_schedule():
    scheduleconf = read_scheduleconf()
    while True:
        current_scheduleconf = read_scheduleconf()
        if current_scheduleconf != scheduleconf:
            # El horario ha sido modificado, actualiza el schedule
            scheduleconf = current_scheduleconf
            schedule.clear()
            schedule.every().day.at(scheduleconf).do(doRequestInforme)
            print("Schedule programado para ejecutarse a las", scheduleconf)

        schedule.run_pending()
        time.sleep(1)

def monitor_scheduleconf():
    file_path = os.getcwd() + '//DATA//CONFIG//scheduleconf.txt'
    last_modified = os.path.getmtime(file_path)

    while True:
        time.sleep(1)
        if os.path.getmtime(file_path) > last_modified:
            # El archivo ha sido modificado, reinicia el proceso del schedule
            last_modified = os.path.getmtime(file_path)
            schedule_thread = threading.Thread(target=run_schedule, daemon=True)
            schedule_thread.start()
'''
def run_schedule():
    with open(os.getcwd() + '//DATA//CONFIG//scheduleconf.txt', 'r') as f:
        scheduleconf = f.read().strip()
        
    schedule.every().day.at(scheduleconf).do(doRequestInforme)

    print("Schedule programado para ejecutarse a las", scheduleconf)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
'''

def main():
    log = BLL_Log.Log()
    print("entre a main")
    #conexion = DAL_Conexion.Conexion().asignarAtributos(**)
    conexion = DAL_Conexion.Conexion()
    if(os.path.exists(os.getcwd() + "//DATA//CONFIG//Conexion.json")):
        conexion.leerArchivo()
    if is_already_running():
        print("hay una instancia en ejecucion")
        show_error()
    else:
        # Crea un subproceso para ejecutar el schedule en segundo plano
        schedule_thread = threading.Thread(target=run_schedule, daemon=True)
        schedule_thread.start()

        monitor_thread = threading.Thread(target=monitor_scheduleconf, daemon=True)
        monitor_thread.start()

        # crea la ventana principal
        global root
        root = Presentacion_Main.App()
        root.show()

        # Agrega el ícono y el menú de Pystray
        image = Image.open(os.getcwd() + "//Presentacion//img//icono.png")  
        menu = (
            item('Abrir', on_open, default=True),
            item('Cerrar', on_exit),
        )

        global icon    
        icon = Icon("Soccrate", image, "Soccrate 2.0", menu)
        icon.run()

        cleanup()
        #sys.exit(app.exec_())

if __name__ == "__main__":
    main()