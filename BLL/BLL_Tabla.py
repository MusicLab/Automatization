import numpy as np
import operator
from BLL import BLL_Fecha
import pandas as pd
import regex as re
from types import NoneType
import gc


class Tabla(object):
    def __init__(self):
        pass

    def procesarTabla(self, df, columna):
        dfProcesado = df.copy()
        lista = dfProcesado[columna].value_counts()
        lista = zip(lista, lista.index)
        return lista
    
    def procesarTablaGraficos(self, df, columna):
        dfProcesado = df.copy()
        lista = dfProcesado[columna].head(10).value_counts()
        lista = zip(lista, lista.index)
        return lista
    
    def procesarTablaLicencias(self, df):
        diferencia = df["licencias"] - df["cant_equipos"]
        lista = zip(df["licencias"], df["cant_equipos"], diferencia)
        return lista
    
    def procesarTablaTops(self, df, columna, columnaCount):
        dfProcesado = df.copy()
        lista1 = dfProcesado[columna].head(10)
        lista2 = dfProcesado[columnaCount].head(10)
        lista = zip(lista1, lista2)
        return lista

    def procesarTablaDevicesZonas(self, df, columna):
        try:
            dfProcesado = df.copy()
            total = []
            totalDict = {}
            ultimasa = []

            dfProcesado['zonename'] = dfProcesado['zonename'].replace('\""', '', regex=True)
            dfProcesado['zonename'] = dfProcesado['zonename'].replace('\[', '', regex=True)
            dfProcesado['zonename'] = dfProcesado['zonename'].replace('\]', '', regex=True)

            for x in dfProcesado["zonename"]: 
                for y in x:
                    total.append(y)
            unique_list = list(dict.fromkeys(total))
            for a in unique_list:
                
                while a[0] == " ":
                    a = a[1:]
                ultimasa.append(a)
            set_res = set(ultimasa)
            asco = list(set_res)

            for z in asco:
                totalDict[z] = 0
                for a in dfProcesado["zonename"]:
                    for b in a:
                        while b[0] == " ":
                            b = b[1:]
                        if z == b:
                            totalDict[z] += 1
            
            dictOrdenado = sorted(totalDict.items(), key=operator.itemgetter(1), reverse=True)                                
            return dictOrdenado

        except Exception as e:
            print(e)
        lista = dfProcesado[columna].value_counts()
        lista = zip(lista, lista.index)
        return lista

    def topQuarantinedCleared(self, df, tipo):
        #tipo "quarantined" o "Cleared"
        
        dfProcesado = df.copy()

        dfProcesado["FileMasPath"] = dfProcesado["filepath"]+ dfProcesado["filename"]
        dfQuarantined = dfProcesado[dfProcesado["filestatus"]==tipo]
        print(dfQuarantined)
        contador = dfQuarantined["FileMasPath"].value_counts().head(10)
        lista = zip(contador, contador.index.get_level_values(0))
        
        return lista



    def procesarTablaAccionesPorTipoMalware(self, df):
        nuevoDf = df["classification"].unique()
        listaDfs = []
        tuplas = []
        listaIndexGlobal = []
        contadorFinal = {}
        for i in nuevoDf:
            nuevoDf = df["classification"] == i
            nuevoDf2 = df[nuevoDf]
            contadorFilestatus = nuevoDf2["filestatus"].value_counts()
            for l in contadorFilestatus.index:
                
                listaIndexGlobal.append(l)
            lista = zip(contadorFilestatus, contadorFilestatus.index)
            listaEntera = ""
            for tupla in lista:
                listaEntera = listaEntera + tupla[1] + ": " + str(tupla[0]) + " "
                tuplas.append(tupla)
            dicContador = {
                "ClassFull" : i,
                "valores" : listaEntera
            }
            listaDfs.append(dicContador)
        res = np.unique(listaIndexGlobal)


        for x in res:
            contadorFinal[x] = 0
            for z in tuplas:
                if x == z[1]:
                    contadorFinal[x] += z[0]

        dictFinal = {"ClassFull": "Total",
                        "valores": str(contadorFinal).replace("{", "").replace("}", "").replace("'", "")}        
        listaDfs.append(dictFinal)                   
        return listaDfs

    def procesarTablaTopEventoEquipoUsuario(self, df, columna, columna2):
        df = df.copy()
        contador = df[columna].value_counts()
        contador = contador.head(10)
        index = contador.index
        listaFinal = []
        for device in index:   
            listaFinal.append(self.crearListaDeDevice(df, device, columna, columna2))

        return listaFinal

    def crearListaDeDevice(self, df, device, columna, columna2):
        df = df[df[columna] == device]
        contador = df[columna2].value_counts()
        lista = []

        for i in contador.index:
            if i == "VACIO":
                i = ("", contador[i])
            else:
                i = (i, contador[i])
            lista.append(i)

        dic = {"equipo" : device,
                "lista" : lista}
        return dic



    def procesarTablaDevicesActualizar(self, df):
        df = df.copy()
        df["versionTransformada"] = df["agentversion"].map(lambda x:self.transformarVersion(x))
        dfProcesado = df[df["versionTransformada"] <= 211574]
        dfProcesado = dfProcesado.sort_values(by=["agentversion"])
        lista = (dfProcesado[["devicename", "operativesystem", "agentversion"]]).values.tolist()

        return lista

    def versionCylanceSum(self, df):
        df = df.copy()
        df["versionTransformada"] = df["agentversion"].map(lambda x:self.transformarVersion(x))
        dfProcesado = df[df["versionTransformada"] <= 211574]
        dfProcesado = dfProcesado.sort_values(by=["agentversion"])
        
        lista = (dfProcesado[["agentversion"]]).value_counts()
        lista = (zip(lista, lista.index.get_level_values(0)), (dfProcesado[["agentversion"]]).value_counts().sum())

        return lista

    def transformarVersion(self, x):
        if x == "None":
            x = "nan"
        n = str(x).replace(".", "")
        if(n == "nan"):
            n = 211575
        return int(n)

    def procesarTablaPoliticasNoSeguras(self, df):
        df = df.copy()
        pattern = "Fase 1|Fase 2|Default"
        dfProcesado = df[df["policy"].str.contains(pattern, na = False)]
        lista = dfProcesado["policy"].value_counts()
        lista = zip(lista, lista.index)

        return lista
    
    def procesarTablaThreats(self, df):
        lista_datos = [list(row) for row in df.values]
        return lista_datos

    def procesarTablaEquiposOffline(self, df):
        df = df.copy()
        diasAtras = BLL_Fecha.Fecha().fechaInicio("diario", 15)
        dfProcesado = df[df["dateoffline"] != "Online"]
        
        dfProcesado2 = dfProcesado.copy()
        dfProcesado2["dateoffline"] = pd.to_datetime(dfProcesado.dateoffline)
        dfProcesado2 = dfProcesado2[dfProcesado2["dateoffline"] < diasAtras]
        dfProcesado2["dateoffline"] = dfProcesado2["dateoffline"].map(lambda x:self.volverAformatearFecha(x))
        #dfProcesado2["ips"] = dfProcesado2["ips"].map(lambda x:self.limpiarIPs(x))
        return (dfProcesado2[["devicename", "lastloggedinuser", "ips", "dateoffline"]]).values.tolist()

    def limpiarIPs(self, x):
        ip = re.search('((//d+//.){3}//d+)', str(x))
        if(type(ip) == NoneType):
            ip = "-"
        else:
            ip = ip.group(1)

        return ip

    def volverAformatearFecha(self, x):
        date = x.strftime("%m/%d/%Y %H:%M:%S")
        return date


    def __del__(self):
        gc.collect()