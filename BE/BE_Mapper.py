
class Mapper(object):
    
    __conexion = False

    def getConexion(self):
        return self.conexion

    def setConexion(self, conexion):
        self.conexion = conexion
