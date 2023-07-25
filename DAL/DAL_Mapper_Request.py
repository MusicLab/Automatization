import regex as re
from DAL import DAL_Conexion
from DAL import DAL_Mapper
from DAL import DAL_Mapper_Archivo
from BLL import BLL_Archivo
from BLL import BLL_Log
import gc
import wget
import datetime
import os
import ftfy


class Mapper_Request(DAL_Mapper.Mapper):

    def __init__(self):
        conexion = DAL_Conexion.Conexion()
        self.conexion = conexion
        print("Se creo un objeto Mapper_Request")
    
    def mapperLecturaThreat(self, cliente, fecha, dataframe):
        ano = str((fecha.ahora() - datetime.timedelta(1)).year)
        mes = str((fecha.ahora() - datetime.timedelta(1)).month)

        nombreArchivoThreats = ano +  " - " + mes + " - "  + cliente.nombre + " - Threats.csv"
        nombreArchivoEvents = ano +  " - " + mes + " - "  + cliente.nombre + " - Events.csv"
        nombreArchivoCleared = ano +  " - " + mes + " - "  + cliente.nombre + " - Cleared.csv"
        mapperArchivo = DAL_Mapper_Archivo.Mapper_Archivo()
        mapperArchivo.mapperExisteArchivo(".//DATA//CSVS//THREATS//" + nombreArchivoThreats)
        mapperArchivo.mapperExisteArchivo(".//DATA//CSVS//THREATS//" + nombreArchivoEvents)
        mapperArchivo.mapperExisteArchivo(".//DATA//CSVS//THREATS//" + nombreArchivoCleared)

        if cliente.region == "NA":
            URLThreat = "https://protect.cylance.com/Reports/ThreatDataReportV1/threats/" + cliente.token           
            URLEvents = "https://protect.cylance.com/Reports/ThreatDataReportV1/events/" + cliente.token
            URLCleared = "https://protect.cylance.com/Reports/ThreatDataReportV1/cleared/" + cliente.token

        elif cliente.region == "SA":
            URLThreat = "https://protect-sae1.cylance.com/Reports/ThreatDataReportV1/threats/" + cliente.token
            URLEvents = "https://protect-sae1.cylance.com/Reports/ThreatDataReportV1/events/" + cliente.token
            URLCleared = "https://protect-sae1.cylance.com/Reports/ThreatDataReportV1/cleared/" + cliente.token

        wget.download(URLThreat, ".//DATA//CSVS//THREATS//" + nombreArchivoThreats)
        wget.download(URLEvents, ".//DATA//CSVS//THREATS//" + nombreArchivoEvents)
        wget.download(URLCleared, ".//DATA//CSVS//THREATS//" + nombreArchivoCleared)

        #dataframe.dataframeADB(self.conexion, "threat")
        log = BLL_Log.Log()
        log.escribir("CSV descargados", cliente.nombre, "Informar")

    def mapperLecturaThreatDB(self, cliente, fecha):
        con = DAL_Mapper.Mapper.conectarDB("**")
        cur = con.cursor()
        cur.execute("SELECT exploitsEntreFechas(%s, %s)",(fecha.fechaInicio("mensual"), fecha.fechaFin()))
        rows = cur.fetchall()
        return rows

    def mapperLecturaMemProt(self, cliente, fecha,  dataframe, tipo = "diario"):
        ano = str((fecha.ahora() - datetime.timedelta(1)).year)
        mes = str((fecha.ahora() - datetime.timedelta(1)).month)
        nombreArchivo = ano +  " - " + mes + " - "  + cliente.nombre + " - Memory Protection.csv"
        archivo = BLL_Archivo.Archivo(".//DATA//CSVS//", nombreArchivo)
        conexion = DAL_Conexion.Conexion() 
        API = conexion.conectar(cliente)

        i = 0
        header = "DeviceName,UserName,ViolationType,Action,FilePath,FileName,Created,ProcessID"

        if(os.path.exists(archivo.ruta + nombreArchivo) == False):
            archivo.escribirArchivo(header)
        
        memoryProtection = API.get_memory_protection_events(fecha.fechaInicio(tipo).isoformat(sep='T'), fecha.fechaFin().isoformat(sep='T'))
        for log in memoryProtection.data:
            device = API.get_device(str(log['device_id']))

            dName = str(device.data['name']).replace(",", "")
            dName = ftfy.fix_text(dName)

            userName = str(log['user_name']).replace(",", "")
            userName = ftfy.fix_text(userName)

            violationType = str(log['violation_type']).replace(",", "")
            violationType =  ftfy.fix_text(violationType)

            action = str(log['action']).replace(",", "")
            action = ftfy.fix_text(action)

            pID = str(log['process_id']).replace(",", "")
            pID = ftfy.fix_text(pID)

            created = str(log['created']).replace(",", "")
            created= ftfy.fix_text(created)

            fPath = str(log['image_name']).replace(",", "")
            fPath = ftfy.fix_text(fPath)

            fName = os.path.basename(log['image_name']).replace(",", "")
            fName = ftfy.fix_text(fName)

            fPath = os.path.dirname(log['image_name']).replace(",", "")
            fPath = ftfy.fix_text(fPath)
            
            i += 1

            campos = dName + "," + userName + "," + violationType + "," + action + "," + fPath + "," + fName + "," + created + "," + pID
            archivo.escribirArchivo(campos)
            #dataframe.dataframeADB(self.conexion, "exploit")

        log = BLL_Log.Log()
        log.escribir("Fecha Inicio: " + str(fecha.fechaInicio("diario").isoformat(sep='T')), cliente.nombre, "Informar")
        log.escribir("Logs encontrados Memory Protection: " + str(i), cliente.nombre, "Informar")
        

    def mapperLecturaDevice(self, cliente, fecha, dataframe):
        ano = str((fecha.ahora() - datetime.timedelta(1)).year)
        mes = str((fecha.ahora() - datetime.timedelta(1)).month)
        nombreArchivo = ano +  " - " + mes + " - "  + cliente.nombre + " - Devices.csv"
        archivo = BLL_Archivo.Archivo(".//DATA//CSVS//", nombreArchivo)
        conexion = DAL_Conexion.Conexion() 
        API = conexion.conectar(cliente)

        if(os.path.exists(archivo.ruta + nombreArchivo)):
            os.remove(archivo.ruta + nombreArchivo)

        i = 0

        header = "OperativeSystem,DeviceName,AgentVersion,Policy,IPs,DateOffline,ZoneName,LastLoggedInUser"
        if(os.path.exists(archivo.ruta + nombreArchivo) == False):
            archivo.escribirArchivo(header)
        
        dv = API.get_devices_extended()
        for device in dv.data:
            zonaDV = API.get_device_zones(device['id'])
            dv = API.get_device(device['id'])

            OS = str(device['os_version']).replace(",", "")
            OS = ftfy.fix_text(OS)

            dName = str(device['name']).replace(",", "")
            dName = ftfy.fix_text(dName)

            aVersion = str(device['agent_version']).replace(",", "")
            aVersion = ftfy.fix_text(aVersion)

            policy = str(device['policy']['name']).replace(",", "")
            policy = ftfy.fix_text(policy)

            try:
                IP = re.search('((\d+\.){3}\d+)', str(device['ip_addresses']))
                IP = str(IP.group(1)).replace(",", "")
                IP = ftfy.fix_text(IP)

            except:
                IP = ""
            dOffline = str(device['date_offline']).replace(",", "")
            dOffline = ftfy.fix_text(dOffline)

            try:
                listaZonas = []
                for z in zonaDV.data:
                    a = ftfy.fix_text(z["name"])
                    listaZonas.append(a)
                    
              
                zonas = str(listaZonas).replace(",", "{").replace("'", "").replace("[", "").replace("]", "")
                if len(zonas) < 1:
                    zonas = "Default"

            except Exception as e:
                print("error Devices")
                log = BLL_Log.Log()
                log.escribir("Error: en Zonas" + str(e), cliente.nombre, "error")

            LLIU = str(dv.data['last_logged_in_user']).replace(",", "")
            LLIU = ftfy.fix_text(LLIU)

            i += 1
            campos = OS + "," + dName + "," + aVersion + "," + policy + "," + str(IP) + "," + dOffline + "," + zonas + "," + LLIU
            archivo.escribirArchivo(campos)
            #dataframe.dataframeADB(self.conexion, "device")

        log = BLL_Log.Log()
        log.escribir("Logs encontrados Devices: " + str(i), cliente.nombre, "Informar")


    def __del__(self):
        gc.collect()


