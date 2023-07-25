import os
from PySide2.QtCore import QUrl
from PySide2.QtGui import QDesktopServices

class Dialogo:
    def abrir_informes(self):
        # Ruta de la carpeta
        ruta_informes = os.getcwd() + "//DATA//INFORMES"
        # Abrir la carpeta de descargas
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_informes))

    def abrir_logs(self):
        # Ruta de la carpeta
        ruta_logs = os.getcwd() + "//DATA//LOGS"
        # Abrir la carpeta de descargas
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_logs))

    def abrir_csv(self):
        # Ruta de la carpeta
        ruta_csv = os.getcwd() + "//DATA//CSVS"
        # Abrir la carpeta de descargas
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_csv))

        ################################# las rutas con soccrate #################################
