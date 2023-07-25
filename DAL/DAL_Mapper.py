import gc
from BE import BE_Mapper
from DAL import DAL_Conexion

class Mapper(object):

    def __init__(self):
        conexion = DAL_Conexion.Conexion()
        BE_Mapper.Mapper.setConexion(self, conexion)


    def asignarConexion(self, conexion):
        self.conexion = conexion

    def mapperConectarDB(self):
        self.conexion.conectarDB()

    def mapperDesconectarDB(self):
        self.conexion.desconectarDB()

    def mapperEncriptar(self):
        self.conexion.encriptarConexion()

    def mapperDesencriptar(self):
        self.conexion.desencriptarConexion()

    def mapperEncriptarArchivo(self):
        self.conexion.encriptarArchivo()


    def __del__(self):
        gc.collect()


