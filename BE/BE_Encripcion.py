class Encripcion(object):

    __key = ""
    __listaConexion = []
    __estado = False
    __estadoArchivo = False

    def getKey(self):
        return self.key
    
    def setKey(self, key):
        self.key = key

    def getListaConexion(self):
        return self.listaConexion
    
    def setListaConexion(self, lista):
        self.listaConexion = lista

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado

    def getEstadoArchivo(self):
        return self.estadoArchivo
    
    def setEstadoArchivo(self, estado):
        self.estadoArchivo = estado
