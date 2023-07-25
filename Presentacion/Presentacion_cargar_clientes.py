from BLL import BLL_Cliente
from PySide2.QtWidgets import QFileDialog, QMessageBox
from .ui_interface import  *
import os
import shutil

class CargarClientes(QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def agregar_cliente(self):
        cliente = BLL_Cliente.Cliente()

        # Obtener los datos de los QLineEdit y QComboBox
        nombre = self.ui.entry_nombre.text()
        region = self.ui.regio_combo.currentText()
        token = self.ui.entry_token.text()
        tid = self.ui.entry_tid.text()
        aid = self.ui.entry_aid.text()
        sid = self.ui.entry_sid.text()
        periodicidad = self.ui.perio_combo.currentText()

        # Verificar que todos los campos tengan valores
        logo_cargado = self.ui.label_logo.text() != ""
        if not all([nombre, region, token, tid, aid, sid, periodicidad, logo_cargado]):
            mensaje = "Debe completar todos los campos para agregar un cliente."
            QMessageBox.warning(self, "Advertencia", mensaje)
            return
            
        # Verificar que el TID no esté en uso
        clientes_existentes = cliente.leerClientesDB()
        tids_existentes = [cliente[0] for cliente in clientes_existentes]
        if tid in tids_existentes:
            mensaje = f"El Tenant ID '{tid}' ya se encuentra en uso. Por favor, seleccione otro TID."
            QMessageBox.warning(self, "Advertencia", mensaje)
            return

        ruta_carpeta = "../Presentacion/logos/"
        ruta_imagen = ruta_carpeta + nombre  # Crear la ruta completa de la imagen
        logo = ruta_imagen

        # Convertir el valor de periodicidad a un número entero
        conversion_periodicidad = {"Diario": 0, "Semanal": 1, "Mensual": 2}
        periodicidad_entero = conversion_periodicidad.get(periodicidad)

        mensaje_confirmacion = f"¿Desea cargar el cliente '{nombre}'?"
        respuesta = QMessageBox.question(self, "Confirmación", mensaje_confirmacion, QMessageBox.Yes | QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            # Llamar a la función para agregar el cliente a la base de datos
            cliente.agregarDB(nombre, region, token, tid, aid, sid, logo, periodicidad_entero)

            ruta_imagen_origen = self.ruta_imagen_seleccionada
            if ruta_imagen_origen:
                carpeta_principal = os.path.dirname(__file__)
                carpeta_logo = os.path.join(carpeta_principal,"logos")
                ruta_imagen_destino = os.path.join(carpeta_logo, nombre + ".png")
                try:
                    shutil.copy(ruta_imagen_origen, ruta_imagen_destino)
                except Exception as e:
                    print(f"Error al copiar la imagen: {str(e)}")
                
            self.ui.entry_nombre.clear()
            self.ui.entry_token.clear()
            self.ui.entry_tid.clear()
            self.ui.entry_aid.clear()
            self.ui.entry_sid.clear()
            self.ui.label_logo.clear()

            mensaje_exito = f"El cliente '{nombre}' se ha cargado correctamente."
            QMessageBox.information(self, "Éxito", mensaje_exito)
        else:
            mensaje_cancelacion = f"No se ha cargado el cliente '{nombre}'."
            QMessageBox.warning(self, "Cancelación", mensaje_cancelacion)

    def seleccionar_imagen(self):
        # Abrir la ventana de diálogo para seleccionar la imagen
        ruta_imagen, _ = QFileDialog.getOpenFileName(None, "Seleccionar imagen", "", "Archivos de imagen (*.png *.jpg *.jpeg)")

        if ruta_imagen:
            # Obtener el nombre de archivo y la ruta
            info = QFileInfo(ruta_imagen)
            nombre_archivo = info.fileName()

            # Mostrar el nombre del archivo en el label_logo
            self.ui.label_logo.setText(nombre_archivo)

            # Guardar la ruta de la imagen seleccionada para usarla en la función agregar_cliente
            self.ruta_imagen_seleccionada = ruta_imagen
            