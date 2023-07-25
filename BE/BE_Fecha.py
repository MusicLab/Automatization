class Fecha(object):
    __fechaActual = ""
    __tipo = ""

    def getFechaActual(self):
        return self.fechaActual

    def setFechaActual(self, fechaActual):
        self.fechaActual = fechaActual

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        if tipo == "diario" or "semanal" or "mensual":
            self.tipo = tipo
        




