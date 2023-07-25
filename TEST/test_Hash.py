import unittest
from BLL import BLL_Hash
from BLL import BLL_Cliente


class Test_Hash(unittest.TestCase):

    def test_agregarMultiHash(self):
        
        ruta = ".//DATA//CLIENTES//Hashes.csv"
        hash = BLL_Hash.Hash()
        cliente = BLL_Cliente.Cliente()

        listaClientes = cliente.crearLista()
        listaActual = []
        for cliente in listaClientes:
            if cliente.nombre == "Ran":
                listaActual.append(cliente)

        hash.cargarMultiHashes(listaActual, ruta, "safe", "pruebaMultiHash", "None")
        self.assertEqual(200, 200)


