import unittest
from BLL import BLL_Fecha
from BLL import BLL_Tabla
from BLL import BLL_Cliente
from BLL import BLL_Fecha
from BLL import BLL_Dataframe_Personalizado
from DAL import DAL_Mapper_Cliente
import datetime




class Test_Tabla(unittest.TestCase):
 
    def test_TablaProcesarDevices(self):
        
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("diario") - datetime.timedelta(days=1)
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        lista = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "ThreatsUsuarios")
        df = dataframe.crearDataframePersonalizado(lista)
        tabla = BLL_Tabla.Tabla()
        tablaPrueba = tabla.procesarTabla(df, "devicename")
        print(list(tablaPrueba))
        self.assertEqual(type(tablaPrueba), zip)

    def test_TablaProcesarDevicesZonas(self):
        
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        lista = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "Devices")
        print(lista)
        df = dataframe.crearDataframePersonalizado(lista, "Devices")
        tabla = BLL_Tabla.Tabla()
        tablaPrueba = tabla.procesarTablaDevicesZonas(df, "zonename")
        print(list(tablaPrueba))
        self.assertEqual(type(tablaPrueba), zip)

    def test_topQuarantined(self):
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        lista = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "ThreatsFilestatusQuarantined")

        df = dataframe.crearDataframePersonalizado(lista)

        tabla = BLL_Tabla.Tabla()
        tablaPrueba = tabla.procesarTablaThreats(df)
        print(tablaPrueba)
        self.assertEqual(type(tablaPrueba), list)


    def test_topCleared(self):

        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        lista = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "ThreatsFilestatusCleared")

        df = dataframe.crearDataframePersonalizado(lista)

        tabla = BLL_Tabla.Tabla()
        tablaPrueba = tabla.procesarTablaThreats(df)
        print(tablaPrueba)
        self.assertEqual(type(tablaPrueba), list)

    def test_procesarTablaAccionesPorTipoMalware(self):
        
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("diario")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        lista = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "ClearedEvent")
        df = dataframe.crearDataframePersonalizado(lista, "Threats")
        tabla = BLL_Tabla.Tabla()
        tablaPrueba = tabla.procesarTablaAccionesPorTipoMalware(df)
        print(list(tablaPrueba))
        self.assertEqual(type(tablaPrueba), list)

    def test_procesarTablaTopExploitsEquipoUsuario(self):
        
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        lista = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "Exploits")
        df = dataframe.crearDataframePersonalizado(lista, "Exploits")
        tabla = BLL_Tabla.Tabla()
        tablaPrueba = tabla.procesarTablaTopExploitsEquipoUsuario(df, "devicename")
        print(list(tablaPrueba))
        self.assertEqual(type(tablaPrueba), list)

    def test_procesarTablaDevicesActualizar(self):
        
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        lista = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "Devices")
        df = dataframe.crearDataframePersonalizado(lista, "Devices")
        tabla = BLL_Tabla.Tabla()
        tablaPrueba = tabla.procesarTablaDevicesActualizar(df)
        print(list(tablaPrueba))
        self.assertEqual(type(tablaPrueba), list)

    def test_tablaProcesarTablaPoliticasNoSeguras(self):
        
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        lista = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "Devices")
        df = dataframe.crearDataframePersonalizado(lista, "Devices")
        tabla = BLL_Tabla.Tabla()
        tablaPrueba = tabla.procesarTablaPoliticasNoSeguras(df)
        print(list(tablaPrueba))
        self.assertEqual(type(tablaPrueba), zip)


    def test_procesarTablaEquiposOffline(self):
        
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("mensual")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for i in clientes:
            if i.nombre == "Banco Patagonia":
                patagonia = i

        dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        lista = dataframe.leerEventosDB(fechaInicio, fechaFin, patagonia, "Devices")
        df = dataframe.crearDataframePersonalizado(lista, "Devices")
        tabla = BLL_Tabla.Tabla()
        tablaPrueba = tabla.procesarTablaEquiposOffline(df)


        print(list(tablaPrueba))
        self.assertEqual(type(tablaPrueba), list)

    def test_ProcesarTablaTops(self):
        
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("diario")
        fechaFin = BLL_Fecha.Fecha().fechaFin()
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for cliente in clientes:
            if cliente.nombre == "Banco Patagonia":

                dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
                lista = dataframe.leerEventosDB(fechaInicio, fechaFin, cliente, "Devices")
                df = dataframe.crearDataframePersonalizado(lista)
                tabla = BLL_Tabla.Tabla()
                tablaPrueba = tabla.procesarTablaTops(df, "policy")
                print(list(tablaPrueba))
                self.assertEqual(type(tablaPrueba), zip)

    def test_ProcesarTablaLicencias(self):
        fechaInicio = BLL_Fecha.Fecha().fechaInicio("diario")
        fechaFin = BLL_Fecha.Fecha().fechaFin() - datetime.timedelta(days=35)
        mapperCliente = DAL_Mapper_Cliente.Mapper_Cliente()
        mapperCliente.conexion.asignarAtributos("**")
        mapperCliente.mapperConectarDB()
        clientes = BLL_Cliente.Cliente().crearListaDB()
        for cliente in clientes:
            if cliente.nombre == "Ran":
                dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
                lista = dataframe.leerEventosDB(fechaInicio, fechaFin, cliente, "cantEquiposLic")
                df = dataframe.crearDataframePersonalizado(lista)
                tabla = BLL_Tabla.Tabla()
                tablaPrueba = tabla.procesarTablaLicencias(df)
                print(list(tablaPrueba))
                self.assertEqual(type(tablaPrueba), zip)



if __name__ == '__main__':
    unittest.main()
