import os
import gc
from DAL import DAL_Mapper
from DAL import DAL_Conexion
from BLL import BLL_Log
from BLL import BLL_Fecha
import csv
import json
from pathlib import Path
import pandas as pd


class Mapper_Archivo(DAL_Mapper.Mapper):
    
    def __init__(self):
        conexion = DAL_Conexion.Conexion()
        self.conexion = conexion
        print("Se creo un objeto Mapper_Archivo")

    def mapperVerificarArchivo(self, ruta):
        if(os.path.exists(ruta)):
            return True
        else:
            return False

    
    def mapperGenerarDirectorios(self, directorio, fecha, nombreCliente):
    
        directorio = Path(directorio)
        directorio.mkdir(parents=True, exist_ok=True)
        directorio = directorio / str(fecha.year)
        directorio.mkdir(exist_ok=True)
        directorio = directorio / str(fecha.month)
        directorio.mkdir(exist_ok=True)
        directorio = directorio / nombreCliente
        directorio.mkdir(exist_ok=True)
        BLL_Log.Log().escribir("Se crearon los directorios de Informes", nombreCliente, "Informar")

        return str(directorio)
    
    def mapperExisteArchivo(self, ruta):
        if(os.path.exists(ruta)):
            os.remove(ruta)
            print("Archivo borrado con exito")
        else:
            print("El archivo no existe o no se encuentra en la ruta especificada")

    
    def mapperLeerCSV(self, ruta):

        listaHashes = []
        with open(ruta, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                listaHashes.append(row)

        return listaHashes


    def mapperCrearArchivoConexion(self, db, user, password, host, port):
        datos = {"database": db, "user": user, "password": password, "host": host, "port": port, "estado": 0}    

        with open(".//DATA//CONFIG//Conexion.json", 'w') as f:
            json.dump(datos, f, indent=4, separators=(',',': '))

    
    def mapperVerificarEstadoArchivo(self):
        with open(".//DATA//CONFIG//Conexion.json", 'r') as file:
            datos = json.load(file)
        if(datos["estado"] == 0):
            print("El archivo no estaba encriptado")
            return False
        else:
            print("El archivo ya estaba encriptado")
            return True
        
    def mapperCrearCSVConBaseDeDatos(self, df, cliente, periodo, rutaDirectorio, tipoDf):
        log = BLL_Log.Log()
        fecha = BLL_Fecha.Fecha()
        fechaFin = fecha.fechaFin()
        if periodo == "diario" or periodo == "semanal":
            nombreArchivo = str(fechaFin.year) + " - " + str(fechaFin.month) + " - " + str(fechaFin.day) + " - " + cliente.nombre + " - " + periodo + " - " + tipoDf + ".csv"
        else:
            nombreArchivo = str(fechaFin.year) + " - " + str(fechaFin.month) + " - " + cliente.nombre + " - " + periodo + " - " + tipoDf + ".csv"
        ruta = rutaDirectorio + nombreArchivo
        try:
            df.to_csv(ruta, index = False, header=True, encoding='utf-8-sig')
            print("Se creo el archivo " + nombreArchivo + " en la ruta " + rutaDirectorio)
            log.escribir("Se creo el archivo " + nombreArchivo + " en la ruta " + rutaDirectorio, cliente.nombre, "Informar")
            return ruta
        except:
            log.escribir("Error al crear el archivo " + nombreArchivo + " en la ruta " + rutaDirectorio, cliente.nombre, "Error")
        

    def __del__(self):
        gc.collect()




