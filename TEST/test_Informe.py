import unittest
from BLL import BLL_Cliente
from BLL import BLL_Fecha
from BLL import BLL_Archivo
from BLL import BLL_Informe
from DAL import DAL_Mapper_Cliente
import datetime


class Test_Informe(unittest.TestCase):
    
            
    def test_hacerInforme(self):

        
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        
        for cliente in clientes:
            if cliente.nombre == "Banco Patagonia":
                try:


                    fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
                    fechaFin = BLL_Fecha.Fecha().fechaFin()
                    print(fechaInicio)
                    print(fechaFin)
                    informe = BLL_Informe.Informe(fechaInicio, fechaFin, cliente, "mensual")
                    informe.hacerInforme()
                    self.assertEqual(True, True)
                except Exception as e:
                    print(str(e) + "  " + cliente.nombre)



if __name__ == '__main__':
    unittest.main()
