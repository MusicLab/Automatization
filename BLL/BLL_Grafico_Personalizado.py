from BLL import BLL_Log
from BLL import BLL_Dataframe_Personalizado
from BLL import BLL_Grafico
from BE import BE_Grafico
import gc
import os
from PySide2.QtGui import QPixmap

class Grafico_Personalizado(BLL_Grafico.Grafico):

    def __init__(self):
        BE_Grafico.Grafico.setID(self, 1)
        BE_Grafico.Grafico.setNombre(self, ".//DATA//GRAFICOS//Grafico Personalizado.png")


    def graficoPersonalizado(self, tipoGrafico, tipoDato, columna, cliente, fechaInicio, fechaFin, top = None):
        try:
            dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()    
            filas = dataframe.leerEventosDB(fechaInicio, fechaFin, cliente, tipoDato)
            df = dataframe.crearDataframePersonalizado(filas)
            if tipoGrafico == "Torta":
                graf = self.graficarTorta(df, columna, 10)
            elif tipoGrafico == "Barras":
                graf = self.graficarBarras(df, columna, 10)
            elif tipoGrafico == "Histograma":
                graf = self.graficarHistograma(df)
            
            graf.savefig(os.getcwd() + "//DATA//GRAFICOS//Grafico Personalizado.png", bbox_inches='tight')
            
        except Exception as e:
            BLL_Log.Log().escribir("Error en Grafico Personalizado: " + str(e), cliente.nombre, "error")

        return graf
    

    def graficoPersonalizadoDash(self, tipoGrafico, tipoDato, columna, cliente, fechaInicio, fechaFin, top = None):
        pixmap = ""
        try:
            dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()    
            filas = dataframe.leerEventosDB(fechaInicio, fechaFin, cliente, tipoDato)
            df = dataframe.crearDataframePersonalizado(filas)
            if tipoGrafico == "Torta":
                graf = self.graficarTorta(df, columna, 10)
            elif tipoGrafico == "Barras":
                graf = self.graficarBarras(df, columna, 10)
            elif tipoGrafico == "Histograma":
                graf = self.graficarHistograma(df)
            
            rutaGraficoTemporal = os.getcwd() + "//DATA//GRAFICOS//graficoTemporal.png"
            graf.savefig(rutaGraficoTemporal, bbox_inches='tight')
            print(df)
            pixmap = QPixmap(rutaGraficoTemporal)
            os.remove(rutaGraficoTemporal)
            
        except Exception as e:
            BLL_Log.Log().escribir("Error en Grafico PersonalizadoDash: " + str(e), "general", "error")

        return pixmap


    

    def __del__(self):
        gc.collect()