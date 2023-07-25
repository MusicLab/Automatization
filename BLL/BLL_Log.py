from LOG import L_Log
from BLL import BLL_Archivo
from DAL import DAL_Mapper_Log
import gc
from UTILITIES import Singleton  

class Log(metaclass=Singleton.Singleton):

    def __init__(self):
        archivo = BLL_Archivo.Archivo("..//DATA//LOGS//", "Logs.txt")
        L_Log.Log.setArchivo(self, archivo)

        
    def escribir(self, datos, cliente = "General", tipo = ""):
        print(datos)
        mapper = DAL_Mapper_Log.Mapper_Log()
        mapper.mapperLog(self.archivo, datos, cliente, tipo)

    def __del__(self):
        gc.collect()


