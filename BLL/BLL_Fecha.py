from datetime import datetime, timedelta
from BE import BE_Fecha
import dateutil.relativedelta
import gc
from UTILITIES import Singleton   


class Fecha(metaclass=Singleton.Singleton):
    def __init__(self):
        BE_Fecha.Fecha.setFechaActual(self, datetime.now())

    def fechaInicio(self, tipo, cantidad = 1):
        if tipo == "diario":
            hoy = datetime.now() - timedelta(cantidad)
        if tipo == "mensual":
            hoy = datetime.now() - dateutil.relativedelta.relativedelta(months=cantidad)
        if tipo == "semanal":
            hoy = datetime.now() - timedelta(cantidad*7)
        inicio = hoy - timedelta(0,hoy.second, hoy.microsecond, 0, hoy.minute, hoy.hour)
        return inicio

    def fechaFin(self):
        hoy = datetime.now()
        hoy = hoy - timedelta(0,hoy.second, hoy.microsecond, 0, hoy.minute, hoy.hour)
        fin = hoy - timedelta(0,1)
        return fin
    
    def isoFormat(self):
        return datetime.now().isoformat(sep='T')

    def ahora(self):
        return datetime.now()

    #def recalcularNow(self):
    #    BE_Fecha.Fecha.setFechaActual(self, datetime.now())
    #    return BE_Fecha.Fecha.getFechaActual(self)

    def __del__(self):
        gc.collect()




