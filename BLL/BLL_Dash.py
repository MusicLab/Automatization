from BLL import BLL_Grafico_Personalizado
from BLL import BLL_Log
from BLL import BLL_Fecha
import matplotlib.pyplot as plt

class Dash(object):
    def __init__(self):
            pass

    def dashHist(self, tipoDato, columna, cliente, fechaInicio, fechaFin, default = True):
        log = BLL_Log.Log()
        grafHist = ""
        grafico = BLL_Grafico_Personalizado.Grafico_Personalizado()
        try:
            if default == True:
                fecha = BLL_Fecha.Fecha()
                fechaInicio = fecha.fechaInicio("diario", 2)
                fechaFin = fecha.fechaFin()
                grafHist = grafico.graficoPersonalizadoDash("Histograma", "DeviceCount", "noHaceFaltaColumnaReemplazarPds", "todos", fechaInicio, fechaFin)
            elif default == False:
                grafHist = grafico.graficoPersonalizadoDash("Histograma", tipoDato, columna, cliente, fechaInicio, fechaFin)
        except Exception as e:
            log.escribir("Error en Dashboard: " + str(e), tipo = "error")

        return grafHist    
    
    def dashBarrasExploits(self, tipoDato, columna, cliente, fechaInicio, fechaFin, default = True):
        log = BLL_Log.Log()
        grafico = BLL_Grafico_Personalizado.Grafico_Personalizado()
        try:
            if default == True:
                # fecha = BLL_Fecha.Fecha()
                # fechaInicio = fecha.fechaInicio("diario")
                # fechaFin = fecha.fechaFin()
                grafBarrasExploits, ax = plt.subplots(figsize = (10,5))
                #grafBarrasExploits = BLL_Grafico_Personalizado.Grafico_Personalizado("Barras", "Exploits", "filename", cliente, fechaInicio, fechaFin)
            elif default == False:
                grafBarrasExploits = grafico.graficoPersonalizadoDash("Barras", tipoDato, columna, cliente, fechaInicio, fechaFin)
        except Exception as e:
            log.escribir("Error en Dashboard: " + str(e), tipo = "error")

        return grafBarrasExploits
   
   
    def dasBarrasThreatsOnly(self, tipoDato, columna, cliente, fechaInicio, fechaFin, default = True):
        log = BLL_Log.Log()
        grafico = BLL_Grafico_Personalizado.Grafico_Personalizado()
        try:
            if default == True:
                # fecha = BLL_Fecha.Fecha()
                # fechaInicio = fecha.fechaInicio("diario")
                # fechaFin = fecha.fechaFin()
                grafBarrasThreatsOnly, ax = plt.subplots(figsize = (10,5))
                #grafBarrasThreatsOnly = BLL_Grafico_Personalizado.Grafico_Personalizado("Barras", "ThreatsOnly", "sha256", cliente, fechaInicio, fechaFin)
            elif default == False:
                grafBarrasThreatsOnly = grafico.graficoPersonalizadoDash("Barras", tipoDato, columna, cliente, fechaInicio, fechaFin)
        except Exception as e:
            log.escribir("Error en Dashboard: " + str(e), tipo = "error")

        return grafBarrasThreatsOnly
            
    def dashTortaClearedEvent(self, tipoDato, columna, cliente, fechaInicio, fechaFin, default = True):
        log = BLL_Log.Log()
        grafico = BLL_Grafico_Personalizado.Grafico_Personalizado()
        try:
            if default == True:
                # fecha = BLL_Fecha.Fecha()
                # fechaInicio = fecha.fechaInicio("diario")
                # fechaFin = fecha.fechaFin()
                grafTortaClearedEvent, ax = plt.subplots(figsize = (9,6))
                #grafTortaClearedEvent = BLL_Grafico_Personalizado.Grafico_Personalizado("Torta", "ClearedEvent", "classification", cliente, fechaInicio, fechaFin)
            elif default == False:
                grafTortaClearedEvent = grafico.graficoPersonalizadoDash("Torta", tipoDato, columna, cliente, fechaInicio, fechaFin)
        except Exception as e:
            log.escribir("Error en Dashboard: " + str(e), tipo = "error")

        return grafTortaClearedEvent