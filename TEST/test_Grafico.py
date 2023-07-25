import os
import unittest
from BLL import BLL_Grafico
from BLL import BLL_Fecha
from BLL import BLL_Cliente
from BLL import BLL_Fecha
from BLL import BLL_Dataframe_Personalizado
from DAL import DAL_Mapper_Eventos
from DAL import DAL_Conexion
import datetime



class Test_Grafico(unittest.TestCase):
    


    def test_GraficarBarras(self):

        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("mensual")
        fechaFin = fecha.fechaFin()
        conexion = DAL_Conexion.Conexion()
        conexion.asignarAtributos("**")
        mapperEventos = DAL_Mapper_Eventos.Mapper_Eventos()
        mapperEventos.asignarConexion(conexion)
    
        cliente = BLL_Cliente.Cliente()
        listaClientes = cliente.crearListaDB()

        dfPersonalizado = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        print("estoy aca")
        for cliente in listaClientes:    
            funciono = False
            if cliente.nombre == "Banco Patagonia":
                mapperEventos.conexion.conectarDB()
                filas = mapperEventos.leerEventos(fechaInicio, fechaFin, "ThreatsUsuarios", cliente)
                df = dfPersonalizado.crearDataframePersonalizado(filas, "Deprecado")

                grafico = BLL_Grafico.Grafico()
                graf = grafico.graficarBarras(df, "lastloggedinuser", 10)
                graf.savefig(os.getcwd() + "//DATA//GRAFICOS//prueba barras " + cliente.nombre + ".png", bbox_inches='tight')
                if(os.path.exists(os.getcwd() + "//DATA//GRAFICOS//prueba barras " + cliente.nombre + ".png")):
                    funciono = True

                self.assertEqual(funciono, True)

    def test_GraficarBarrasContadas(self):

            fecha = BLL_Fecha.Fecha()
            fechaInicio = fecha.fechaInicio("diario")
            fechaFin = fecha.fechaFin()
            conexion = DAL_Conexion.Conexion()
            conexion.asignarAtributos("**")
        
            listaClientes = BLL_Cliente.Cliente().crearListaDB()

            for cliente in listaClientes:    
                funciono = False
                if cliente.nombre == "Banco Patagonia":

                    filas = DAL_Mapper_Eventos.Mapper_Eventos().leerEventos(cliente, "ThreatsUsuarios", fechaInicio, fechaFin)

                    df = BLL_Dataframe_Personalizado.Dataframe_Personalizado().crearDataframePersonalizado(filas, "Deprecado")
                    print(df)
                    grafico = BLL_Grafico.Grafico()
                    graf = grafico.graficarBarrasContadas(df, "devicename", 10)


                    graf.savefig(os.getcwd() + "//DATA//GRAFICOS//prueba barras " + cliente.nombre + ".png", bbox_inches='tight')
                    if(os.path.exists(os.getcwd() + "//DATA//GRAFICOS//prueba barras " + cliente.nombre + ".png")):
                        funciono = True

                    self.assertEqual(funciono, True)



    def test_GraficoTorta(self):
        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("mensual")
        fechaFin = fecha.fechaFin()
        conexion = DAL_Conexion.Conexion()
        conexion.asignarAtributos("**")
        mapperEventos = DAL_Mapper_Eventos.Mapper_Eventos()
        mapperEventos.asignarConexion(conexion)
    
        cliente = BLL_Cliente.Cliente()
        listaClientes = cliente.crearListaDB()
        dfPersonalizado = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        for cliente in listaClientes:    
            funciono = False
            if cliente.nombre == "Banco Patagonia":
                mapperEventos.conexion.conectarDB()
                filas = mapperEventos.leerEventos(cliente, "Threats", fechaInicio, fechaFin)
                df = dfPersonalizado.crearDataframePersonalizado(filas, "Threats")
                print(df)
                grafico = BLL_Grafico.Grafico()
                graf = grafico.graficarTorta(df, "classification", 10)
                graf.savefig(os.getcwd() + "//DATA//GRAFICOS//prueba torta " + cliente.nombre + ".png")
                if(os.path.exists(os.getcwd() + "//DATA//GRAFICOS//prueba torta " + cliente.nombre + ".png")):
                    funciono = True

                self.assertEqual(funciono, True)

    def test_GraficarHist(self):

        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("mensual")
        fechaFin = fecha.fechaFin()
        conexion = DAL_Conexion.Conexion()
        conexion.asignarAtributos("**")
        mapperEventos = DAL_Mapper_Eventos.Mapper_Eventos()
        mapperEventos.asignarConexion(conexion)
    
        cliente = BLL_Cliente.Cliente()
        listaClientes = cliente.crearListaDB()
        dfPersonalizado = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        for cliente in listaClientes:    
            funciono = False
            if cliente.nombre == "Banco Patagonia":
                mapperEventos.conexion.conectarDB()
                filas = mapperEventos.leerEventos(cliente, "ThreatOnlyCount", fechaInicio, fechaFin)
                df = dfPersonalizado.crearDataframePersonalizado(filas)
                print(df)
                grafico = BLL_Grafico.Grafico()
                graf = grafico.graficarHistograma(df)
                graf.savefig(os.getcwd() + "//DATA//GRAFICOS//prueba hist " + cliente.nombre + ".png")
                if(os.path.exists(os.getcwd() + "//DATA//GRAFICOS//prueba hist " + cliente.nombre + ".png")):
                    funciono = True

                self.assertEqual(funciono, True)

