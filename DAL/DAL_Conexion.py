import json
import psycopg2
from UTILITIES import Singleton   
from BE import BE_Conexion
from BLL import BLL_Log
from BLL import BLL_Encripcion
from cyapi.cyapi import CyAPI
import gc
import requests


class Conexion(metaclass=Singleton.Singleton):


    def __init__(self, database = "", user = "", password = "", host = "", port = ""):
        BE_Conexion.Conexion.setEncripcion(self, BLL_Encripcion.Encripcion())
        self.encripcion.asignarAtributos(database, user, password, host, port)
        BE_Conexion.Conexion.setConexionDB(self, "")
        BE_Conexion.Conexion.setDatabase(self, database)
        BE_Conexion.Conexion.setUser(self, user)
        BE_Conexion.Conexion.setPassword(self, password)
        BE_Conexion.Conexion.setHost(self, host)
        BE_Conexion.Conexion.setPort(self, port)

    def asignarAtributos(self, db, user, password, host, port):
        self.database = db
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.encripcion.asignarAtributos(db, user, password, host, port)
        
    def conectar(self, cliente):

        API = CyAPI(cliente.tid, cliente.aid, cliente.sid, cliente.region)
        API.create_conn()
        if(API.s != None):
            BLL_Log.Log().escribir("Se creo la conexion", cliente.nombre, "informar")
            return API
        else:
            BLL_Log.Log().escribir("Error en  la conexion", cliente.nombre, "error")
            self.conectar(cliente)


    def conectarDB(self):
        try:

            #if(self.encripcion.estado == True):
            #    self.encripcion.desencriptarDatosConexion()
            #    print("desencripte")
                
            con = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host, 
            port= self.port)
            self.conexionDB = con
            print("Se realizo la conexion con exito")
            BLL_Log.Log().escribir("La conexion a la Base de Datos se realizo con exito", "General", "Informar")

            #self.encripcion.encriptarDatosConexion()
            
        except Exception as e:

            BLL_Log.Log().escribir("Hubo un problema con la conexion a la Base de Datos: " + str(e), "General", "Error")
            print("Hubo un problema con la conexion: " + str(e))

    def desconectar():
        Conexion.conexion = False

    def desconectarDB(self):
        self.conexionDB.close()

    def encriptarConexion(self):
        self.encripcion.encriptarDatosConexion()
        
    def desencriptarConexion(self):
        self.encripcion.desencriptarDatosConexion()

    def cambiarEstadoArchivo(self):
        self.encripcion.estadoArchivo = False

    def encriptarArchivo(self):
        self.encripcion.encriptarDatosArchivo()

    def leerArchivo(self):
        #self.encripcion.desencriptarDatosArchivo()
        with open (".//DATA//CONFIG//Conexion.json", "r", encoding='utf-8') as file:
            lista = json.load(file)
        print(lista)
        self.asignarAtributos(lista["database"], lista["user"], lista["password"], lista["host"], lista["port"])
        #self.encriptarArchivo()

    def getAccessToken(self, datosZoho):
        url = 'https://accounts.zoho.com/oauth/v2/token'
        payload = {
            'client_id': datosZoho['rows'][0][3],
            'client_secret': datosZoho['rows'][0][2],
            'refresh_token': datosZoho['rows'][0][1],
            'grant_type': 'refresh_token'
        }
        response = requests.post(url, data=payload)
        access_token = response.json()['access_token']
        return access_token

    def __del__(self):
        gc.collect()
        



