from PySide2.QtWidgets import QMessageBox
from PySide2 import QtWidgets
from .ui_interface import  *
import csv
from BLL import BLL_Hash
from BLL import BLL_Cliente
from BLL import BLL_Archivo



class Hashes(QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        self.cliente = BLL_Cliente.Cliente()
        self.listaClientes = self.cliente.leerClientesDB()
        self.listaojb = self.cliente.crearListaDB()

        self.ui.stackedWidget.currentChanged.connect(self.listar_clientes_hashes)
        self.ui.progressBar.setVisible(False)

        self.first_load = True

    def listar_clientes_hashes(self):
        test = []
        checkbox = None
        if self.ui.stackedWidget.currentWidget() == self.ui.hashes and self.first_load:
            # Realiza la conexión y la llamada a leerClientesDB() solo en la primera carga
            test = self.cliente.convertirListaClientesADict(self.listaClientes)
            test = sorted(test, key=lambda x: x['nombre']) #sorted es una funcion que indica por que valor de cada diccionario se va a ordenar la lista. 

            self.first_load = False
 

        #Ocultar botones y frames al cargar la pagina
        self.ui.FrameSubContent_Hashes.setVisible(False)
        self.ui.btn_hashes_cargar.setVisible(False)
        self.ui.btn_hashes_borrar.setVisible(False)

        # Agregar el QCheckBox "Seleccionar todos"
        checkbox_select_all = QCheckBox("Seleccionar todos")
        checkbox_select_all.setStyleSheet("QCheckBox::indicator { width: 50px; height: 30px; }"
                    "QCheckBox { font-family: Poppins; font-size: 14px; width:300px; }"
                    "QCheckBox:hover { background-color: rgb(51, 51, 51); color: white; }") 
        checkbox_select_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.List_Clientes.addItem(QListWidgetItem())
        self.ui.List_Clientes.setItemWidget(self.ui.List_Clientes.item(0), checkbox_select_all)

        # Conectar la señal "stateChanged" del QCheckBox "Seleccionar todos" a la función "seleccionar_todos"
        checkbox_select_all.stateChanged.connect(self.seleccionar_todos)

        # Agregar cada usuario como un elemento del QListWidget
        for usuario in test:
            nombre_usuario = usuario["nombre"]  # Obtener el nombre del usuario desde el diccionario
            item = QListWidgetItem()
            if checkbox is None:
                checkbox = QCheckBox(nombre_usuario)
            else:
                checkbox = QCheckBox(nombre_usuario, parent=checkbox)

            checkbox.setStyleSheet("QCheckBox::indicator { width: 50px; height: 30px; }"
                        "QCheckBox { font-family: Poppins; font-size: 14px; width:300px; }"
                        "QCheckBox:hover { background-color: rgb(51, 51, 51); color: white; }") 
            #checkbox.setStyleSheet()
            checkbox.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.List_Clientes.addItem(item)
            self.ui.List_Clientes.setItemWidget(item, checkbox)

            # Establecer la selección del QListWidgetItem cuando se selecciona el QCheckBox
            #checkbox.clicked.connect(lambda state, item=item, checkbox=checkbox: item.setSelected(checkbox.isChecked()))
 
        # Agregar una línea debajo de cada elemento en el QListWidget
        item_style = "QListWidget::item { border-bottom: 1px solid gray; }"
        self.ui.List_Clientes.setStyleSheet(item_style)

        # Ajustar la altura de cada fila del QListWidget a 50 píxeles
        row_style = "QListWidget::item { min-height: 30px; }"
        self.ui.List_Clientes.setStyleSheet(self.ui.List_Clientes.styleSheet() + row_style)


        #checkbox.clicked.connect(lambda state, item=item: item.setSelected(checkbox.isChecked()))
    
    def seleccionar_todos(self, state):
        for i in range(1, self.ui.List_Clientes.count()):
            item = self.ui.List_Clientes.item(i)
            checkbox = self.ui.List_Clientes.itemWidget(item)
            checkbox.setChecked(state)

    def mostrar_usuarios_seleccionados(self):
        usuarios_seleccionados = [] # Crear una lista vacía para almacenar los usuarios seleccionados
        listafinal = []
        seleccionados = 0  # Contador para llevar el registro de la cantidad de usuarios seleccionados
        total_usuarios = self.ui.List_Clientes.count() - 1  # Restar 1 para excluir el primer elemento (Seleccionar todos)

        for i in range(1, total_usuarios + 1):
            item = self.ui.List_Clientes.item(i)
            checkbox = self.ui.List_Clientes.itemWidget(item)
            if checkbox is not None and checkbox.isChecked():
                usuarios_seleccionados.append(checkbox.text()) # Agregar el nombre de usuario a la lista de usuarios seleccionados si el QCheckBox está seleccionado
                seleccionados += 1

        if seleccionados == 0:
            QMessageBox.warning(self, "Atención", "Debe seleccionar al menos un cliente para mostrar.")
            self.ui.entry_hashes.clear()
        elif seleccionados == total_usuarios:
            self.ui.entry_hashes.setPlaceholderText("Ingrese el hash para todos los usuarios aquí.")
            self.ui.btn_hashes_cargar.setVisible(True)
            self.ui.btn_hashes_borrar.setVisible(True)
            self.ui.FrameSubContent_Hashes.setVisible(True)
        else:
            self.ui.entry_hashes.setPlaceholderText("Ingrese el Hash para: " + ", ".join(usuarios_seleccionados) + " aquí.")
            self.ui.btn_hashes_cargar.setVisible(True)
            self.ui.btn_hashes_borrar.setVisible(True)
            self.ui.FrameSubContent_Hashes.setVisible(True)
        # Imprimir los usuarios seleccionados en la consola
        print("Usuarios seleccionados:")
        for usuario in usuarios_seleccionados:
            print(usuario)

        for usuario in usuarios_seleccionados:
            for cliente in self.listaojb:
                if cliente.nombre == usuario:
                    listafinal.append(cliente)
    
        return listafinal
       
    
    def open_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "CSV Files (*.csv);;Text Files (*.txt)")
        global ruta_archivo
        ruta_archivo = filepath

        self.ui.entry_hashes.clear()
        self.ui.entry_hashes.insert(ruta_archivo)

        # Abre el archivo CSV seleccionado y lee los datos en una lista
        with open(ruta_archivo, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            data = list(csvreader)

        # Imprime la lista para verificar que los datos se hayan leído correctamente
        print("Contenido del archivo:")
        for row in data:
            print(row)
        
    def cargar_hashes(self):
        bll_hashes = BLL_Hash.Hash()
        bll_archivo = BLL_Archivo.Archivo()

        # Obtener los datos de entrada
        tipoLista = {"Global Quarentine": "quarantine", "Global Safe": "safe"}
        listType = tipoLista[self.ui.tipolista_combo.currentText()]
        razon = self.ui.entry_reason.text()
        categoria = self.ui.category_combo.currentText()

        # Obtener la lista de hashes
        listaHashes = []
        entry_hash = str(self.ui.entry_hashes.text())
        if entry_hash.endswith('.csv'):
            # si entry_hash es un archivo CSV, llama a bll_archivo.leerCSV para obtener la lista de hashes
            listaHashes = bll_archivo.leerCSV(entry_hash)
        else:
            # si entry_hash no es un archivo CSV, convierte el valor en una lista y lo agrega a la listaHashes
            listaHashes.append(entry_hash)

        # Obtener los usuarios seleccionados
        usuarios_seleccionados = self.mostrar_usuarios_seleccionados()

        print(f"Usuario: {usuarios_seleccionados}, List Type: {listType}, Razon: {razon}, Categoria: {categoria}, Lista Hashes: {listaHashes}")
                
        # Configurar la barra de progreso
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(len(listaHashes)) 
        self.ui.progressBar.setVisible(True) 

        # Realizar la carga de hashes 
        #for i, hash in enumerate(listaHashes):   
        response_code = bll_hashes.cargarMultiHashes(usuarios_seleccionados , listaHashes, listType, razon, categoria)
            
            # Actualizar la barra de progreso
        self.ui.progressBar.setValue(len(listaHashes))

            # Permitir que la interfaz gráfica se actualice
        QtWidgets.QApplication.processEvents()

        if response_code == 200:
            QMessageBox.information(self, "Carga de Hashes", "Los hashes se cargaron correctamente.")
            self.ui.entry_hashes.clear() 
            self.ui.entry_reason.clear()  
        else:
            QMessageBox.critical(self, "Carga de Hashes", "Hubo un error al cargar los hashes. Código de respuesta: {}".format(response_code))
                 
            
    def eliminar_data(self):
        bll_hashes = BLL_Hash.Hash()
        usuarios_seleccionados = self.mostrar_usuarios_seleccionados()
        
        print(usuarios_seleccionados)

        tipoLista = {"Global Quarentine": "quarantine", "Global Safe": "safe"}
       
        if usuarios_seleccionados:
            exito_eliminar = True  # Variable para controlar si se eliminaron todos los hashes exitosamente
            for usuario in usuarios_seleccionados:
                entry_data = str(self.ui.entry_hashes.text())
                listType = tipoLista[self.ui.tipolista_combo.currentText()]

                status_code = bll_hashes.eliminar(usuario, listType, entry_data)  # Obtener el status_code de la función eliminar

                if status_code == 200:
                    print(f"Usuario: {usuario.nombre}, List Type: {listType}, hash: {entry_data}")
                else:
                    exito_eliminar = False  # Si hay un error en la eliminación, cambiar el valor de la variable a False

            if exito_eliminar:
                QMessageBox.information(self, "Eliminacion de Hashes", "El Hash fue eliminado correctamente.")
                self.ui.entry_hashes.clear() 
                self.ui.entry_reason.clear()  
            else:
                QMessageBox.warning(self, "Eliminacion de Hashes", "Hubo un error al eliminar el hash.")
        else:
            QMessageBox.warning(self, "Eliminacion de Hashes", "No se seleccionaron usuarios.")
            