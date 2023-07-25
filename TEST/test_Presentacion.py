from PySide2.QtWidgets import QApplication
import sys
import unittest
import os
from Presentacion import Presentacion_Main
from Presentacion.ui_interface import *
from PySide2.QtWidgets import QApplication
from DAL import DAL_Conexion


class TestApp(unittest.TestCase):
    def test_app(self):
            conexion = DAL_Conexion.Conexion()
            if(os.path.exists(os.getcwd() + "//DATA//CONFIG//Conexion.json")):
                conexion.leerArchivo()
            app = QApplication(sys.argv)
            window = Presentacion_Main.App()
            window.show()
            app.exec_()
