from .ui_interface import  *
from PySide2 import QtGui, QtWidgets, QtCore
import os
from DAL import DAL_Mapper
from BLL import BLL_Grafico_Personalizado
from BLL import BLL_Cliente

class GraficosPersonalizados(QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        self.grafico_creado = False

        #Fecha actual en el calendario.
        current_date = QDate.currentDate()
        self.ui.fecha_fin.setDate(current_date)

        previous_date = current_date.addDays(-1)  # Restar un día a la fecha actual
        self.ui.fecha_inicio.setDate(previous_date)

        #Diccionarios
        self.dict_graficos = {
            ("Devices", "Gráfico de barras"): "Barras", ("Devices", "Gráfico de torta"): "Torta",
            ("Exploits", "Gráfico de barras"): "Barras",("Exploits", "Gráfico de torta"): "Torta",
            ("Threats", "Gráfico de barras"): "Barras", ("Threats", "Gráfico de torta"): "Torta", ("Threats", "Histograma"): "Histograma"
        }
        self.dict_columns = {
            ("Devices", "Tenant id"): "tid", ("Devices", "Device name"): "devicename", ("Devices", "Operative System"): "operativesystem", ("Devices", "Agent Version"): "agentversion", ("Devices", "Policy"): "policy", ("Devices", "IPs"): "ips", ("Devices", "Date off line"): "dateoffline", ("Devices", "Zone Name"): "zonename", ("Devices", "Last logged in user"): "lastloggedinuser", ("Devices", "Date"): "date",
            ("Exploits", "Tenant id"): "tid", ("Exploits", "Filename"): "filename", ("Exploits", "Device name"): "devicename", ("Exploits", "Username"): "username", ("Exploits", "Violation type"): "violationtype", ("Exploits", "Action"): "action", ("Exploits", "Filepath"): "filepath", ("Exploits", "Created"): "created", ("Exploits", "Process ID"): "processid",
            ("Threats", "Tenant id"): "tid", ("Threats", "SHA256"): "sha256", ("Threats", "File status"): "filestatus", ("Threats", "Device name"): "devicename", ("Threats", "File path"): "filepath", ("Threats", "File name"): "filename", ("Threats", "Classification"): "classification", ("Threats", "Sub class"): "subclass", ("Threats", "File owner"): "fileowner", ("Threats", "Drive type"): "drivetype", ("Threats", "Date found"): "datefound", ("Threats", "Origen de dato"): "origindedato" 
        }

    def actualizar_graficos(self, tipo_seleccionado):
        if tipo_seleccionado == "Devices":
            self.ui.graficos_tipog_combo.clear()
            self.ui.graficos_tipog_combo.addItems(["Gráfico de barras", "Gráfico de torta"])
            self.ui.graficos_colum_combo.clear()
            self.ui.graficos_colum_combo.addItems(["Tenant id", "Device name", "Operative System", "Agent Version", "Policy", "IPs", "Date off line", "Zone Name", "Last logged in user", "Date"])
        elif tipo_seleccionado == "Exploits":
            self.ui.graficos_tipog_combo.clear()
            self.ui.graficos_tipog_combo.addItems(["Gráfico de barras", "Gráfico de torta"])
            self.ui.graficos_colum_combo.clear()
            self.ui.graficos_colum_combo.addItems(["Tenant id", "Filename", "Device name", "Username", "Violation type", "Action", "Filepath", "Created", "Process ID"])
        elif tipo_seleccionado == "Threats":
            self.ui.graficos_tipog_combo.clear()
            self.ui.graficos_tipog_combo.addItems(["Gráfico de barras", "Gráfico de torta", "Histograma"])
            self.ui.graficos_colum_combo.clear()
            self.ui.graficos_colum_combo.addItems(["Tenant id", "SHA256", "File status", "Device name", "Filepath", "Filename", "Classification", "Sub class", "File owner", "Drive type", "Date found", "Origen de dato"])
                
    def eliminar_vacio(self):
        if self.ui.graficos_tipod_combo.itemText(0) == "":
            self.ui.graficos_tipod_combo.removeItem(0)  

    def cargar_clientes_combo(self):
        cliente = BLL_Cliente.Cliente()
        listaClientes = cliente.leerClientesDB()
        data = cliente.convertirListaClientesADict(listaClientes) #trae la data de los clientes
        data = sorted(data, key=lambda x: x['nombre'])  
        # Vaciar el QComboBox graficos_cliente_combo antes de agregar los clientes
        self.ui.graficos_cliente_combo.clear()  
        # Agregar los nombres de los clientes al QComboBox graficos_cliente_combo
        for cliente in data:
            self.ui.graficos_cliente_combo.addItem(cliente['nombre'])   

    def crear_grafico(self):
        #Verifica si hay un gráfico previamente creado, en caso de que sea asi, lo elimina
        tipo_dato = self.ui.graficos_tipod_combo.currentText()
        tipo_grafico = self.ui.graficos_tipog_combo.currentText()
        columna = self.ui.graficos_colum_combo.currentText()
        cliente_data = self.ui.graficos_cliente_combo.currentText()
        fecha_inicio = self.ui.fecha_inicio.date().toString("yyyy-MM-dd")
        fecha_fin = self.ui.fecha_fin.date().toString("yyyy-MM-dd") 
        # Obtener valor simplificado correspondiente a la selección
        valor_graficos = self.dict_graficos.get((tipo_dato, tipo_grafico), tipo_grafico)
        valor_column = self.dict_columns.get((tipo_dato, columna), columna) 
        cliente = BLL_Cliente.Cliente()
        listaClientes = cliente.crearListaDB()
        mapper = DAL_Mapper.Mapper()
        graficosp = BLL_Grafico_Personalizado.Grafico_Personalizado()
        for client in listaClientes:
            if client.nombre == cliente_data:
                clienteSeleccionado = client    
        print(f"tipo_dato: {tipo_dato}, tipo_grafico: {valor_graficos}, columna: {valor_column}, cliente: {clienteSeleccionado}, fecha_inicio: {fecha_inicio}, fecha_fin: {fecha_fin}")
    
        try:
            mapper.mapperConectarDB()
            graficosp.graficoPersonalizado(valor_graficos, tipo_dato, valor_column, clienteSeleccionado, fecha_inicio, fecha_fin)
            imagepath = os.getcwd() + "//DATA//GRAFICOS//Grafico Personalizado.png"
            pixmap = QtGui.QPixmap(imagepath).scaled(self.ui.label_grafico.size(), QtCore.Qt.KeepAspectRatio)
            self.ui.label_grafico.setPixmap(pixmap) 
            # Mostrar mensaje de confirmación
            QtWidgets.QMessageBox.information(self, "Éxito", "El gráfico se creó correctamente.")
        except:
            # Mostrar mensaje de error
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo crear el gráfico.")   

    def borrar_grafico(self):
        self.ui.graficos_tipod_combo.clear()
        self.ui.graficos_tipog_combo.clear()
        self.ui.graficos_colum_combo.clear()
        self.ui.graficos_cliente_combo.clear()  
        for widget in self.ui.FrameDer.children():
            widget.deleteLater()    
        if os.path.exists(os.getcwd() + "//DATA//GRAFICOS//Grafico Personalizado.png"):
            os.remove(os.getcwd() + "//DATA//GRAFICOS//Grafico Personalizado.png")
            # Mostrar mensaje de confirmación
            QtWidgets.QMessageBox.information(self, "Gráfico eliminado", "El gráfico ha sido eliminado correctamente.")
        else:
            # Mostrar mensaje de error
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo encontrar la imagen del gráfico. Por favor, verifique la ruta y vuelva a intentarlo.")    
   
    def exportar_grafico(self):
        archivo, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Exportar gráfico", "", "Archivo PNG (*.png)") 
        if archivo:
            graf = QtGui.QPixmap(os.getcwd() + "//DATA//GRAFICOS//Grafico Personalizado.png")
            graf.save(archivo)
            QtWidgets.QMessageBox.information(self, "Exportar gráfico", "El gráfico se exportó correctamente")  
            self.ui.graficos_tipod_combo.clear()
            self.ui.graficos_tipog_combo.clear()
            self.ui.graficos_colum_combo.clear()
            self.ui.graficos_cliente_combo.clear()  
            for widget in self.ui.FrameDer.children():
                widget.deleteLater()
        else:
            QtWidgets.QMessageBox.critical(self, "Exportar gráfico", "No se seleccionó ningún archivo para guardar")    