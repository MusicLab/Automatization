import unittest
from BLL import BLL_Grafico_Personalizado
from BLL import BLL_Cliente
from BLL import BLL_Fecha
from DAL import DAL_Mapper_Cliente
import matplotlib.pyplot as plt




class Test_Grafico_Personalizado(unittest.TestCase):

    def test_crearGraficoPersonalizado(self):
        
        grafico = BLL_Grafico_Personalizado.Grafico_Personalizado()
        cliente = BLL_Cliente.Cliente()
        fecha = BLL_Fecha.Fecha()
        DAL_Mapper_Cliente.Mapper_Cliente().conexion.asignarAtributos("**")
        
        fechaInicio = fecha.fechaInicio("diario", 10)
        fechaFin = fecha.fechaFin()
        listaClientes = cliente.crearListaDB()
        for cliente in listaClientes:
            if cliente.nombre == "Banco Patagonia":
                
                grafico.graficoPersonalizado("Barras", "Exploits", "filename", cliente, fechaInicio, fechaFin).show()
 
        self.assertEqual(True, True)

    def test_crearGraficoPersonalizadoDash(self):
        
        grafico = BLL_Grafico_Personalizado.Grafico_Personalizado()
        cliente = BLL_Cliente.Cliente()
        fecha = BLL_Fecha.Fecha()
        DAL_Mapper_Cliente.Mapper_Cliente().conexion.asignarAtributos("**")
        
        fechaInicio = fecha.fechaInicio("diario", 10)
        fechaFin = fecha.fechaFin()
        listaClientes = cliente.crearListaDB()
        for cliente in listaClientes:
            if cliente.nombre == "Banco Patagonia":
                
                grafico.graficoPersonalizadoDash("Histograma", "DeviceCount", "noHaceFaltaColumnaReemplazarPds", "todos", fechaInicio, fechaFin)
                #grafico.graficoPersonalizadoDash("Barras", "Exploits", "filename", cliente, fechaInicio, fechaFin)

        self.assertEqual(True, True)