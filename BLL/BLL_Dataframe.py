import os
import csv
import dateutil.parser as parser
import copy
import pandas as pd
from BE import BE_Dataframe
from DAL import DAL_Mapper_Eventos
import gc
from BLL import BLL_Log


# comando para que no salten alertas por uso de funciones desatendidas de pandas
pd.options.mode.chained_assignment = None  # default='warn'

class Dataframe(object):
    def __init__(self, cliente, fechaInicio, fechaFin, archivo):
        BE_Dataframe.Dataframe.setCliente(self, cliente)
        BE_Dataframe.Dataframe.setFechaInicio(self, fechaInicio)
        BE_Dataframe.Dataframe.setFechaFin(self, fechaFin)
        BE_Dataframe.Dataframe.setArchivo(self, archivo)
        BE_Dataframe.Dataframe.setDiccCSV(self, diccCSV = {
            "cliente" : "",
            "threat" : "",
            "exploit" : "",
            "device" : "",
            "clearedEvent" : "",
            "threatSolo" : ""
            })

            
        
    def unificarCsvThreat(self, ruta):
        try:   
        
            rutaRaw = ruta + "THREATS//"
        
            nombreArchivo = str(self.fechaFin.year) + " - " + str(self.fechaFin.month) + " - " + self.cliente.nombre
            
            files = [file for file in os.listdir(rutaRaw)]
            listaFilas = []
            for file in files:
                if nombreArchivo in file and "Events" in file:
                    with open (rutaRaw + file, encoding="utf-8-sig") as fileOpen:
                        filas = csv.reader(fileOpen)
                        next(filas)                
                        for fila in filas:
                            fila[3] = parser.parse(fila[3])
                            if self.fechaInicio < fila[3] < self.fechaFin:
                                listaFilas.append(self.parsearEventos(fila, "Events"))

                if nombreArchivo in file and "Cleared" in file:
                    with open (rutaRaw + file, encoding="utf-8-sig") as fileOpen:
                        filas = csv.reader(fileOpen)
                        next(filas)                
                        for fila in filas:
                            fila[3] = parser.parse(fila[3])
                            if self.fechaInicio < fila[3] < self.fechaFin:
                                listaFilas.append(self.parsearEventos(fila, "Cleared"))

                if nombreArchivo in file and "Threats" in file:
                    with open (rutaRaw + file, encoding="utf-8-sig") as fileOpen:
                        filas = csv.reader(fileOpen)
                        next(filas)                
                        for fila in filas:
                            fila = self.parsearEventos(fila, "Threats")
                            fila[9] = parser.parse(fila[9])
                            if self.fechaInicio < fila[9] < self.fechaFin:
                                listaFilas.append(fila)

            with open(ruta + nombreArchivo + " - Threats.csv", "w", newline='', encoding="utf-8-sig") as file3:
                writer = csv.writer(file3)
                writer.writerows(listaFilas)
                
                
        except Exception as e:
            
            BLL_Log.Log().escribir("Error en unificarCsvThreat: " + str(e), self.cliente.nombre, "error")
                    
                            
    
            

    def crearDataframe(self, ruta, tipo = None):
        try:
        
            nombreArchivo = str(self.fechaFin.year) + " - " + str(self.fechaFin.month) + " - " + self.cliente.nombre
            files = [file for file in os.listdir(ruta)]
            for file in files:
                # ------------------------ EXPLOITS -----------------------
                if nombreArchivo in file and "Memory Protection" in file and (tipo == None or tipo == "exploit"):
                    
                    print("paso por exploit")
                    exploit = pd.read_csv(ruta + file, encoding='utf-8', header =0)
                    self.diccCSV["exploit"] = exploit
                    

                    self.diccCSV["exploit"]["Action"] = self.diccCSV["exploit"]["Action"].map({
                        0: "Alert",
                        2: "Block",
                        3: "Terminate",
                        })
                    # Reemplazamos los valores numericos por las descripciones correspondientes.
                    # TODO aviso de nuevas unclassified
                    self.diccCSV["exploit"]["ViolationType"] = self.diccCSV["exploit"]["ViolationType"].map({
                        1: "Stack pivot",
                        2: "Stack protect",
                        3: "Overwrite code",
                        4: "Remote allocation of memory",
                        5: "Remote mapping of memory",
                        6: "Remote write to memory",
                        7: "Remote write PE to memory",
                        8: "Remote overwrite code",
                        9: "Remote unmap of memory",
                        10: "Remote thread creation",
                        11: "Remote APC scheduled",
                        12: "LSASS read",
                        13: "RAM scraping",
                        22: "Zero allocate",
                        23: "DYLD injection",
                        24: "Malicous payload",
                        # agregados
                        27: "Memory Permission changes in Other processes",
                        28: "Memory Permission Changes in Child Processes",
                        31: "Direct System Calls",
                        32: "System DLL Overwrite",
                        38: "Injection via APC",
                        })
                    self.diccCSV["exploit"]["ViolationType"].fillna("Unclassified", inplace = True)
                
                    self.diccCSV["exploit"]["Created"] = self.diccCSV["exploit"]["Created"].map(lambda x:parser.parse(x))
                    self.diccCSV["exploit"] = self.diccCSV["exploit"].loc[(self.diccCSV["exploit"]['Created'] > self.fechaInicio) & (self.diccCSV["exploit"]['Created'] < self.fechaFin)]

                    self.diccCSV["exploit"].to_csv(ruta + nombreArchivo + " - Exploits.csv", index = False, header=True)
                    dfExploitADB = self.diccCSV["exploit"].copy()
                    dfExploitADB["Created"] = pd.to_datetime(dfExploitADB["Created"], unit='ms').apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
            
                    
                        

                    


                # ------------------------ DEVICES -----------------------
                if nombreArchivo in file and "Devices" in file and (tipo == None or tipo == "device"):
                    print("paso por device")
                    device = pd.read_csv(ruta + file, encoding='utf-8', index_col=False)

                    device["ZoneName"] = [x.split("{") for x in device["ZoneName"]]              
                    device["DateOffline"] = device["DateOffline"].replace("None", "Online")
                    device['LastLoggedInUser'] = device['LastLoggedInUser'].str.lower()
                    device = device.drop_duplicates('DeviceName')
                    self.diccCSV["device"] = device

                # ------------------------ THREATS -----------------------

                if nombreArchivo in file and "Threats" in file and (tipo == None or tipo == "threat"):
                    print("paso por threat")
                    threat = pd.read_csv(ruta + file, encoding='utf-8', names = ["SHA256", "FileStatus", "DeviceName", "FilePath", "FileName", "Classification", "SubClass", "FileOwner", "DriveType", "DateFound", "OrigenDeDato"], on_bad_lines='skip')
                    self.diccCSV["threat"] = threat
                    self.diccCSV["threat"].to_csv(ruta + nombreArchivo + " - Threats.csv", index = "false")    
                    cleared = self.diccCSV["threat"][ self.diccCSV["threat"]["OrigenDeDato"] == "Cleared" ]
                    event = self.diccCSV["threat"][ self.diccCSV["threat"]["OrigenDeDato"] == "Event" ]
                    threat = self.diccCSV["threat"][ self.diccCSV["threat"]["OrigenDeDato"] == "Threat" ]
                    self.diccCSV["threatSolo"] = threat
                    self.diccCSV["clearedEvent"] = pd.concat([cleared, event])
                    
                    #threats = self.diccCSV["clearedEvent"]
                    #devices = self.diccCSV["device"]
                    # Rellena usuarios con el ultimo logueado en devices especificado por el SOC
                    merged = pd.merge(self.diccCSV["clearedEvent"], self.diccCSV["device"][["DeviceName", "LastLoggedInUser"]], on="DeviceName", how="left")
                    merged["FileOwner"] = merged["LastLoggedInUser"].fillna("None")
                    self.diccCSV["clearedEvent"] = merged
        except Exception as e:
            print(e)
                


    def parsearEventos(self, fila, tipo):
        if tipo == "Events":
            try:
                nuevaFila = []
                nuevaFila.append(fila[0])
                if fila[5] == None:
                    nuevaFila.append("En blanco")
                else:
                    nuevaFila.append(fila[5])
                nuevaFila.append(fila[2])
                # 2 filepath 
                nuevaFila.append(os.path.dirname(fila[4]))
                # 3 filename 
                nuevaFila.append(os.path.basename(fila[4]))
                # 4 classification
                copiaClass = copy.copy(fila[7])
                if fila[7] == "":
                    fila[7] = ("(en blanco)")
                nuevaFila.append(fila[7])
                # proceso subclass
                splitClass = copiaClass.split(" - ")
                # 5 subclass
                if len(splitClass) > 1:
                    nuevaFila.append(splitClass[1])
                else: nuevaFila.append("(en blanco)")

                nuevaFila.append("")
                nuevaFila.append("")
                nuevaFila.append(fila[3])
                nuevaFila.append("Event")
                return nuevaFila
            except Exception as e:
                BLL_Log.Log().escribir("Error en parsearEventos: " + str(e), self.cliente.nombre, "error")
                        
        if tipo == "Cleared":
            try:
                nuevaFila = []
                nuevaFila.append(fila[0])
                nuevaFila.append("Cleared")
                nuevaFila.append(fila[2])
                # 2 filepath 
                nuevaFila.append(os.path.dirname(fila[4]))
                # 3 filename 
                nuevaFila.append(os.path.basename(fila[4]))
                # 4 classification
                copiaClass = copy.copy(fila[6])
                if copiaClass == "":

                    nuevaFila.append("(en blanco)")
                    nuevaFila.append("(en blanco)")
                else:
                    nuevaFila.append(fila[6])
                    splitClass = copiaClass.split(" - ")
                    if type(splitClass) == list:
                        nuevaFila.append(splitClass[1])
                        
                    else: 
                        nuevaFila.append[1]


                nuevaFila.append("")
                nuevaFila.append("")
                nuevaFila.append(fila[3])
                nuevaFila.append("Cleared")

                return nuevaFila
            except Exception as e:
                print(e)
                pass


        if tipo == "Threats":
            try: 
                nuevaFila = []
                nuevaFila.append(fila[17])
                nuevaFila.append(fila[1])
                nuevaFila.append(fila[20])          
                # 2 filepath 
                nuevaFila.append(os.path.dirname(fila[23]))
                # 3 filename 
                nuevaFila.append(os.path.basename(fila[23]))
                # 4 classification
                copiaClass = copy.copy(fila[19])
                if fila[19] == "":
                    fila[19] = ("(en blanco)")
                nuevaFila.append(fila[19])
                # proceso subclass
                splitClass = copiaClass.split(" - ")
                # 5 subclass
                if len(splitClass) > 1:
                    nuevaFila.append(splitClass[1])
                else: nuevaFila.append("(en blanco)")
                nuevaFila.append(fila[25])
                nuevaFila.append(fila[24])
                
                #seleccionamos una columna inservible (16) para poner la fecha correcta segun especificaciones del SOC
                if fila[1] == "quarantined" or "abnormal":
                    fila[16] = fila[32] 
                elif fila[1] == "waived":
                    fila[16] = fila[33]
                else:
                    fila[16] == [32]

                nuevaFila.append(fila[16])
                nuevaFila.append("Threat")
                return nuevaFila
            except Exception as e:
                print(e)
                pass
    
    def dataframeADB(self,tipo, periodicidad = None):
        mapperEventos = DAL_Mapper_Eventos.Mapper_Eventos()
        try:
            if tipo == "exploit":
                df = self.diccCSV["exploit"].copy()
                df["Created"] = pd.to_datetime(df["Created"], unit='ms').apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
                mapperEventos.escribirEventos(self.cliente, df, tipo)
                BLL_Log.Log().escribir("Se ha escrito bien la BD con el dataframe exploits", self.cliente.nombre, "informar")
            if tipo == "threat":
                mapperEventos.escribirEventos(self.cliente, self.diccCSV["threat"], tipo)
                BLL_Log.Log().escribir("Se ha escrito bien la BD con el dataframe threats", self.cliente.nombre, "informar")
            if tipo == "device":
                mapperEventos.escribirEventos(self.cliente, self.diccCSV["device"], tipo)
                BLL_Log.Log().escribir("Se ha escrito bien la BD con el dataframe devices", self.cliente.nombre, "informar")
        except Exception as e:
            BLL_Log.Log().escribir("Error en dataframeADB: " + str(e), self.cliente.nombre, "error")


    def __del__(self):
        gc.collect()
