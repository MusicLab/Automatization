import unittest
from BLL import BLL_Cliente
from DAL import DAL_Mapper_Cliente


class Test_Cliente(unittest.TestCase):

    def test_CrearLista(self):
        

        DAL_Mapper_Cliente.Mapper_Cliente().conexion.asignarAtributos("**")
        listaCliente = BLL_Cliente.Cliente().crearListaDB()
        print(listaCliente)
        self.assertEqual(type(listaCliente), list)

    def test_AgregarClienteDB(self):
        

        DAL_Mapper_Cliente.Mapper_Cliente().conexion.asignarAtributos("**")
        BLL_Cliente.Cliente.agregarDB(self, "nombreTest22", "regionTe", "tokenTest", "tidTest222", "aidTest", "sidTest", "logoTest", "1")

    def test_BorrarClienteDB(self):
        

        DAL_Mapper_Cliente.Mapper_Cliente().conexion.asignarAtributos("**")

        cliente = BLL_Cliente.Cliente()    
        listaCliente = cliente.crearListaDB()
        for i in listaCliente:
            print(i)
            if i.tid == "tidTest222":
                BLL_Cliente.Cliente.borrarDB(self, i.tid)


    def test_LeerClienteEspecifico(self):
        mapper = DAL_Mapper_Cliente.Mapper_Cliente()
        mapper.conexion.asignarAtributos("**")
        cliente = BLL_Cliente.Cliente()
        ran = cliente.leerClienteEspecifico("Ran")
        print(ran.nombre)
        self.assertEqual(ran.nombre, "Ran")