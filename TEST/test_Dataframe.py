import unittest
import os
from BLL import BLL_Dataframe
from BLL import BLL_Fecha
from BLL import BLL_Cliente
from BLL import BLL_Fecha
from BLL import BLL_Archivo
from BLL import BLL_Dataframe
import dateutil.parser as parser
from DAL import DAL_Mapper_Cliente



class Test_Dataframe(unittest.TestCase):


    def test_DataframeVacio(self):
        self.assertEqual(True, True)

    def test_DataframeDiario(self):
        
        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("diario")
        fechaFin = fecha.fechaFin()
        archivo = BLL_Archivo.Archivo(".//DATA//CSVS//")
        DAL_Mapper_Cliente.Mapper_Cliente().conexion.asignarAtributos("**")
        listaCliente = BLL_Cliente.Cliente().crearListaDB()

        files = [file for file in os.listdir(archivo.ruta)]
    
        for cliente in listaCliente:
            if cliente.nombre == "Banco Patagonia":
                dataframe = BLL_Dataframe.Dataframe(cliente, fechaInicio, fechaFin, archivo)
                dataframe.unificarCsvThreat(archivo.ruta)
                dataframe.crearDataframe(archivo.ruta)
        
            #Exploits

                df = dataframe.diccCSV["exploit"]
                
                for index, row in df.iterrows():
                    self.assertEqual(row["Created"].day, fecha.fechaFin().day)

                    #Threats
                df2 = dataframe.diccCSV["threat"]
                
                for index, row in df2.iterrows():
                    row = parser.parse(row["DateFound"])
                    
                    self.assertEqual(row.day, fecha.fechaFin().day)

    
    def test_DataframeInsercionDB(self):
        
        fecha = BLL_Fecha.Fecha()
        fechaInicio = fecha.fechaInicio("diario")
        fechaFin = fecha.fechaFin()
        archivo = BLL_Archivo.Archivo(".//DATA//CSVS//")
        DAL_Mapper_Cliente.Mapper_Cliente().conexion.asignarAtributos("**")
        listaCliente = BLL_Cliente.Cliente().crearListaDB()
    
        for cliente in listaCliente:     
            if cliente.nombre == "Banco Patagonia":
            
                dataframe = BLL_Dataframe.Dataframe(cliente, fechaInicio, fechaFin, archivo)
                dataframe.unificarCsvThreat(archivo.ruta)
                dataframe.crearDataframe(archivo.ruta)
                dataframe.dataframeADB("device", "mensual")
                dataframe.dataframeADB("threat", "mensual")
                dataframe.dataframeADB("exploit", "mensual")

                
        
            
    #def test_integridad(self):

    #            for file in self.files:
    #                # ------------------------ EXPLOITS -----------------------
    #                if self.nombreArchivo in file and "Memory Protection" in file:
    #                    exploitLectura = pd.read_csv(self.rutaCSV + file, encoding='utf-8')

    #                    for index, row in exploitLectura.iterrows():
    #                        for index2, row2 in self.dataframe.diccCSV["exploit"].iterrows():
    #                            if index == index2:
    #                                self.assertEqual(row["DeviceName"],row2["DeviceName"])
    #                                self.assertEqual(row["UserName"],row2["UserName"])
    #                                #self.assertEqual(row["ViolationType"],row2["ViolationType"])
    #                               #self.assertEqual(row["Action"],row2["Action"])
    #                                self.assertEqual(row["FilePath"],row2["FilePath"])
    #                                self.assertEqual(row["FileName"],row2["FileName"])
    #                                #self.assertEqual(row["Created"],row2["Created"])
    #                                self.assertEqual(row["ProcessID"],row2["ProcessID"])

    #                # ------------------------ DEVICES -----------------------
    #                if self.nombreArchivo in file and "Devices" in file:
    #                    deviceLectura = pd.read_csv(self.rutaCSV + file, encoding='utf-8')

    #                    for index, row in deviceLectura.iterrows():
    #                        for index2, row2 in self.dataframe.diccCSV["device"].iterrows():
    #                            if index == index2:
    #                                #self.assertEqual(row["OperativeSystem"],row2["OperativeSystem"])
    #                                self.assertEqual(row["DeviceName"],row2["DeviceName"])
    #                                #self.assertEqual(row["AgentVersion"],row2["AgentVersion"])
    #                                #self.assertEqual(row["Policy"],row2["Policy"])
    #                                #self.assertEqual(row["IPs"],row2["IPs"])
    #                                #self.assertEqual(row["ZoneName"],row2["ZoneName"])
    #                                self.assertEqual(row["LastLoggedInUser"],row2["LastLoggedInUser"])
                                
    #                ## ------------------------ THREATS -----------------------

    #                if self.nombreArchivo in file and "Threats" in file:
    #                    threatLectura = pd.read_csv(self.rutaCSV + file, encoding='utf-8')
                        


    #                    for index, row in threatLectura.iterrows():
    #                        for index2, row2 in self.dataframe.diccCSV["threat"].iterrows():
    #                            if index == index2:
    #                                self.assertEqual(row["FileStatus"],row2["FileStatus"])
    #                                self.assertEqual(row["DeviceName"],row2["DeviceName"])
    #                                self.assertEqual(row["FilePath"],row2["FilePath"])
    #                                self.assertEqual(row["FileName"],row2["FileName"])
    #                                self.assertEqual(row["Classification"],row2["Classification"])
    #                                self.assertEqual(row["SubClass"],row2["SubClass"])
    #                                #self.assertEqual(row["FileOwner"],row2["FileOwner"])
    #                                #self.assertEqual(row["DriveType"],row2["DriveType"])
    #                                self.assertEqual(row["OrigenDeDato"],row2["OrigenDeDato"])

    


