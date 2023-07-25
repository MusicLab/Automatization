from .ui_interface import  *
from PySide2 import QtGui, QtWidgets

from io import StringIO
import os
import sys 
from DAL import DAL_Conexion
from DAL import DAL_Mapper
from DAL import DAL_Mapper_Archivo

class ConexionConfig(QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        # Conectar la señal currentChanged del QStackedWidget a la función actualizar_conexion
        self.ui.stackedWidget.currentChanged.connect(self.actualizar_conexion)

        self.ui.progressBar_2.setVisible(False)

    def actualizar_conexion(self, index):
        # Buscar el objeto QWidget dentro del QStackedWidget
        widget = self.ui.stackedWidget.widget(index)
        self.ui.progressBar_2.setVisible(False)

        # Buscar el objeto QLabel que muestra los logs de la consola dentro del QWidget
        label = widget.findChild(QtWidgets.QLabel, "Label_Console_conx")

        # Verificar si se encontró el objeto
        if label is not None:
            # Limpiar el texto del QLabel
            label.clear()

    def test_clicked(self):
        conexiondal = DAL_Conexion.Conexion()
        mapperdal = DAL_Mapper.Mapper()

        dataip = self.ui.ip_entry.text()
        datauser = self.ui.user_entry.text()
        datapassw  = self.ui.pass_entry.text()
        datadb = self.ui.namedb_entry.text()
        datapuerto = self.ui.port_entry.text()


        # Realizar la conexión
      
        # Redirigir stdout a un StringIO en memoria
        stdout_buffer = StringIO()
        sys.stdout = stdout_buffer

        try:
            conexiondal.asignarAtributos(datadb, datauser, datapassw, dataip, datapuerto)
            mapperdal.asignarConexion(conexiondal)
            mapperdal.mapperConectarDB()

            print("Nombre db:{}".format(datadb))
            print("Usuario:{}".format(datauser))
            print("Password:{}".format(datapassw))
            print("IP:{}".format(dataip))
            print("Puerto:{}".format(datapuerto))

            #self.clear_fields()

            self.ui.Label_Console_conx.setText(stdout_buffer.getvalue())
        except Exception as e:
            print("Error al conectar a la base de datos:", e)

        finally:
            mapperdal.mapperDesconectarDB()

        # Restaurar stdout y stderr
        sys.stdout = sys.__stdout__
        
    def borrar_clicked(self):
        conexiondal = DAL_Conexion.Conexion()
        mapperarchivo = DAL_Mapper_Archivo.Mapper_Archivo()

        # Redirigir stdout a un StringIO en memoria
        stdout_buffer = StringIO()
        sys.stdout = stdout_buffer

        mapperarchivo.mapperExisteArchivo(os.getcwd() + "//soccrate2//DATA//CONFIG//Conexion.json")
        conexiondal.cambiarEstadoArchivo()
            
        self.ui.Label_Console_conx.setText(stdout_buffer.getvalue())

        # Restaurar stdout y stderr
        sys.stdout = sys.__stdout__

    def asignar_clicked(self):
        conexiondal = DAL_Conexion.Conexion()
        mapperdal = DAL_Mapper.Mapper()
        mapperarchivo = DAL_Mapper_Archivo.Mapper_Archivo()

        dataip = self.ui.ip_entry.text()
        datauser = self.ui.user_entry.text()
        datapassw = self.ui.pass_entry.text()
        datadb = self.ui.namedb_entry.text()
        datapuerto = self.ui.port_entry.text()

        # Redirigir stdout a un StringIO en memoria
        stdout_buffer = StringIO()
        sys.stdout = stdout_buffer

        mapperarchivo.mapperCrearArchivoConexion(datadb, datauser, datapassw, dataip, datapuerto)
        conexiondal.asignarAtributos(datadb, datauser, datapassw, dataip, datapuerto)
        mapperdal.asignarConexion(conexiondal)
        mapperdal.mapperEncriptar()

        self.clear_fields()

        self.ui.Label_Console_conx.setText(stdout_buffer.getvalue())

        # Restaurar stdout y stderr
        sys.stdout = sys.__stdout__
            
    def validar_ip(self, text):
        # Verificar si el texto está vacío
        if not text:
            self.ui.ip_entry.setStyleSheet("")  # Restaurar el color de fondo del QLineEdit
            return

        # Validar que la dirección IP solo contenga números y puntos
        for char in text:
            if not char.isdigit() and char != '.':
                self.ui.ip_entry.setStyleSheet("background-color: #FFB6C1;")  # Cambiar el color de fondo del QLineEdit a rojo
                return

        # Validar que la dirección IP tenga el formato correcto
        parts = text.split('.')
        if len(parts) != 4:
            self.ui.ip_entry.setStyleSheet("background-color: #FFB6C1;")  # Cambiar el color de fondo del QLineEdit a rojo
            return
        for part in parts:
            if not part.isdigit() or int(part) > 255:
                self.ui.ip_entry.setStyleSheet("background-color: #FFB6C1;")  # Cambiar el color de fondo del QLineEdit a rojo
                return

        # La dirección IP es válida
        self.ui.ip_entry.setStyleSheet("")  # Restaurar el color de fondo del QLineEdit
        
    def validar_puerto(self, text):
        # Verificar si el texto está vacío
        if not text:
            self.ui.port_entry.setStyleSheet("")  # Restaurar el color de fondo del QLineEdit
            return
        
        # Validar que el valor solo contenga números
        if not text.isdigit():
            self.ui.port_entry.setStyleSheet("background-color: #FFB6C1;")  # Cambiar el color de fondo del QLineEdit a rojo
            return QtGui.QValidator.Intermediate, text

        # Validar que el valor esté en el rango permitido (0-65535)
        if int(text) < 0 or int(text) > 65535:
            self.ui.port_entry.setStyleSheet("background-color: #FFB6C1;")  # Cambiar el color de fondo del QLineEdit a rojo
            return QtGui.QValidator.Intermediate, text

        # El valor es válido
        self.ui.port_entry.setStyleSheet("")  # Restaurar el color de fondo del QLineEdit
        return QtGui.QValidator.Acceptable, text
    
    def clear_fields(self):
        # Borrar los datos de los campos
        self.ui.ip_entry.setText("")
        self.ui.user_entry.setText("")
        self.ui.pass_entry.setText("")
        self.ui.namedb_entry.setText("")
        self.ui.port_entry.setText("")

'''
    def test_clicked(self):
        conexiondal = DAL_Conexion.Conexion()
        mapperdal = DAL_Mapper.Mapper()

        dataip = self.ui.ip_entry.text()
        datauser = self.ui.user_entry.text()
        datapassw  = self.ui.pass_entry.text()
        datadb = self.ui.namedb_entry.text()
        datapuerto = self.ui.port_entry.text()

        self.ui.progressBar_2.setVisible(True)

        # Configurar la barra de progreso
        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar_2.setMaximum(100)

        # Realizar la conexión
        try:
        # Realizar la conexión
            for i in range(101):
                # Redirigir stdout a un StringIO en memoria
                stdout_buffer = StringIO()
                sys.stdout = stdout_buffer

                conexiondal.asignarAtributos(datadb, datauser, datapassw, dataip, datapuerto)
                mapperdal.asignarConexion(conexiondal)
                mapperdal.mapperConectarDB()
                #mapperdal.mapperDesconectarDB()

                # Actualizar la barra de progreso
                progress = i / 100 * 100
                self.ui.progressBar_2.setValue(progress)

                print("Nombre db:{}".format(datadb))
                print("Usuario:{}".format(datauser))
                print("Password:{}".format(datapassw))
                print("IP:{}".format(dataip))
                print("Puerto:{}".format(datapuerto))

                self.clear_fields()

                self.ui.Label_Console_conx.setText(stdout_buffer.getvalue())

                # Restaurar stdout y stderr
                sys.stdout = sys.__stdout__

        except Exception as e:
            # Manejar la excepción o error ocurrido durante la conexión
            self.ui.Label_Console_conx.setText(str(e))
'''