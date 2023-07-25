from DAL import DAL_Mapper_Request
from DAL import DAL_Mapper_Eventos
from BLL import BLL_Log
from BLL import BLL_Dataframe
from BLL import BLL_Archivo
import requests
import gc


class Request(object):
    
    def __init__(self):
        pass

    def ejecutarMapperLectura(self, fecha, semanal, mensual, cliente):

        fechaInicio = fecha.fechaInicio("diario")
        fechaFin = fecha.fechaFin()
        archivo = BLL_Archivo.Archivo(".//DATA//CSVS//")
        mapper = DAL_Mapper_Request.Mapper_Request()

        dataframe = BLL_Dataframe.Dataframe(cliente, fechaInicio, fechaFin, archivo)

        try:
            mapper.mapperLecturaMemProt(cliente, fecha, dataframe)
            dataframe.crearDataframe(archivo.ruta, "exploit")
            dataframe.dataframeADB("exploit")
            BLL_Log.Log().escribir("Se realizo la request de Memory Protection", cliente.nombre, "Informar")
        except Exception as e:
            BLL_Log.Log().escribir("Hubo un problema con la request de Memory Protection: " + str(e), cliente.nombre, "Error")

        # request completas diarias
        #if(cliente.periodicidad == "0") or (semanal == True and cliente.periodicidad == "1") or (mensual == True):
        try:
            mapper.mapperLecturaDevice(cliente, fecha, dataframe)
            BLL_Log.Log().escribir("Se realizo la request de Devices", cliente.nombre, "Informar")
        except Exception as e:
            BLL_Log.Log().escribir("Hubo un problema con la request de Devices: " + str(e), cliente.nombre, "Error")
        dataframe.crearDataframe(archivo.ruta, "device")
        dataframe.dataframeADB("device")

        try:
            mapper.mapperLecturaThreat(cliente, fecha, dataframe)
            BLL_Log.Log().escribir("Se realizo la request de Threats", cliente.nombre, "Informar")
        except Exception as e:
            BLL_Log.Log().escribir("Hubo un problema con la request de Threats: " + str(e), cliente.nombre, "Error")

        try:
            
            dataframe.unificarCsvThreat(archivo.ruta)
            dataframe.crearDataframe(archivo.ruta, "threat")
            dataframe.dataframeADB("threat")
            BLL_Log.Log().escribir("Se realizo la escritura de Threats en la BD", cliente.nombre, "Informar")
        except Exception as e:
            BLL_Log.Log().escribir("Hubo un problema con la escritura de threats en la BD: " + str(e), cliente.nombre, "Error")

        try:
            ran = cliente.leerClienteEspecifico("Ran")
            datos = self.requestZoho(ran, 'accounts')
            matches = self.matchearClientesZoho(datos, cliente)
            for clienteMatcheado in matches:
                if clienteMatcheado['nombre'] == cliente.nombre:
                    #self.insertarDatosZoho(cliente, clienteMatcheado['id'])
                    cliente.modificarDB(cliente.nombre, cliente.region, cliente.token, cliente.tid, cliente.aid, cliente.sid, cliente.logo, cliente.periodicidad, clienteMatcheado['licencias'])
        except:
            log = BLL_Log.Log()
            log.escribir("Hubo un problema con la insercion de las licencias en la Base de Datos", cliente.nombre, "Error")


    def requestZoho(self, cliente, api_endpoint, params=None):
        mapper = DAL_Mapper_Eventos.Mapper_Eventos()
        mapper.conexion.conectarDB()
        datosZoho = mapper.leerEventos(cliente, "TokensZoho")
        access_token = mapper.conexion.getAccessToken(datosZoho)
        return mapper.mapperRequestZoho(api_endpoint, access_token)
    
    def matchearClientesZoho(self, response, cliente):
        mapper = DAL_Mapper_Eventos.Mapper_Eventos()
        return mapper.mapperMatchearClientes(response, cliente)
    
    def insertarDatosZoho(self, cliente, id_cliente, refresh_token = None, sid = None):
        mapper = DAL_Mapper_Eventos.Mapper_Eventos()
        mapper.mapperInsertarDatosZoho(cliente, id_cliente, refresh_token, sid)


    def __del__(self):
        gc.collect()
