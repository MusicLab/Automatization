import unittest
from BLL import BLL_Log



class Test_Log(unittest.TestCase):

    def test_escribirLog(self):
        
        BLL_Log.Log().escribir("prueba", "Banco Patagonia", "advertencia")
        file = open("./DATA//LOGS//Logs.txt", mode = "r", encoding='utf-8')
        self.assertIn("Banco Patagonia: advertencia - prueba", file.read()) 
