from BLL import BLL_Cliente
from PySide2.QtWidgets import QTableWidgetItem
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2.QtGui import QPixmap, QImage
from .ui_interface import  *
import os
import shutil

cliente = BLL_Cliente.Cliente()

class ListaClientes(QMainWindow):
    def __init__(self, tableWidget, ui):
        super().__init__()
        self.tableWidget = tableWidget
        self.ui = ui
        self.ui.stackedWidget.currentChanged.connect(self.listar_clientes)

        self.ruta_imagen_seleccionada = None

    def convert_periodicidad(self, periodicidad):
        if periodicidad == "0":
            return "Diario"
        elif periodicidad == "1":
            return "Semanal"
        elif periodicidad == "2":
            return "Mensual"
        else:
            return ""

    def listar_clientes(self):
        datos_clientes = cliente.leerClientesDB()

        self.tableWidget.setRowCount(len(datos_clientes))
        for row, cliente_tabla in enumerate(datos_clientes):
            tid = cliente_tabla[0]
            nombre_cliente = cliente_tabla[1]
            region = cliente_tabla[2]
            token = cliente_tabla[3]
            aid = cliente_tabla[4]
            sid = cliente_tabla[5]
            logo = cliente_tabla[6]
            periodicidad = cliente_tabla[7]

            periodicidad_texto = self.convert_periodicidad(periodicidad)

            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(tid)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(nombre_cliente))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(region))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(token))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(aid))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(sid))
            self.tableWidget.setItem(row, 0, QTableWidgetItem(logo))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(periodicidad_texto))


    def cliente_seleccionado(self):
        if self.ui is None:
            return
        
        self.ui.btn_aceptarmod.setVisible(True)
        self.ui.btn_borrarcli.setVisible(True)
        self.ui.btn_act_logo.setVisible(True)
        # Obtener la fila seleccionada
        selected_row = self.ui.tableWidget.currentRow()

        ruta_base = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir, 'soccrate2', 'Presentacion'))

        # Verificar si se ha seleccionado alguna fila
        if selected_row >= 0:
            # Obtener los datos de la fila seleccionada
            tid_item = self.ui.tableWidget.item(selected_row, 3)
            nombre_item = self.ui.tableWidget.item(selected_row, 1)
            region_item = self.ui.tableWidget.item(selected_row, 7)
            token_item = self.ui.tableWidget.item(selected_row, 5)
            aid_item = self.ui.tableWidget.item(selected_row, 2)
            sid_item = self.ui.tableWidget.item(selected_row, 4)
            logo_item = self.ui.tableWidget.item(selected_row, 0)
            periodicidad_item = self.ui.tableWidget.item(selected_row, 6)
            
            # Obtener el texto de los items seleccionados
            tid = tid_item.text()
            nombre_cliente = nombre_item.text()
            region = region_item.text()
            token = token_item.text()
            aid = aid_item.text()
            sid = sid_item.text()
            logo = logo_item.text()
            periodicidad_texto = periodicidad_item.text()
            
            # Mostrar los datos en los labels correspondientes
            self.ui.entrylist_tid.setText(tid)
            self.ui.entrylist_nombre.setText(nombre_cliente)
            self.ui.combol_region.setCurrentText(region)
            self.ui.entrylist__token.setText(token)
            self.ui.entrylist_aid.setText(aid)
            self.ui.entrylist_sid.setText(sid)
            self.ui.entrylist_logo.setText(logo)
            self.ui.combol_perio.setCurrentText(periodicidad_texto)

            # Cargar la imagen del cliente en el QLabel correspondiente
            ruta_imagen = os.path.normpath(os.path.join(ruta_base, logo))
            pixmap = QPixmap(ruta_imagen)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(self.ui.show_logo.width(), self.ui.show_logo.height(), QtCore.Qt.KeepAspectRatio)
                self.ui.show_logo.setPixmap(pixmap)
            else:
                self.ui.show_logo.setText('No se pudo cargar \nla imagen')

    def seleccionar_imagen(self):
        # Abrir la ventana de diálogo para seleccionar la imagen
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Archivos de imagen (*.png *.jpg *.jpeg)")

        if ruta_imagen:
            # Cargar la imagen en el QLabel correspondiente
            imagen = QImage(ruta_imagen)
            if not imagen.isNull():
                pixmap = QPixmap.fromImage(imagen)
                pixmap = pixmap.scaled(self.ui.show_logo.width(), self.ui.show_logo.height(), QtCore.Qt.KeepAspectRatio)
                self.ui.show_logo.setPixmap(pixmap)
                self.ruta_imagen_seleccionada = ruta_imagen
            else:
                QMessageBox.critical(self, "Error", "No se pudo cargar la imagen seleccionada.")

    def actualizar_tabla(self):
        datos_clientes = cliente.leerClientesDB()

        def convert_periodicidad(periodicidad):
            if periodicidad == "0":
                return "Diario"
            elif periodicidad == "1":
                return "Semanal"
            elif periodicidad == "2":
                return "Mensual"
            else:
                return ""

        # Crear una lista de tuplas que contenga los datos de cada cliente
        clientes_ordenados = []
        for cliente_tabla in datos_clientes:
            tid = cliente_tabla[0]
            nombre_cliente = cliente_tabla[1]
            region = cliente_tabla[2]
            token = cliente_tabla[3]
            aid = cliente_tabla[4]
            sid = cliente_tabla[5]
            logo = cliente_tabla[6]
            periodicidad = cliente_tabla[7]

            periodicidad_texto = convert_periodicidad(periodicidad)

            clientes_ordenados.append((nombre_cliente, tid, logo, aid, sid, token, periodicidad_texto, region))

        # Ordenar la lista de tuplas por el nombre del cliente
        clientes_ordenados.sort(key=lambda x: x[0])

        self.ui.tableWidget.setRowCount(len(clientes_ordenados))
        for row, cliente_tupla in enumerate(clientes_ordenados):
            nombre_cliente, tid, logo, aid, sid, token, periodicidad_texto, region = cliente_tupla

            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(tid)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(nombre_cliente))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(region))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(token))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(aid))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(sid))
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(logo))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(periodicidad_texto))

    def modificar_cliente(self):
        # Obtener los datos de los entrys y combobox
        nombre = self.ui.entrylist_nombre.text()
        region = self.ui.combol_region.currentText()
        token = self.ui.entrylist__token.text()
        tid = self.ui.entrylist_tid.text()
        aid = self.ui.entrylist_aid.text()
        sid = self.ui.entrylist_sid.text()
        logo = self.ui.entrylist_logo.text()
        periodicidad_texto = self.ui.combol_perio.currentText()

        ruta_base = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir, 'soccrate2', 'Presentacion'))
        ruta_imagen_actual = os.path.normpath(os.path.join(ruta_base, logo))

        if self.ruta_imagen_seleccionada and os.path.abspath(self.ruta_imagen_seleccionada) != os.path.abspath(ruta_imagen_actual):
            # Obtener la ruta de la nueva imagen seleccionada
            ruta_imagen_nueva = os.path.abspath(self.ruta_imagen_seleccionada)
            # Obtener el nombre del archivo de la imagen actual
            nombre_archivo_actual = os.path.basename(ruta_imagen_actual)
            # Obtener la ruta de la carpeta de logos
            ruta_carpeta_logos = os.path.join(ruta_base, "logos")
            # Copiar la nueva imagen en la carpeta de logos y sobrescribir la imagen actual
            shutil.copy(ruta_imagen_nueva, os.path.join(ruta_carpeta_logos, nombre_archivo_actual))
            # Actualizar la ruta del logo a la ruta relativa de la carpeta de logos en la db
            #logo = os.path.relpath(os.path.join(ruta_carpeta_logos, nombre_archivo_actual), ruta_base).replace("\\", "/")

            self.actualizar_tabla()

        if periodicidad_texto == "Diario":
            periodicidad = "0"
        elif periodicidad_texto == "Semanal":
            periodicidad = "1"
        elif periodicidad_texto == "Mensual":
            periodicidad = "2"
        else:
            periodicidad = ""

        # Mostrar un mensaje de confirmación
        confirmacion = QMessageBox.question(self, "Confirmación", "¿Estás seguro de que deseas modificar este cliente?",
                                                QMessageBox.Yes | QMessageBox.No)
        if confirmacion == QMessageBox.Yes:
            try:
                # Modificar los datos del cliente en la base de datos
                cliente.modificarDB(nombre, region, token, tid, aid, sid, logo, periodicidad)

                # Mostrar un mensaje de éxito
                QMessageBox.information(self, "Éxito", "Los datos del cliente se han modificado correctamente.")

                self.ui.entrylist_nombre.clear()
                self.ui.entrylist__token.clear()
                self.ui.entrylist_tid.clear()
                self.ui.entrylist_aid.clear()
                self.ui.entrylist_sid.clear()
                self.ui.entrylist_logo.clear()
                self.ui.show_logo.clear()

                # Actualizar la tabla
                self.actualizar_tabla()
            except Exception as e:
                # Mostrar un mensaje de error
                QMessageBox.critical(self, "Error", f"No se pudo modificar el cliente. Error: {str(e)}")
        else:
            # Mostrar un mensaje de cancelación
            QMessageBox.information(self, "Cancelación", "La modificación del cliente se ha cancelado.")

    def borrar_cliente(self):
        # Obtener la fila seleccionada
        selected_row = self.ui.tableWidget.currentRow()

        # Verificar si se ha seleccionado alguna fila
        if selected_row >= 0:
            # Obtener el ID del cliente seleccionado
            tid_item = self.ui.tableWidget.item(selected_row, 3)
            tid = tid_item.text()
            nombre_cliente_item = self.ui.tableWidget.item(selected_row, 1)
            nombre_cliente = nombre_cliente_item.text()

            # Mostrar un mensaje de confirmación
            confirmacion = QMessageBox.question(self, "Confirmación", f"¿Estás seguro de que deseas eliminar el cliente {nombre_cliente}?",
                                                QMessageBox.Yes | QMessageBox.No)
            if confirmacion == QMessageBox.Yes:
                try:
                    # Eliminar el cliente de la base de datos
                    cliente.borrarDB(tid)

                    # Eliminar la fila seleccionada de la tabla
                    self.ui.tableWidget.removeRow(selected_row)

                    # Mostrar un mensaje de éxito
                    QMessageBox.information(self, "Éxito", f"El cliente {nombre_cliente} se ha eliminado correctamente.")

                    self.ui.entrylist_nombre.clear()
                    self.ui.entrylist__token.clear()
                    self.ui.entrylist_tid.clear()
                    self.ui.entrylist_aid.clear()
                    self.ui.entrylist_sid.clear()
                    self.ui.entrylist_logo.clear()
                    self.ui.show_logo.clear()

                except Exception as e:
                    # Mostrar un mensaje de error
                    QMessageBox.critical(self, "Error", f"No se pudo eliminar el cliente {nombre_cliente}. Error: {str(e)}")
            else:
                # Mostrar un mensaje de cancelación
                QMessageBox.information(self, "Cancelación", f"La eliminación del cliente {nombre_cliente} se ha cancelado.")
        else:
            # Mostrar un mensaje de advertencia si no se ha seleccionado ninguna fila
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una fila para eliminar.")