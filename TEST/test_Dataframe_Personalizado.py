import unittest
from BLL import BLL_Fecha
from BLL import BLL_Cliente
from BLL import BLL_Fecha
from BLL import BLL_Dataframe_Personalizado
from DAL import DAL_Mapper_Cliente



class Test_Dataframe_Personalizado(unittest.TestCase):

    def test_CrearDataframePersonalizado(self):

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaInicio.date()
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i
        filas = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "ThreatsFilestatusCleared")
        df = dataframe.crearDataframePersonalizado(filas)

        print(df)
        self.assertEqual(True, True)

    def test_CrearDataframePersonalizadoThreatsUsuarios(self):
        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("mensual")
        fechaInicio.date()
        fechaFin = fecha.fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i
        filas = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "ThreatsUsuarios")
        print(filas)
        df = dataframe.crearDataframePersonalizado(filas)
        # print(df)
        # print('\n')
        # self.assertEqual(True, True)



    def test_CrearDataframeReemplazoPandas(self):

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaInicio.date()
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i
        filas = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "ClearedEvent")
        df = dataframe.crearDataframePersonalizado(filas)

        print(df)
        self.assertEqual(True, True)