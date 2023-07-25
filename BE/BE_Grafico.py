class Grafico(object):
    __ID = ""
    __nombre = ""
    __ejes = ""
    __columna = ""
    __evento = ""


    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEjes(self):
        return self.ejes

    def setEjes(self, ejes):
        self.ejes = ejes

    def getColumna(self):
        return self.columna

    def setColumna(self, columna):
        self.columna = columna

    def getEvento(self):
        return self.evento

    def setEvento(self, evento):
        self.evento = evento


