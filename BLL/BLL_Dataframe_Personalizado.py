import pandas as pd
from DAL import DAL_Mapper_Eventos
from BLL import BLL_Log



class Dataframe_Personalizado(object):

    def __init__(self):
        pass

    def crearDataframePersonalizado(self, dictTuplas):

        df = pd.DataFrame(dictTuplas["rows"], columns = dictTuplas["columns"])

        return df
        
    
    def leerEventosDB(self, fechaInicio, fechaFin, cliente, tipoEvento):
        
        mapper = DAL_Mapper_Eventos.Mapper_Eventos()
        return mapper.leerEventos(cliente, tipoEvento, fechaInicio, fechaFin)
    
    