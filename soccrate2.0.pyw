import threading
import tkinter as tk
import pystray
from PIL import Image
from Presentacion import Presentacion
import psutil
import schedule
import time
from time import sleep
from BLL import BLL_Request
from BLL import BLL_Fecha
from BLL import BLL_Cliente
from BLL import BLL_Informe
from BLL import BLL_Log
from BLL import BLL_Archivo
from DAL import DAL_Conexion
import os

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
    # crea una ventana de error
    error_window = tk.Tk()
    error_window.title("Error")
    error_label = tk.Label(error_window, text="Ya hay una instancia de la aplicación en ejecución")
    error_label.pack()
    error_window.mainloop()

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
        
        except Exception as e:
            BLL_Log.Log().escribir("Hubo algun problema en la creacion de informe " + str(e), cliente.nombre, "Error")



def doRequest(listaCliente):   
    fecha = BLL_Fecha.Fecha()
    semanal = False
    mensual = False
    request = BLL_Request.Request()
    print("entre a request")
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
        except Exception as e:
            BLL_Log.Log().escribir("Hubo algun problema en las request " + str(e), cliente.nombre, "Error")



def doRequestInforme():
    cliente = BLL_Cliente.Cliente()
    listaCliente = cliente.crearListaDB()

    doRequest(listaCliente)

    doInforme(listaCliente)

### -----------------------------------------------------------------------------------##################


def create_menu():
    # crea el menu del icono
    menu = pystray.Menu(pystray.MenuItem("Abrir", show, default=True), pystray.MenuItem("Cerrar", stop))
    return menu

def create_icon():
# crea el icono y lo devuelve
    image = Image.open("Presentacion//img//icono.png")
    menu = create_menu()
    icon = pystray.Icon("SOCcrate", image, "SOCcrate", menu)
    return icon

def cleanup():
    # elimina los recursos utilizados por la aplicación
    icon.stop()

def stop():
    # detiene el subproceso del icono y cierra la aplicacion
    cleanup()
    confirm = tk.messagebox.askyesno("Confirmar", "¿Estás seguro que quieres cerrar la aplicación?")
    if confirm:
        root.quit()

def show():
    # muestra la ventana principal
    root.deiconify()

def minimize_to_tray():
    # minimize to tray instead of closing
    root.withdraw()

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():

    log = BLL_Log.Log()
    fecha = BLL_Fecha.Fecha()
    print("entre a main")
    conexion = DAL_Conexion.Conexion().asignarAtributos("*/*")
    if is_already_running():
        print("hay una instancia en ejecucion")
        show_error()
    else:
        # crea la ventana principal
        global root
        root = Presentacion.App()
        root.protocol("WM_DELETE_WINDOW", minimize_to_tray)
        
    
        # crea el icono
        global icon
        icon = create_icon()
        
    
        # corre el subproceso del icono en segundo plano
        threading.Thread(target=run_icon).start()
        schedule_thread = threading.Thread(target=run_schedule, daemon=True)
        schedule_thread.start()
    
        #schedule.every().day.at("18:00").do(doRequest)
        with open(os.getcwd() + '//DATA//CONFIG//scheduleconf.txt', 'r') as f:

            scheduleconf = f.read().strip().replace('"', '')

        log.escribir("Horario de ejecución leído desde el archivo scheduleconf.txt: {}".format(scheduleconf), "main", "Info")
        schedule.every().day.at(str(scheduleconf)).do(doRequestInforme)
        root.mainloop()
    

def run_icon():
    # corre el subproceso del icono
    icon.run()

if __name__ == "__main__":
    main()
