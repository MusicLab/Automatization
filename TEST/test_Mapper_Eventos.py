import unittest
import pandas as pd
from BLL import BLL_Cliente
from BLL import BLL_Fecha
from DAL import DAL_Mapper_Archivo
from DAL import DAL_Mapper_Cliente
from DAL import DAL_Mapper
from DAL import DAL_Mapper_Eventos
from DAL import DAL_Conexion




class Test_Mapper_Eventos(unittest.TestCase):
    


    def test_MapperDB(self):

        mapper = DAL_Mapper.Mapper()
        mapper.conexion.asignarAtributos("**")
        mapperArchivo = DAL_Mapper_Archivo.Mapper_Archivo()
        
        if(mapperArchivo.mapperVerificarEstadoArchivo() == False):
            mapper.mapperEncriptarArchivo()

        mapper.mapperConectarDB()
        
        #mapper.mapperDesconectarDB()
        self.assertEqual(True, True)
        
    def test_mapperLeerClientesDB(self):

        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        listaClienteDB = mapperCliente.mapperLeerClientesDB()


        print("LISTA DB: ", listaClienteDB)
        mapperCliente.mapperDesconectarDB()


        

    def test_AgregarClienteDB(self):

        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        mapperCliente.mapperAgregarClienteDB("nombreTest", "regionTe", "tokenTest", "tidTest", "aidTest", "sidTest", "logoTest", "1")

        mapperCliente.mapperDesconectarDB()
        self.assertEqual("funciono", "funciono")

    def test_BorrarClienteDB(self):

        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        mapperCliente.mapperBorrarClienteDB("tidTest")
        
        mapperCliente.mapperDesconectarDB()
        self.assertEqual("funciono", "funciono")

    def test_LeerEventosExploits(self):
 
        conexion = DAL_Conexion.Conexion("**")
        mapper = DAL_Mapper.Mapper(conexion)
        mapper.mapperConectarDB()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente(mapper.conexion)
        listaClienteDB = mapperCliente.mapperLeerClientesDB()
        listaCliente = BLL_Cliente.Cliente().crearLista(listaClienteDB)
        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("mensual", 24)
        fechaFin = fecha.fechaFin()
        for cliente in listaCliente:
            if cliente.nombre == "Gpat":
                result = mapper.leerEventos(cliente, "Devices", fechaInicio, fechaFin)
                print(result)   
                self.assertEqual(dict, type(result))


    def test_LeerUsuariosThreats(self):
        
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        listaCliente = BLL_Cliente.Cliente().crearListaDB()
        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("diario")
        fechaFin = fecha.fechaFin()
        for cliente in listaCliente:
            if cliente.nombre == "Banco Patagonia":
            
                mapperCliente.mapperConectarDB()
                result = DAL_Mapper_Eventos.Mapper_Eventos().leerEventos(cliente, "ThreatsUsuarios", fechaInicio, fechaFin)
                print(result)

    def test_LeerEventosDevices(self):
        #
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaFin = BLL_Fecha.Fecha().fechaActual
        print(fechaInicio, fechaFin)
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i
            
                result = DAL_Mapper_Eventos.Mapper_Eventos()
                result = result.leerEventos(patagonia, "Devices", fechaInicio, fechaFin)
                print(result)

    def test_LeerEventosThreats(self):
        
        
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        listaClienteDB = mapperCliente.mapperLeerClientesDB()
        listaCliente = BLL_Cliente.Cliente().crearListaDB()
        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("mensual", 24)
        fechaFin = fecha.fechaFin()
        for cliente in listaCliente:
            if cliente.nombre == "Banco Patagonia":
            
                mapperCliente.mapperConectarDB()
                result = DAL_Mapper_Eventos.Mapper_Eventos().leerEventos(cliente, "ThreatsOnly", fechaInicio, fechaFin)
                print(result)

    def test_EscribirEventosDevices(self):
        
        conexion = DAL_Conexion.Conexion("**")
        mapper = DAL_Mapper.Mapper(conexion)
        mapper.mapperConectarDB()
        fecha = BLL_Fecha.Fecha()
        fechaFin = fecha.fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente(conexion)
        listaClienteDB = mapperCliente.mapperLeerClientesDB()
        listaClientes = BLL_Cliente.Cliente().crearLista(listaClienteDB)
        df = pd.read_csv(".\soccrate2\DATA\CSVS\devices.csv", encoding='utf-8')
        for cliente in listaClientes:
            if cliente.tid == "tidTest":

                DAL_Mapper_Eventos.Mapper_Eventos.escribirEventos(mapper.conexion, cliente, df, fechaFin, "devices", "mensual")
    
    def test_EscribirEventosThreats(self):
        
        fecha = BLL_Fecha.Fecha()
        
        conexion = DAL_Conexion.Conexion("**")
        mapper = DAL_Mapper.Mapper(conexion)
        mapper.mapperConectarDB()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente(conexion)
        listaClienteDB = mapperCliente.mapperLeerClientesDB()
        listaClientes = BLL_Cliente.Cliente().crearLista(listaClienteDB)
        df = pd.read_csv(".\soccrate2\DATA\CSVS\\threats.csv", encoding='utf-8')
        for cliente in listaClientes:
            if cliente.tid == "tidTest":
                DAL_Mapper_Eventos.Mapper_Eventos.escribirEventos(mapper.conexion, cliente, df, fecha.fechaFin(), "threats", "mensual")
        mapper.mapperDesconectarDB()

    def test_EscribirEventosExploits(self):
        
        conexion = DAL_Conexion.Conexion("**")
        mapper = DAL_Mapper.Mapper(conexion)
        mapper.mapperConectarDB()
        fecha = BLL_Fecha.Fecha()
        fechaFin = fecha.fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente(conexion)
        listaClienteDB = mapperCliente.mapperLeerClientesDB()
        listaClientes = BLL_Cliente.Cliente().crearLista(listaClienteDB)
        df = pd.read_csv(".\soccrate2\DATA\CSVS\exploits.csv", encoding='utf-8')
        for cliente in listaClientes:
            if cliente.tid == "tidTest":
                DAL_Mapper_Eventos.Mapper_Eventos.escribirEventos(mapper.conexion, cliente, df, fechaFin, "exploits", "mensual")

        mapper.mapperDesconectarDB()



    def test_LeerUsuariosyDevicenames(self):
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        listaCliente = BLL_Cliente.Cliente().crearListaDB()
        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("diario")
        fechaFin = fecha.fechaFin()
        print(fechaInicio, fechaFin)
        for cliente in listaCliente:
            if cliente.nombre == "Banco Patagonia":
                result = DAL_Mapper_Eventos.Mapper_Eventos().leerEventos(cliente, "ThreatsUsuarios", fechaInicio, fechaFin)
                print(result)


    def test_LeerEventosCounts(self):
            mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
            mapperCliente.conexion.asignarAtributos("**")
            listaCliente = BLL_Cliente.Cliente().crearListaDB()
            fecha = BLL_Fecha.Fecha()
            fechaInicio = fecha.fechaInicio("mensual")
            fechaFin = fecha.fechaFin()
            for cliente in listaCliente:
                if cliente.nombre == "nombreTest22":

                    # sin el cliente, trae todos.
                    # "Exploits" "ThreatsOnly" "ClearedEvent" "Devices" "ThreatsUsuarios" "ClearedEventCount" "ThreatOnlyCount" "ExploitCount" "DeviceCount"
                    result = DAL_Mapper_Eventos.Mapper_Eventos().leerEventos(fechaInicio, fechaFin, "ExploitCount", cliente)
                    print(result)


    def test_obtenerColumnas(self):
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        # "exploits" "threats" "devices" "clientes" o "mailsasociados"
        #["exploits", "threats", "devices"]
        result = DAL_Mapper_Eventos.Mapper_Eventos().obtenerColumnas("exploits")
        print(result)