import unittest
from time import sleep
from BLL import BLL_Encripcion
from DAL import DAL_Mapper_Archivo


class Test_Encripcion(unittest.TestCase):

    def test_EncriptarDatosConexion(self):
        
        encripcion = BLL_Encripcion.Encripcion()
        encripcion.encriptarDatosConexion()
        print(encripcion.listaConexion)
        sleep(10)
        encripcion.desencriptarDatosConexion()
        print(encripcion.listaConexion)

    def test_DesencriptarDatosConexion(self):
        
        encripcion = BLL_Encripcion.Encripcion()
        encripcion.desencriptarDatosConexion()

    def test_EncriptarDatosArchivo(self):
        
        encripcion = BLL_Encripcion.Encripcion()
        mapperArchivo = DAL_Mapper_Archivo.Mapper_Archivo()
        if(mapperArchivo.mapperVerificarEstadoArchivo() == False):
            encripcion.encriptarDatosArchivo()
        
            encripcion.desencriptarDatosArchivo()

    def test_DesencriptarDatosArchivo(self):
        
        encripcion = BLL_Encripcion.Encripcion()
        encripcion.estadoArchivo = True
        encripcion.desencriptarDatosArchivo()

    