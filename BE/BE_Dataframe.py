class Dataframe(object):
    __cliente = ""
    __fechaInicio = ""
    __fechaFin = ""
    __archivo = ""
    __log = ""
    __diccCSV = {
                "cliente" : "",
                "threat" : "",
                "exploit" : "",
                "device" : "",
                "clearedEvent" : "",
                "threatSolo" : ""
                }
    
    
    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente

    def getFechaInicio(self):
        return self.fechaInicio

    def setFechaInicio(self, fechaInicio):
        self.fechaInicio = fechaInicio

    def getFechaFin(self):
        return self.fechaFin

    def setFechaFin(self, fechaFin):
        self.fechaFin = fechaFin

    def getArchivo(self):
        return self.archivo

    def setArchivo(self, archivo):
        self.archivo = archivo

    def getLog(self):
        return self.log

    def setLog(self, log):
        self.log = log

    def getDiccCSV(self):
        return self.diccCSV
    
    def setDiccCSV(self, diccCSV):
        if diccCSV["cliente"] != None and diccCSV["threat"] != None and diccCSV["exploit"] != None and diccCSV["device"] != None and diccCSV["clearedEvent"] != None and diccCSV["threatSolo"] != None and len(diccCSV) == 6:
            self.diccCSV = diccCSV




