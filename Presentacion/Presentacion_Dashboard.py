from .ui_interface import  *
from PySide2 import QtGui, QtWidgets, QtCore
import os
import datetime
from DAL import DAL_Mapper
from BLL import BLL_Grafico_Personalizado
from BLL import BLL_Cliente
from BLL import BLL_Dash
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QApplication, QGraphicsView, QGraphicsScene 
from PySide2.QtGui import QPixmap
from DAL import DAL_Mapper_Eventos

class Dashboard_Page(QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        dashboard = BLL_Dash.Dash()

        #Fecha actual en el calendario.
        current_date = QDate.currentDate()
        self.ui.ff_dash_histo.setDate(current_date)
        self.ui.ff_dash_bar1.setDate(current_date) 
        self.ui.ff_dash_bar2.setDate(current_date) 
        self.ui.ff_dash_torta.setDate(current_date)  

        previous_date = current_date.addDays(-1)  # Restar un día a la fecha actual
        self.ui.fi_dash_histo.setDate(previous_date)
        self.ui.fi_dash_bar1.setDate(previous_date)
        self.ui.fi_dash_bar2.setDate(previous_date)
        self.ui.fi_dash_torta.setDate(previous_date)

        #Diccionarios
        self.tipoDato_dict = {"Devices": "devices", "Exploits": "exploits", "Threats": "threats"}
        self.columnas_dict = {"tid": "Tenant ID", "devicename": "Device Name","operativesystem": "Operative System", "agentversion": "Agent Version", "policy": "Policy", "ips": "IPs", "dateoffline": "Date Offline", "zonename": "Zone Name", "lastloggedinuser": "Last Logged In User", "date": "Date",
                              "filename":"File Name", "username": "User Name", "violationtype" : "Violation Type", "action": "Action", "filepath":"File Path", "created" : "Created", "processid" : "Process ID",
                              "sha256": "SHA 256", "filestatus" : "File Status", "classification" : "Classification", "subclass" : "Sub Class", "fileowner" : "File Owner", "drivetype" : "Drive Type", "datefound" : "Date Found", "origendedato" : "Origen de Dato"}
        self.columnas_inverso_dict = {v: k for k, v in self.columnas_dict.items()}

        if self.ui.barras1_tdato_combo.count() == 0:
            self.ui.barras1_tdato_combo.addItems(["", "Devices", "Exploits", "Threats"])
            self.ui.barras1_tdato_combo.setCurrentIndex(0)
        
        if self.ui.barras2_tdato_combo.count() == 0:
            self.ui.barras2_tdato_combo.addItems(["", "Devices", "Exploits", "Threats"])
            self.ui.barras2_tdato_combo.setCurrentIndex(0)
        
        if self.ui.torta_tdato_combo.count() == 0:
            self.ui.torta_tdato_combo.addItems(["", "Devices", "Exploits", "Threats"])
            self.ui.torta_tdato_combo.setCurrentIndex(0)

    def eliminar_vacio_barras1(self):
        if self.ui.barras1_tdato_combo.itemText(0) == "":
            self.ui.barras1_tdato_combo.removeItem(0)

    def eliminar_vacio_barras2(self):
        if self.ui.barras2_tdato_combo.itemText(0) == "":
            self.ui.barras2_tdato_combo.removeItem(0)

    def eliminar_vacio_torta(self):
        if self.ui.torta_tdato_combo.itemText(0) == "":
            self.ui.torta_tdato_combo.removeItem(0)

    def clintes_dashboard(self):
        cliente = BLL_Cliente.Cliente()
        listaClientes = cliente.leerClientesDB()
        data = cliente.convertirListaClientesADict(listaClientes) #trae la data de los clientes
        data = sorted(data, key=lambda x: x['nombre'])

        # Agregar la opción "Seleccionar Todos" al principio de cada QComboBox
        self.ui.histo_client_combo.addItem("Seleccionar Todos")
        self.ui.barras1_client_combo.addItem("Seleccionar Todos")
        self.ui.barras2_client_combo.addItem("Seleccionar Todos")
        self.ui.torta_client_combo.addItem("Seleccionar Todos")

        # Agregar los nombres de los clientes al QComboBox correspondiente
        for cliente in data:
            self.ui.histo_client_combo.addItem(cliente['nombre'])
            self.ui.barras1_client_combo.addItem(cliente['nombre'])
            self.ui.barras2_client_combo.addItem(cliente['nombre'])
            self.ui.torta_client_combo.addItem(cliente['nombre'])

        # Conectar el evento "currentIndexChanged" a la función "seleccionar_todos"
        self.ui.histo_client_combo.currentIndexChanged.connect(self.seleccionar_todos)
        self.ui.barras1_client_combo.currentIndexChanged.connect(self.seleccionar_todos)
        self.ui.barras2_client_combo.currentIndexChanged.connect(self.seleccionar_todos)
        self.ui.torta_client_combo.currentIndexChanged.connect(self.seleccionar_todos)

    def seleccionar_todos(self):
        combo_box = self.sender()  # Obtener el QComboBox que emitió la señal

        if combo_box.currentIndex() == 0:  # Si se seleccionó el item "Seleccionar Todos"
            clientes_seleccionados = [combo_box.itemText(i) for i in range(1, combo_box.count())]
            print("Todos los clientes han sido seleccionados:", clientes_seleccionados)
        else:  # Si se seleccionó un cliente individual
            cliente_seleccionado = combo_box.currentText()
            print("El cliente seleccionado es:", cliente_seleccionado)
            
#################### ACTUALIZAR COLUMNAS ################### Se hacen por separado para no pisar las señales de los combobox.
    def actualizar_columnas_histo(self):
        dal_eventos = DAL_Mapper_Eventos.Mapper_Eventos()
        tipoDato = self.ui.histo_tdato_combo.currentText()
        tipoDato_value = self.tipoDato_dict.get(tipoDato, tipoDato.lower())
        columna = dal_eventos.obtenerColumnas(tipoDato_value)
        self.ui.histo_column_combo.clear()
        for col in columna:
            col_formateada = self.columnas_dict.get(col, col)
            self.ui.histo_column_combo.addItem(col_formateada)
    
    def actualizar_columnas_barras1(self):
        dal_eventos = DAL_Mapper_Eventos.Mapper_Eventos()    
        tipoDato_barras1 = self.ui.barras1_tdato_combo.currentText()
        tipoDato_barras1_value = self.tipoDato_dict.get(tipoDato_barras1, tipoDato_barras1.lower())
        columna_barras1 = dal_eventos.obtenerColumnas(tipoDato_barras1_value)
        self.ui.barras1_column_combo.clear()
        for col in columna_barras1:
            col_formateada = self.columnas_dict.get(col, col)
            self.ui.barras1_column_combo.addItem(col_formateada)

    def actualizar_columnas_barras2(self):
        dal_eventos = DAL_Mapper_Eventos.Mapper_Eventos()    
        tipoDato_barras2 = self.ui.barras2_tdato_combo.currentText()
        tipoDato_barras2_value = self.tipoDato_dict.get(tipoDato_barras2, tipoDato_barras2.lower())
        columna_barras2 = dal_eventos.obtenerColumnas(tipoDato_barras2_value)
        self.ui.barras2_column_combo.clear()
        for col in columna_barras2:
            col_formateada = self.columnas_dict.get(col, col)
            self.ui.barras2_column_combo.addItem(col_formateada)

    def actualizar_columnas_torta(self):
        dal_eventos = DAL_Mapper_Eventos.Mapper_Eventos()    
        tipoDato_torta = self.ui.torta_tdato_combo.currentText()
        tipoDato_torta_value = self.tipoDato_dict.get(tipoDato_torta, tipoDato_torta.lower())
        columna_torta = dal_eventos.obtenerColumnas(tipoDato_torta_value)
        self.ui.torta_column_combo.clear()
        for col in columna_torta:
            col_formateada = self.columnas_dict.get(col, col)
            self.ui.torta_column_combo.addItem(col_formateada)

#################### MOSTRAR GRAFICOS ###################

    def show_histograma(self):
        dashboard = BLL_Dash.Dash()
        dashHist= dashboard.dashHist("tipoDato", "columna", "cliente", "fechaInicio", "fechaFin", default = True)

        #dashHist = dashHist.scaled(self.ui.Label_Histo.width(), self.ui.Label_Histo.height(), Qt.KeepAspectRatio)
        self.ui.Label_Histo.setPixmap(dashHist)
        self.ui.Label_Histo.show()

    def show_histograma_personalizado(self):
        dashboard = BLL_Dash.Dash()
        # Obtener el texto seleccionado en el ComboBox de clientes
        cliente_data = self.ui.histo_client_combo.currentText()

        # Si el texto es "Seleccionar Todos"
        if cliente_data == "Seleccionar Todos":
            clienteObject = "todos"
        else:
            # Buscar el objeto de cliente correspondiente a partir del nombre seleccionado
            cliente = BLL_Cliente.Cliente()
            listaClientes = cliente.crearListaDB()
            for client in listaClientes:
                if client.nombre == cliente_data:
                    self.cliente_seleccionado = client
                    clienteObject = self.cliente_seleccionado

        tipoDato = self.ui.histo_tdato_combo.currentText()
        columna = self.ui.histo_column_combo.currentText()
        fecha_inicio_histo = self.ui.fi_dash_histo.date().toString("yyyy-MM-dd")
        fecha_fin_histo = self.ui.ff_dash_histo.date().toString("yyyy-MM-dd")

        tipoDato_value = self.tipoDato_dict.get(tipoDato, tipoDato.lower())
        columna_value = self.columnas_inverso_dict.get(columna, columna)

        print(f"cliente: {clienteObject}, tipo de dato: {tipoDato_value}, columnas: {columna_value}, fecha inicio: {fecha_inicio_histo}, fecha fin: {fecha_fin_histo}")
        
        dashboard.dashHist(tipoDato, columna, clienteObject, fecha_inicio_histo, fecha_fin_histo, default = False)


    def show_barras1(self):
        dashboard = BLL_Dash.Dash()
        dashBarras1 = dashboard.dashBarrasExploits("tipoDato", "columna", "cliente", "fechaInicio", "fechaFin", default = True)

        #dashBarras1 = dashBarras1.scaled(self.ui.Label_Barras1.width(), self.ui.Label_Barras1.height(), Qt.KeepAspectRatio)   
        self.ui.Label_Barras1.setPixmap(dashBarras1)
        self.ui.Label_Barras1.show()

    def show_barras1_personalizado(self):
        dashboard = BLL_Dash.Dash()
        # Obtener el texto seleccionado en el ComboBox de clientes
        cliente_data = self.ui.barras1_client_combo.currentText()

        # Si el texto es "Seleccionar Todos"
        if cliente_data == "Seleccionar Todos":
            clienteObject = "todos"
        else:
            # Buscar el objeto de cliente correspondiente a partir del nombre seleccionado
            cliente = BLL_Cliente.Cliente()
            listaClientes = cliente.crearListaDB()
            for client in listaClientes:
                if client.nombre == cliente_data:
                    self.cliente_seleccionado = client
                    clienteObject = self.cliente_seleccionado

        tipoDato = self.ui.barras1_tdato_combo.currentText()
        columna = self.ui.barras1_column_combo.currentText()
        fecha_inicio_histo = self.ui.fi_dash_bar1.date().toString("yyyy-MM-dd")
        fecha_fin_histo = self.ui.ff_dash_bar1.date().toString("yyyy-MM-dd")

        tipoDato_value = self.tipoDato_dict.get(tipoDato, tipoDato.lower())
        columna_value = self.columnas_inverso_dict.get(columna, columna)

        print(f"cliente: {clienteObject}, tipo de dato: {tipoDato_value}, columnas: {columna_value}, fecha inicio: {fecha_inicio_histo}, fecha fin: {fecha_fin_histo}")
        
        #agregar el metodo de bll.dash para barras 1 personalizado

    def show_barras2_personalizado(self):
        dashboard = BLL_Dash.Dash()
        # Obtener el texto seleccionado en el ComboBox de clientes
        cliente_data = self.ui.barras2_client_combo.currentText()

        # Si el texto es "Seleccionar Todos"
        if cliente_data == "Seleccionar Todos":
            clienteObject = "todos"
        else:
            # Buscar el objeto de cliente correspondiente a partir del nombre seleccionado
            cliente = BLL_Cliente.Cliente()
            listaClientes = cliente.crearListaDB()
            for client in listaClientes:
                if client.nombre == cliente_data:
                    self.cliente_seleccionado = client
                    clienteObject = self.cliente_seleccionado

        tipoDato = self.ui.barras2_tdato_combo.currentText()
        columna = self.ui.barras2_column_combo.currentText()
        fecha_inicio_histo = self.ui.fi_dash_bar2.date().toString("yyyy-MM-dd")
        fecha_fin_histo = self.ui.ff_dash_bar2.date().toString("yyyy-MM-dd")

        tipoDato_value = self.tipoDato_dict.get(tipoDato, tipoDato.lower())
        columna_value = self.columnas_inverso_dict.get(columna, columna)

        print(f"cliente: {clienteObject}, tipo de dato: {tipoDato_value}, columnas: {columna_value}, fecha inicio: {fecha_inicio_histo}, fecha fin: {fecha_fin_histo}")
        
        #agregar el metodo de bll.dash para barras 2 personalizado
        
    def show_barras2_personalizado(self):
        dashboard = BLL_Dash.Dash()
        # Obtener el texto seleccionado en el ComboBox de clientes
        cliente_data = self.ui.torta_client_combo.currentText()

        # Si el texto es "Seleccionar Todos"
        if cliente_data == "Seleccionar Todos":
            clienteObject = "todos"
        else:
            # Buscar el objeto de cliente correspondiente a partir del nombre seleccionado
            cliente = BLL_Cliente.Cliente()
            listaClientes = cliente.crearListaDB()
            for client in listaClientes:
                if client.nombre == cliente_data:
                    self.cliente_seleccionado = client
                    clienteObject = self.cliente_seleccionado

        tipoDato = self.ui.torta_tdato_combo.currentText()
        columna = self.ui.torta_column_combo.currentText()
        fecha_inicio_histo = self.ui.fi_dash_torta.date().toString("yyyy-MM-dd")
        fecha_fin_histo = self.ui.ff_dash_torta.date().toString("yyyy-MM-dd")

        tipoDato_value = self.tipoDato_dict.get(tipoDato, tipoDato.lower())
        columna_value = self.columnas_inverso_dict.get(columna, columna)

        print(f"cliente: {clienteObject}, tipo de dato: {tipoDato_value}, columnas: {columna_value}, fecha inicio: {fecha_inicio_histo}, fecha fin: {fecha_fin_histo}")
        
        #agregar el metodo de bll.dash para torta personalizado




    '''    
    def plot_histogram(self):
    # Crear la figura y el lienzo de Matplotlib
        fig = plt.figure()
        canvas = FigureCanvas(fig)

        # Crear el gráfico de histograma
        ax = fig.add_subplot(111)
        ax.hist(self.data, bins='auto')

        # Actualizar el lienzo de Matplotlib
        canvas.draw()

        # Obtener la imagen del lienzo y convertirla a QPixmap
        width, height = fig.get_size_inches() * fig.get_dpi()
        image = np.frombuffer(canvas.tostring_rgb(), dtype='uint8').reshape(int(height), int(width), 3)
        pixmap = QPixmap.fromImage(QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888))

        # Redimensionar la imagen para que quepa dentro del QLabel
        pixmap = pixmap.scaled(self.ui.Label_Histo.width(), self.ui.Label_Histo.height(), Qt.KeepAspectRatio)

        # Mostrar la imagen en el QLabel
        self.ui.Label_Histo.setPixmap(pixmap)
    '''
