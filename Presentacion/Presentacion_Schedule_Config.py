from PySide2.QtWidgets import QMessageBox
from .ui_interface import  *
import os
import re

class Schedule(QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        
    def mostrar_horario(self):
        # Ruta del archivo
        ruta_archivo = os.getcwd() + "//DATA//CONFIG//scheduleconf.txt"

        # Leer el contenido del archivo
        with open(ruta_archivo, "r") as f:
            contenido = f.read()

        # Asignar el contenido del archivo al QLabel
        self.ui.label_schedule.setText(contenido)

    def guardar_horario(self):
        # Ruta del archivo
        ruta_archivo = os.getcwd() + "//DATA//CONFIG//scheduleconf.txt"

        # Obtener el horario ingresado en el QLineEdit
        horario = self.ui.entry_schedule.text()

        # Validar la longitud máxima
        if len(horario) > 5:
            QMessageBox.warning(self, "Error", "El horario ingresado excede la longitud máxima permitida (5 caracteres).")
            return

        # Validar el horario utilizando una expresión regular
        if not re.match(r'^[\d:]+$', horario):
            QMessageBox.warning(self, "Error", "El horario ingresado es inválido. Por favor, ingresa solo números y ':'")
            return

        try:
            # Escribir el horario en el archivo (sobreescribiendo el contenido anterior)
            with open(ruta_archivo, "w") as f:
                f.write(horario)
        except Exception as e:
            # Mostrar un cuadro de diálogo de error si ocurre un problema al guardar el horario
            QMessageBox.critical(self, "Error", f"No se pudo guardar el horario:\n{str(e)}")
        else:
            # Mostrar un cuadro de diálogo de confirmación si se guarda el horario correctamente
            QMessageBox.information(self, "Confirmación", "El horario se ha guardado correctamente.")

            # Actualizar el QLabel con el nuevo horario
            self.ui.label_schedule.setText(horario)
            self.ui.entry_schedule.clear()