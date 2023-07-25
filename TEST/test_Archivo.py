import unittest
from BLL import BLL_Archivo
from BLL import BLL_Fecha



class Test_Archivo(unittest.TestCase):

    def test_escribirArchivo(self):
        
        archivo = BLL_Archivo.Archivo(".//DATA//CSVS//", "prueba.csv")
        archivo.escribirArchivo("prueba")
        file = open(".//DATA//CSVS//prueba.csv", mode = "r", encoding='utf-8')
        for line in file.readlines():
            self.assertIn("prueba", line)

    def test_escrbirLogTXT(self):
        fecha = BLL_Fecha.Fecha()
        archivo = BLL_Archivo.Archivo(".//DATA//LOGS//", "logPrueba.txt")
        archivo.escribirLogTXT("prueba Archivo", "Ran")
        file = open(".//DATA//LOGS//Logs.txt", mode = "r", encoding='utf-8')
        self.assertIn("prueba", file.read())    

