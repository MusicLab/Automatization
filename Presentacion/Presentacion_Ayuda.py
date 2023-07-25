import os
from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2.QtCore import QUrl
from PySide2.QtGui import QDesktopServices

class Manual:

    def descargar_archivo(self):
        # Ruta del archivo que se va a descargar
        ruta_manual = os.getcwd() + "//DATA//MANUAL//RAN - SOCcrate 2.0 - Manual de Usuario.docx" ### MODIFICAR CON LA RUTA DE SOC

        # Verificar si el archivo existe
        if not os.path.isfile(ruta_manual):
            QMessageBox.critical(None, "Error", "El archivo no existe.")
            return

        # Obtener el directorio donde el usuario quiere guardar el archivo
        dialogo_guardar = QFileDialog()
        dialogo_guardar.setFileMode(QFileDialog.AnyFile)
        dialogo_guardar.setAcceptMode(QFileDialog.AcceptSave)
        dialogo_guardar.setDirectory(os.path.expanduser("~"))
        dialogo_guardar.setNameFilter("Archivos (*.*)")
        dialogo_guardar.selectFile(os.path.basename(ruta_manual)) # Establecer el nombre del archivo por defecto
        if dialogo_guardar.exec_() == QFileDialog.Accepted:
            ruta_guardado = os.path.join(dialogo_guardar.directory().path(), os.path.basename(ruta_manual))

            # Copiar el archivo a la ruta de guardado seleccionada
            try:
                with open(ruta_manual, "rb") as archivo_origen:
                    with open(ruta_guardado, "wb") as archivo_destino:
                        archivo_destino.write(archivo_origen.read())

                QMessageBox.information(None, "Descarga exitosa", "El archivo se ha descargado exitosamente.")
            except Exception as e:
                QMessageBox.critical(None, "Error", "Se produjo un error al descargar el archivo: {}.".format(str(e)))

    def abrir_enlace(self):
        enlace = "**"
        QDesktopServices.openUrl(QUrl(enlace))