from BE import BE_Archivo 
import gc
from BLL import BLL_Fecha
from DAL import DAL_Mapper_Archivo
from BLL import BLL_Log
import pandas as pd

class Archivo(object):
    def __init__(self, ruta = "", nombre = ""):
        BE_Archivo.Archivo.setRuta(self, ruta)
        BE_Archivo.Archivo.setFecha(self, BLL_Fecha.Fecha())
        BE_Archivo.Archivo.setNombre(self, nombre)

    def escribirArchivo(self, campos):
        nombreArchivoCompleto = BE_Archivo.Archivo.getRuta(self) + BE_Archivo.Archivo.getNombre(self)
        file = open(nombreArchivoCompleto, mode = "a+", encoding='utf-8')    

        file.write(campos + "\n")
        file.close()

    def escribirLogTXT(self, datos, nombreCliente):
        nombreArchivo = ".//DATA//LOGS//Logs.txt"
        file = open(nombreArchivo, mode = "a+", encoding='utf-8')
        file.write(str(self.fecha.ahora()) + " - " + nombreCliente + ": " + str(datos) + "\n")
        file.close()

    def verificarArchivo(self, ruta):
        mapper = DAL_Mapper_Archivo.Mapper_Archivo()
        return mapper.mapperVerificarArchivo(ruta)

    def generarDirectorios(self, directorio, fecha, nombreCliente):
        mapper = DAL_Mapper_Archivo.Mapper_Archivo()
        return mapper.mapperGenerarDirectorios(directorio, fecha, nombreCliente)

    def existeArchivo(self, ruta):
        mapper = DAL_Mapper_Archivo.Mapper_Archivo()
        mapper.mapperExisteArchivo(ruta)

    def leerCSV(self, ruta):
        mapper = DAL_Mapper_Archivo.Mapper_Archivo()
        return mapper.mapperLeerCSV(ruta)
    
    def crearArchivoConexion(db, user, password, host, port):
        mapper = DAL_Mapper_Archivo.Mapper_Archivo()
        mapper.mapperCrearArchivoConexion(db, user, password, host, port)

    def verificarEstadoArchivo(self):
        mapper = DAL_Mapper_Archivo.Mapper_Archivo()
        return mapper.mapperVerificarEstadoArchivo()

    # def creacionCSV(self, df, ruta):
    #     try:
    #         df.to_csv(ruta + ".csv", index=False)
    #         #BLL_Log.Log().escribir("Se creo el CSV en la ruta: " + ruta, "informar")
    #     except Exception as e:
    #         #BLL_Log.Log().escribir("Error en CreacionCSV: " + ruta, "error")
    #         print(e)
    def creacionCSV(self, df, cliente, tipoPeriodo, rutaDirectorio, tipoDf):
        mapper = DAL_Mapper_Archivo.Mapper_Archivo()
        return mapper.mapperCrearCSVConBaseDeDatos(df, cliente, tipoPeriodo, rutaDirectorio, tipoDf)


    def __del__(self):
        gc.collect()

