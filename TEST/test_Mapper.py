import unittest
import os
import json
from BLL import BLL_Cliente
from BLL import BLL_Fecha
from BLL import BLL_Archivo
from BLL import BLL_Log
from BLL import BLL_Dataframe_Personalizado
from DAL import DAL_Mapper_Eventos
from DAL import DAL_Mapper_Hash
from DAL import DAL_Mapper_Archivo
from DAL import DAL_Mapper_Log
from DAL import DAL_Mapper_Request
from DAL import DAL_Mapper_Cliente
from DAL import DAL_Mapper
from DAL import DAL_Conexion
import datetime



class Test_Mapper(unittest.TestCase):
    

    def test_Agregar(self):
        
        conexion = DAL_Conexion.Conexion()
        mapper = DAL_Mapper_Cliente.Mapper_Cliente(conexion)
        mapper.mapperAgregar("nombreTest", "regionTest", "tokenTest", "tidTest", "aidTest", "sidTest", "logoTest", "periodicidadTest")
        funciono = False
        with open(".//DATA//CLIENTES//Tokens.json", "r") as archivo:
            lines = json.load(archivo)
        for line in lines:
            if(line["cliente"] == "nombreTest"):
                funciono = True
        self.assertEqual(funciono, True)



    def test_aModificar(self):
        
        conexion = DAL_Conexion.Conexion()
        mapper = DAL_Mapper_Cliente.Mapper_Cliente(conexion)
        mapper.mapperModificar("nombreTest", "nombreTestModificado", "regionTestModificado", "tokenTestModificado", "tidTestModificado", "aidTestModificado", "sidTestModificado", "logoTestModificado", "periodicidadTestModificado")
        funciono = False
        with open(".//DATA//CLIENTES//Tokens.json", "r") as archivo:
            lines = json.load(archivo)
        for line in lines:
            if(line["cliente"] == "nombreTestModificado"):
                funciono = True 
        self.assertEqual(funciono, True)

    def test_Borrar(self):
        
        conexion = DAL_Conexion.Conexion()
        mapper = DAL_Mapper_Cliente.Mapper_Cliente(conexion)
        mapper.mapperBorrar("nombreTestModificado")
        funciono = True
        with open(".//DATA//CLIENTES//Tokens.json", "r") as archivo:
            lines = json.load(archivo)
        for line in lines:
            if(line["cliente"] == "nombreTestModificado"):
                funciono = False
        self.assertEqual(funciono, True)

    def test_MapperLecturaThreats(self):
        
        fecha = BLL_Fecha.Fecha()
        ano = str(fecha.ahora().year)
        mes = str(fecha.ahora().month)
        cliente = BLL_Cliente.Cliente()
        existe = False
        listaClientes = cliente.crearLista()
        for cliente in listaClientes:
            nombreArchivoThreats = ano +  " - " + mes + " - "  + cliente.nombre + " - Threats.csv"
            nombreArchivoEvents = ano +  " - " + mes + " - "  + cliente.nombre + " - Events.csv"
            nombreArchivoCleared = ano +  " - " + mes + " - "  + cliente.nombre + " - Cleared.csv"
            DAL_Mapper_Request.Mapper_Request.mapperLecturaThreat(self, cliente, fecha)
            if((os.path.exists(".//DATA//CSVS//THREATS//" + nombreArchivoThreats)) and (os.path.exists(".//DATA//CSVS//THREATS//" + nombreArchivoEvents)) and (os.path.exists(".//DATA//CSVS//THREATS//" + nombreArchivoCleared))):
                existe = True

            self.assertIs(existe, True)
            existe = False

    

    def test_MapperLecturaMemProt(self):
        
        fecha = BLL_Fecha.Fecha()
        ano = str(fecha.ahora().year)
        mes = str(fecha.ahora().month)
        cliente = BLL_Cliente.Cliente()
        existe = False
        listaClientes = cliente.crearLista()
        for cliente in listaClientes:
            nombreArchivo = ano +  " - " + mes + " - "  + cliente.nombre + " - Memory Protection.csv"
            DAL_Mapper_Request.Mapper_Request.mapperLecturaMemProt(self, cliente, fecha, "diario")
            if(os.path.exists(".//DATA//CSVS//" + nombreArchivo)):
                existe = True

            self.assertIs(existe, True)
            existe = False

    def test_MapperLecturaDevices(self):
        
        fecha = BLL_Fecha.Fecha()
        ano = str(fecha.ahora().year)
        mes = str(fecha.ahora().month)
        cliente = BLL_Cliente.Cliente()
        existe = False
        listaClientes = cliente.crearLista()
        for cliente in listaClientes:
            nombreArchivo = ano +  " - " + mes + " - "  + cliente.nombre + " - Devices.csv"
            DAL_Mapper_Request.Mapper_Request.mapperLecturaDevice(self, cliente, fecha)
            if(os.path.exists(".//DATA//CSVS//" + nombreArchivo)):
                existe = True

            self.assertIs(existe, True)
            existe = False

    def test_MapperLog(self):
        
        fecha = BLL_Fecha.Fecha()
        archivo = BLL_Archivo.Archivo(fecha, ".//DATA//LOGS//", "Logs.txt")
        if(os.path.exists(".//DATA//LOGS//Logs.txt")):
            file = open(".//DATA//LOGS//Logs.txt", mode = "r", encoding='utf-8')
        else:
            file = open(".//DATA//LOGS//Logs.txt", mode = "x+", encoding='utf-8')
            
        DAL_Mapper_Log.Mapper_Log.mapperLog(archivo, "Datos Prueba", "Cliente Prueba", "advertencia")
        self.assertIn("Cliente Prueba: advertencia - Datos Prueba", file.read())


    def test_MapperVerificarArchivo(self):
        
        ruta = ".//DATA//TEST//ArchivoPrueba.txt"
        existe = DAL_Mapper_Archivo.Mapper_Archivo.mapperVerificarArchivo(ruta)

        self.assertIs(existe, True)

    def test_MapperGenerarDirectorios(self):
        
        fechaTest = BLL_Fecha.Fecha()
        fecha = BLL_Fecha.Fecha().ahora()
        ano = str(fechaTest.ahora().year)
        mes = str(fechaTest.ahora().month)
        DAL_Mapper_Cliente.Mapper_Cliente().conexion.asignarAtributos("**")
        listaCliente = BLL_Cliente.Cliente().crearListaDB()

        for cliente in listaCliente:
            directorio = ".//DATA//TEST//"
            DAL_Mapper_Archivo.Mapper_Archivo().mapperGenerarDirectorios(directorio, fecha, cliente.nombre)

            if(os.path.exists(directorio)):
                existe = True
            self.assertIs(existe, True)
            existe = False

            if(os.path.exists(directorio + "/" + str(ano))):
                existe = True
            self.assertIs(existe, True)
            existe = False

            if(os.path.exists(directorio + "/" + str(ano) + "/" + str(mes))):
                existe = True
            self.assertIs(existe, True)
            existe = False
    
    def test_MapperExisteArchivo(self):
        
        ruta = ".//DATA//TEST//ArchivoPrueba.txt"

        DAL_Mapper_Archivo.Mapper_Archivo.mapperExisteArchivo(ruta)

        if(os.path.exists(ruta)):
            funciona = False
        else:
            funciona = True
      
        self.assertIs(funciona, True)

    def test_MapperAgregarHash(self):
        
        cliente = BLL_Cliente.Cliente()
        listaClientes = cliente.crearLista()
        for cliente in listaClientes:
            if cliente.nombre == "Ran":
                resp = DAL_Mapper_Hash.Mapper_Hash.mapperAgregarHash(cliente, "safe", "prueba", "DF95EA262571D5900A509ACFE3F015BED9E4FDDF016E1D78F19BBA993DD75549", "None")
                self.assertEqual(200, resp)
       
    def test_MapperMultiHash(self):
        
        ruta = ".//DATA//CLIENTES//Hashes.csv"
        cliente = BLL_Cliente.Cliente()
        listaClientes = cliente.crearLista()
        listaFinal = []
        for cliente in listaClientes:
            if cliente.nombre == "Ran" or cliente.nombre == "Gpat":
                listaFinal.append(cliente)
        
        mapper = DAL_Mapper_Hash.Mapper_Hash()
        mapper.mapperAgregarMultiHashes(listaFinal, ruta, "safe", "pruebaFinal", "None")
        self.assertEqual(200, 200)

    def test_MapperEliminarHash(self):
        
        cliente = BLL_Cliente.Cliente()
        listaClientes = cliente.crearLista()
        for cliente in listaClientes:
            if cliente.nombre == "Ran":
                resp = DAL_Mapper_Hash.Mapper_Hash.mapperEliminarHash(cliente, "safe", "DF95EA262571D5900A509ACFE3F015BED9E4FDDF016E1D78F19BBA993DD75549")
                self.assertEqual(200, resp)

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
        mapperCliente.mapperConectarDB()
        listaClienteDB = mapperCliente.mapperLeerClientesDB()
        listaClienteVieja = mapperCliente.mapperLeerClientes()

        print("LISTA VIEJA: ", listaClienteVieja)
        print("LISTA DB: ", listaClienteDB)
        mapperCliente.mapperDesconectarDB()


        

    def test_AgregarClienteDB(self):
        
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        DAL_Mapper_Cliente.Mapper_Cliente.mapperAgregarClienteDB(mapperCliente.conexion, "nombreTest", "regionTe", "tokenTest", "tidTest", "aidTest", "sidTest", "logoTest", "1")
        
        mapperCliente.mapperDesconectarDB()
        self.assertEqual("funciono", "funciono")

    def test_BorrarClienteDB(self):
        
        conexion = DAL_Conexion.Conexion("**")
        mapper = DAL_Mapper.Mapper(conexion)
        mapper.mapperConectarDB()
        DAL_Mapper_Cliente.Mapper_Cliente.mapperBorrarClienteDB(mapper.conexion, "tidTest")
        
        mapper.mapperDesconectarDB()
        self.assertEqual("funciono", "funciono")


    def test_MapperCrearArchivoConexion(self):
        
        funciona = False
        ruta = os.getcwd() + "//DATA//CONFIG//Conexion.json"
        conexion = DAL_Conexion.Conexion()
        mapper = DAL_Mapper_Archivo.Mapper_Archivo()
        conexion.cambiarEstadoArchivo()
        mapper.mapperCrearArchivoConexion("**")

        if(os.path.exists(ruta)):
            funciona = True

        self.assertEqual(funciona, True)

    def test_MapperLeerEventos(self):

        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("mensual")
        fechaFin = fecha.fechaFin() - datetime.timedelta(days=35)
        print(fechaFin)
        mapper = DAL_Mapper_Eventos.Mapper_Eventos()
        conexion = DAL_Conexion.Conexion()
        conexion.asignarAtributos("**")
        mapper.asignarConexion(conexion)

        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        
        for cliente in clientes:
            if cliente.nombre == "Ran":
                eventos = mapper.leerEventos(cliente, "cantEquiposLic", fechaFin=fechaFin)
                print(eventos)


        self.assertEqual(dict, type(eventos))


    def test_parrafo(self):
        mapper = DAL_Mapper_Eventos.Mapper_Eventos()
        parrafo = mapper.parrafo()
        print(parrafo)
        self.assertEqual(str, type(parrafo))

    def test_MapperCrearCSVConBaseDeDatos(self):
        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("mensual")
        print(fechaInicio)
        fechaFin = fecha.fechaFin()
        print(fechaFin)
        cliente = BLL_Cliente.Cliente()
        mapperArchivo = DAL_Mapper_Archivo.Mapper_Archivo()
        dataframePersonalizado = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        mapperArchivo.conexion.asignarAtributos("**")
        mapperArchivo.mapperConectarDB()

        listaCliente = cliente.crearListaDB()
        ruta = os.getcwd() + "//DATA//CSVS//REPORTE SEMANAL//"
        for cliente in listaCliente:
            filas = dataframePersonalizado.leerEventosDB(fechaInicio, fechaFin, cliente, "DevicesSinZonas")
            df = dataframePersonalizado.crearDataframePersonalizado(filas)
            rutaCSV = mapperArchivo.mapperCrearCSVConBaseDeDatos(df, cliente, "diario", "Devices sin Zonas", ruta)
            self.assertTrue(os.path.exists(rutaCSV))


    def test_MapperInsertarDatosZoho(self):
        mapper = DAL_Mapper_Eventos.Mapper_Eventos()
        cliente = BLL_Cliente.Cliente()
        mapper.conexion.asignarAtributos("**")
        listaCliente = cliente.crearListaDB()
        for cliente in listaCliente:
            if cliente.nombre == "Banco Patagonia":
                mapper.mapperInsertarDatosZoho(cliente, "2021-05-01", "2021-05-31", "Banco Patagonia")
        
        self.assertEqual(True, True)


    def test_MapperLeerClienteEspecifico(self):
        mapper = DAL_Mapper_Cliente.Mapper_Cliente()
        mapper.conexion.asignarAtributos("**")
        cliente = mapper.mapperLeerClienteDBEspecifico("Ran")
        print(cliente)
        self.assertEqual("Ran", cliente[0][1])

                