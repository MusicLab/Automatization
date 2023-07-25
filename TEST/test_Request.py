import unittest
import os
import sys
import csv
from BLL import BLL_Request
from BLL import BLL_Cliente
from BLL import BLL_Fecha
from DAL import DAL_Mapper_Cliente
from DAL import DAL_Mapper_Eventos
from DAL import DAL_Conexion

class Test_Request(unittest.TestCase):
    def test_ejecutarMapperLecturaDiario(self):

        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        request = BLL_Request.Request()
        fecha = BLL_Fecha.Fecha()
        listaClientes = BLL_Cliente.Cliente().crearListaDB()
        headerDevices = ['OperativeSystem', 'DeviceName', 'AgentVersion', 'Policy', 'IPs', 'DateOffline', 'ZoneName', 'LastLoggedInUser']
        headerMemProt = ['DeviceName', 'UserName', 'ViolationType', 'Action', 'FilePath', 'FileName', 'Created', 'ProcessID']
        headerThreats = ['', 'SHA256', 'FileStatus', 'DeviceName', 'FilePath', 'FileName', 'Classification', 'SubClass', 'FileOwner', 'DriveType', 'DateFound', 'OrigenDeDato']     
        
        for cliente in listaClientes:
            if cliente.nombre == "Banco Patagonia":

                rutaArchivo = os.getcwd() + "/DATA/CSVS/" + str(fecha.ahora().year) + " - " + str(fecha.ahora().month) + " - " + cliente.nombre    
                archivoMemProt = rutaArchivo + " - Memory Protection.csv"
                archivoDevices = rutaArchivo + " - Devices.csv"
                archivoExploit = rutaArchivo + " - Exploits.csv"
                archivoThreat = rutaArchivo + " - Threats.csv"
                request.ejecutarMapperLectura(fecha, False, False, cliente)

                self.assertTrue(os.path.exists(archivoDevices))
                self.assertTrue(os.path.exists(archivoMemProt))
                self.assertTrue(os.path.exists(archivoExploit))
                self.assertTrue(os.path.exists(archivoThreat))

                with open(archivoDevices, 'r') as fileDevice:
                    reader = csv.reader(fileDevice)
                    header = next(reader) 
                    #data_types = next(reader) 

                self.assertEqual(headerDevices, header)

                
                with open(archivoMemProt, 'r') as fileMemProt:
                    reader = csv.reader(fileMemProt)
                    header = next(reader) 
                    #data_types = next(reader) 

                self.assertEqual(headerMemProt, header)


                with open(archivoExploit, 'r') as fileExploit:
                    reader = csv.reader(fileExploit)
                    header = next(reader) 
                    #data_types = next(reader) 

                self.assertEqual(headerMemProt, header)


                with open(archivoThreat, 'r') as fileThreats:
                    reader = csv.reader(fileThreats)
                    header = next(reader) 
                    #data_types = next(reader) 

                self.assertEqual(headerThreats, header)


    def test_RequestZoho(self):
        cliente = BLL_Cliente.Cliente()
        conexion = DAL_Conexion.Conexion()
        request = BLL_Request.Request()
        conexion.asignarAtributos("**")
        
        listaClientes = cliente.crearListaDB()

        for cliente in listaClientes:
            if cliente.nombre == "Ran":
                response = request.requestZoho(cliente, 'accounts')
                print(response)



    def test_creacion_token(self):

        cliente = BLL_Cliente.Cliente()
        conexion = DAL_Conexion.Conexion()
        request = BLL_Request.Request()
        conexion.asignarAtributos("**")
        
        listaClientes = cliente.crearListaDB()
        for cliente in listaClientes:
            if cliente.nombre == "Ran":
                request = BLL_Request.Request()
                response = request.requestZoho(cliente, 'accounts')
                matchesClientes = request.matchearClientesZoho(response, cliente)
                print(matchesClientes)
                self.assertEqual(type(matchesClientes), list)
                self.assertEqual(matchesClientes[0]['nombre'], "Ran")

    def test_PruebaZoho(self):
        cliente = BLL_Cliente.Cliente()
        conexion = DAL_Conexion.Conexion()
        request = BLL_Request.Request()
        conexion.asignarAtributos("**")
        
        listaClientes = cliente.crearListaDB()
        ran = cliente.leerClienteEspecifico("Ran")
        print(ran.tid)
        datos = request.requestZoho(ran, 'accounts')
        
        for cliente in listaClientes:
            matches = request.matchearClientesZoho(datos, cliente)
            print(matches)
            for clienteMatcheado in matches:
                print(clienteMatcheado['nombre'])
                if clienteMatcheado['nombre'] == cliente.nombre:
                    request.insertarDatosZoho(cliente, clienteMatcheado['id'])
                    self.assertEqual(clienteMatcheado['nombre'], cliente.nombre)



