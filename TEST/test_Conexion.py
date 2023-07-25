import unittest
from DAL import DAL_Conexion
from DAL import DAL_Mapper_Eventos
from DAL import DAL_Mapper_Cliente
from BLL import BLL_Cliente


class Test_Conexion(unittest.TestCase):

    def test_Singleton(self):
        
        conexion1 = DAL_Conexion.Conexion()
        conexion2 = DAL_Conexion.Conexion()
        print(conexion1.database)
        print(str(id(conexion1)) + "        " + str(id(conexion2)))
        self.assertEqual(id(conexion1), id(conexion2))

    def test_LeerArchivo(self):
        
        conexion = DAL_Conexion.Conexion()
        conexion.leerArchivo()

    def test_GetAccessToken(self):
        mapper = DAL_Mapper_Eventos.Mapper_Eventos()
        conexion = DAL_Conexion.Conexion()
        conexion.asignarAtributos("**")
        mapper.asignarConexion(conexion)

        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        
        for cliente in clientes:
            if cliente.nombre == "Ran":
                datos = mapper.leerEventos(cliente, "TokensZoho")
                token = conexion.getAccessToken(datos)
                print(token)
                self.assertEqual(type(token), str)