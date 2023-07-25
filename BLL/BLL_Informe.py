from BLL import BLL_Grafico
from BLL import BLL_Tabla
from BLL import BLL_Dataframe_Personalizado
from BLL import BLL_Log
from BLL import BLL_Archivo
from docx.shared import Mm
import os
from docxtpl import DocxTemplate, InlineImage
import gc
import shutil
import time

class Informe(object):

    log = BLL_Log.Log()

    def __init__(self, fechaInicio, fechaFin, cliente, tipo):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.cliente = cliente
        self.archivo = BLL_Archivo.Archivo()
        self.dataframe = BLL_Dataframe_Personalizado.Dataframe_Personalizado()
        self.tipo = tipo


    def hacerInforme(self): #AGREGAR REQUEST COMO PARAMETRO
        directorioInformes = self.archivo.generarDirectorios("./DATA/INFORMES/", self.fechaFin, self.cliente.nombre)

        if self.tipo == "diario":
            doc = DocxTemplate(".//DATA//TEMPLATES//templateDiario.docx")
        elif self.tipo == "semanal":
            doc = DocxTemplate(".//DATA//TEMPLATES//templateSemanal.docx")
        else:
            doc = DocxTemplate(".//DATA//TEMPLATES//templateMensual.docx")

        
        if self.tipo == "semanal" or self.tipo == "diario":
            numeroInforme = str(self.fechaFin.month) + str(self.fechaFin.year) + str(self.fechaFin.day)
        else:
            numeroInforme = str(self.fechaFin.month) + str(self.fechaFin.year)
        fechaInicioFormat = self.fechaInicio.date()
        fechaFinFormat = self.fechaFin.now().date()

        listaThreatsOnly = self.dataframe.leerEventosDB(self.fechaInicio, self.fechaFin, self.cliente, "ThreatsOnly")
        listaClearedEvent = self.dataframe.leerEventosDB(self.fechaInicio, self.fechaFin, self.cliente, "ClearedEvent")

        listaExploits = self.dataframe.leerEventosDB(self.fechaInicio, self.fechaFin, self.cliente, "Exploits")

        listaDevices = self.dataframe.leerEventosDB(self.fechaInicio, self.fechaFin, self.cliente, "Devices")

        listaThreatsUsuarios = self.dataframe.leerEventosDB(self.fechaInicio, self.fechaFin, self.cliente, "ThreatsUsuarios")
        #listaDevicesSinProt = self.dataframe.leerEventosDB(self.fechaInicio, self.fechaFin, self.cliente, "DevicesSinProt")
        listaDevicesSinZonas = self.dataframe.leerEventosDB(self.fechaInicio, self.fechaFin, self.cliente, "DevicesSinZonas")
        #listaLicencias = self.generarListaLicencias(request, selcliente)
        listaThreatsFilestatusQuarantined = self.dataframe.leerEventosDB(self.fechaInicio, self.fechaFin, self.cliente, "ThreatsFilestatusQuarantined")
        listaThreatsFilestatusCleared = self.dataframe.leerEventosDB(self.fechaInicio, self.fechaFin, self.cliente, "ThreatsFilestatusCleared")
        # <----//---- se declara directorio de informe por cliente ----//---->



        dfThreatsOnly = self.dataframe.crearDataframePersonalizado(listaThreatsOnly)
        dfClearedEvent = self.dataframe.crearDataframePersonalizado(listaClearedEvent)
        dfExploits = self.dataframe.crearDataframePersonalizado(listaExploits)
        dfDevices = self.dataframe.crearDataframePersonalizado(listaDevices)
        dfThreatsCleared = self.dataframe.crearDataframePersonalizado(listaThreatsFilestatusCleared)
        dfThreatsQuarantined = self.dataframe.crearDataframePersonalizado(listaThreatsFilestatusQuarantined)
        #dfThreatsUsuarios = self.dataframe.crearDataframePersonalizado(listaThreatsUsuarios)

        #logo
        if(self.archivo.verificarArchivo(".//Presentacion//logos//" + self.cliente.nombre + ".png")):
            try:
                self.cliente.logo = InlineImage(doc, ".//Presentacion//logos//" + self.cliente.nombre + ".png", width=Mm(50))
            except Exception as e:
                self.log.escribir("Hubo un error en la busqueda de logo en informe: " + str(e), self.cliente.nombre, "Error")
        else: 
            self.cliente.logo = "No hay imagen de logo"
                
        tabla = BLL_Tabla.Tabla()
        # tablas
        try:
            #licencias = tabla.tablaLicencias(listaLicencias)
            # devicesPolicy = tabla.procesarTabla(dfDevices, "policy")
            # devicesZones = tabla.procesarTablaDevicesZonas(dfDevices, "zonename")
            # operativeSystem = tabla.procesarTabla(dfDevices, "operativesystem")
            # versionCylanceSum = tabla.procesarTablaGraficos(dfDevices, "agentversion")
            # devicesActualizar = tabla.procesarTablaDevicesActualizar(dfDevices)
            # politicasNoSeguras = tabla.procesarTablaPoliticasNoSeguras(dfDevices)
            # equiposOffline = tabla.procesarTablaEquiposOffline(dfDevices)
            # accionesPorClasificacion = tabla.procesarTablaAccionesPorTipoMalware(dfClearedEvent)

            topAmenazasQuarantined = tabla.procesarTablaThreats(dfThreatsQuarantined)
            topAmenazasCleared = tabla.procesarTablaThreats(dfThreatsCleared)

            #equiposTopExploits = tabla.procesarTablaTopEventoEquipoUsuario(dfExploits, "devicename", "filename")
            #print(equiposTopExploits)
                # versionesAgenteCy = tabla.procesarTablaGraficos(dfDevices, "agentversion")
                # ubicacionAmenazas = tabla.procesarTablaGraficos(dfThreatsOnly, "drivetype")
                # categoriaAmenazas = tabla.procesarTablaGraficos(dfClearedEvent, "classification")
                # estadoAmenazas = tabla.procesarTablaGraficos(dfClearedEvent, "filestatus")
                # exploitsViolationTypes = tabla.procesarTablaGraficos(dfExploits, "violationtype")
                # exploitsAccionTomada = tabla.procesarTablaGraficos(dfExploits, "action")
                # exploitPorDevices = tabla.procesarTablaGraficos(dfExploits, "devicename")
                # exploitPorUsers = tabla.procesarTablaGraficos(dfExploits, "username")
                # topEquiposAmenazas = tabla.procesarTablaTops(dfThreatsUsuarios, "devicename", "countdevicename")
                # topUsersAmenazas = tabla.procesarTablaTops(dfThreatsUsuarios, "lastloggedinuser", "countlastloggedinuser")
            self.log.escribir("Se generaron las tablas de manera correcta", self.cliente.nombre, "Informar")
        except Exception as e:
            self.log.escribir("Hubo un error en la creacion de tablas: " + str(e), self.cliente.nombre, "Error")

        # try:
        #     directorio = self.archivo.generarDirectorios(".//DATA//GRAFICOS//", self.fechaFin, self.cliente.nombre)
        #     self.log.escribir("Se generaron los directorios de graficos de manera correcta", self.cliente.nombre, "Informar")
        # except Exception as e:
        #     self.log.escribir("Hubo algun error en la creacion de los directorios de graficos: " + str(e), self.cliente.nombre, "Error")


        # grafico = BLL_Grafico.Grafico()
        # try:
        #     histograma = grafico.graficarHistograma(dfThreatsOnly)
        #     histograma.savefig(directorio + "/" + self.cliente.nombre + " - Histograma Amenazas.png", bbox_inches='tight')
        #     if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Histograma Amenazas.png")):
        #         histograma =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Histograma Amenazas.png", width=Mm(150), height=Mm(75))
        #     else:
        #         histograma = "No hay datos"
        # except:
        #     histograma = "No hay datos"

        '''
        #grafico

        try:
            directorio = self.archivo.generarDirectorios(".//DATA//GRAFICOS//", self.fechaFin, self.cliente.nombre)
            self.log.escribir("Se generaron los directorios de graficos de manera correcta", self.cliente.nombre, "Informar")
        except Exception as e:
            self.log.escribir("Hubo algun error en la creacion de los directorios de graficos: " + str(e), self.cliente.nombre, "Error")
        
        grafico = BLL_Grafico.Grafico()

        try:
            ubicacionAmenazas = grafico.graficarBarras(dfThreatsOnly, "drivetype", 10)
            ubicacionAmenazas.savefig(directorio + "/" + self.cliente.nombre + " - Ubicacion Amenazas.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Ubicacion Amenazas.png")): 
                ubicacionAmenazas =  InlineImage(doc,  directorio + "/" + self.cliente.nombre + " - Ubicacion Amenazas.png", width=Mm(150), height=Mm(75))
            else:
                ubicacionAmenazas = "No hay datos sobre la ubicacion de las amenazas"

            versionesAgenteCy = grafico.graficarBarras(dfDevices, "agentversion", 10)
            versionesAgenteCy.savefig(directorio + "/" + self.cliente.nombre + " - Versiones de agente Cylance.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Versiones de agente Cylance.png")):
                versionesAgenteCy =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Versiones de agente Cylance.png", width=Mm(150), height=Mm(75))
            else:
                versionesAgenteCy = "No hay datos sobre versiones de agente Cylance"

            categoriaAmenazas = grafico.graficarBarras(dfClearedEvent, "classification", 10)
            categoriaAmenazas.savefig(directorio + "/" + self.cliente.nombre + " - Categoria Amenazas.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Categoria Amenazas.png")):
                categoriaAmenazas =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Categoria Amenazas.png", width=Mm(150), height=Mm(75))
            else:
                categoriaAmenazas = "No hay datos sobre la categoria de las amenazas"

            estadoAmenazas = grafico.graficarBarras(dfClearedEvent, "filestatus", 10)
            estadoAmenazas.savefig(directorio + "/" + self.cliente.nombre + " - Estado de Amenazas.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Estado de Amenazas.png")):
                estadoAmenazas =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Estado de Amenazas.png", width=Mm(150), height=Mm(75))
            else:
                estadoAmenazas = "No hay datos sobre el estado de las amenazas"

            topEquiposAmenazas = grafico.graficarBarrasContadas(dfThreatsUsuarios, "devicename", 10)
            topEquiposAmenazas.savefig(directorio + "/" + self.cliente.nombre + " - Top Devices con Amenazas.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Top Devices con Amenazas.png")):
                topEquiposAmenazas =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Top Devices con Amenazas.png", width=Mm(150), height=Mm(75))
            else:
                topEquiposAmenazas = "No hay datos sobre las amenazas en los equipos"

            topUsersAmenazas = grafico.graficarBarrasContadas(dfThreatsUsuarios, "lastloggedinuser", 10)
            topUsersAmenazas.savefig(directorio + "/" + self.cliente.nombre + " - Top Users con Amenazas.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Top Users con Amenazas.png")):
                topUsersAmenazas =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Top Users con Amenazas.png", width=Mm(150), height=Mm(75))
            else:
                topUsersAmenazas = "No hay datos sobre los usuarios con mas amenazas"

            exploitsViolationTypes = grafico.graficarBarras(dfExploits, "violationtype", 10)
            exploitsViolationTypes.savefig(directorio + "/" + self.cliente.nombre + " - Exploits Violation types.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Exploits Violation types.png")):
                exploitsViolationTypes =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Exploits Violation types.png", width=Mm(150), height=Mm(75))
            else:
                exploitsViolationTypes = "No hay datos sobre los tipos de violaciones de memoria"

            exploitsAccionTomada = grafico.graficarBarras(dfExploits, "action", 10)
            exploitsAccionTomada.savefig(directorio + "/" + self.cliente.nombre + " - Exploits por accion tomada.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Exploits por accion tomada.png")):
                exploitsAccionTomada =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Exploits por accion tomada.png", width=Mm(150), height=Mm(75))
            else:
                exploitsAccionTomada = "No hay datos sobre accion tomada por cada malware"

            exploitPorDevices = grafico.graficarBarras(dfExploits, "devicename", 10)
            exploitPorDevices.savefig(directorio + "/" + self.cliente.nombre + " - Exploits por Devices.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Exploits por Devices.png")):
                exploitPorDevices =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Exploits por Devices.png", width=Mm(150), height=Mm(75))
            else:
                exploitPorDevices = "No hay datos sobre los exploits por dispositivo"

            exploitPorUsers = grafico.graficarBarras(dfExploits, "username", 10)
            exploitPorUsers.savefig(directorio + "/"+ self.cliente.nombre + " - Exploits por Usuarios.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/"+ self.cliente.nombre + " - Exploits por Usuarios.png")):
                exploitPorUsers =  InlineImage(doc, directorio + "/"+ self.cliente.nombre + " - Exploits por Usuarios.png", width=Mm(150), height=Mm(75))
            else:
                exploitPorUsers = "No hay datos sobre los exploits por usuario"

            histograma = grafico.graficarHistograma(dfThreatsOnly, "filestatus")
            histograma.savefig(directorio + "/" + self.cliente.nombre + " - Histograma Amenazas.png", bbox_inches='tight')
            if(self.archivo.verificarArchivo(directorio + "/" + self.cliente.nombre + " - Histograma Amenazas.png")):
                histograma =  InlineImage(doc, directorio + "/" + self.cliente.nombre + " - Histograma Amenazas.png", width=Mm(150), height=Mm(75))
            else:
                histograma = "No hay datos"

            self.log.escribir("Se generaron los graficos de manera correcta", self.cliente.nombre, "Informar")
        except Exception as e:
            self.log.escribir("Hubo un error en la creacion de graficos: " + str(e), self.cliente.nombre, "Error")

        '''



        context = { 
                        "Logo" : self.cliente.logo,
                        "n_informe" : numeroInforme,
                        "nombre_cliente" : self.cliente.nombre,
                        "date1" : fechaInicioFormat,
                        "date2" : fechaFinFormat,
                        #"licencias": licencias,
                        # "devicesPolicy" : devicesPolicy,
                        # "devicesZones" : devicesZones,
                        # "operativeSystem" : operativeSystem,
                        # "versionesAgenteCy" : versionesAgenteCy,
                        # "versionCylanceSum" : versionCylanceSum,
                        # "devicesActualizar" : devicesActualizar,
                        # "politicasNoSeguras" : politicasNoSeguras,
                        # "equiposOffline" : equiposOffline,
                        # "ubicacionAmenazas" : ubicacionAmenazas,
                        # "categoriaAmenazas" : categoriaAmenazas,
                        #"histograma" : histograma,
                        # "estadoAmenazas" : estadoAmenazas,
                        # "accionesPorClasificacion" : accionesPorClasificacion,
                        # "topEquiposAmenazas" : topEquiposAmenazas,
                        # "topUsersAmenazas" : topUsersAmenazas,
                        "topAmenazasQuarantined" : topAmenazasQuarantined,
                        "topAmenazasCleared" : topAmenazasCleared,
                        # "exploitsViolationTypes" : exploitsViolationTypes,
                        # "exploitsAccionTomada" : exploitsAccionTomada,
                        # "exploitPorDevices" : exploitPorDevices,
                        #"equiposTopExploits" : equiposTopExploits
                        #"exploitPorUsers" : exploitPorUsers,                      
            }



        # definicion de carpetas de informes y entregables csvs

        # if self.tipo == "personalizado":
        #     try:
        #         nombreArchivo = "Informe de Gestion Personalizado - " + self.cliente.nombre
        #         directorioPersonalizado = os.getcwd() + "/DATA/INFORMES/PERSONALIZADO/"

        #         try:
        #             os.stat(directorioPersonalizado)
        #         except:
        #             os.mkdir(directorioPersonalizado)

        #         doc.save(directorioPersonalizado + nombreArchivo + ".docx")
        #     except:
        #         self.log.escribir("Hubo un error en la creacion del informe personalizado", self.cliente.nombre, "Error")


        # directorioInformes declarado al principio 

        directorioCSVsEntregables = directorioInformes + "/CSVS/"
        try:
            os.stat(directorioCSVsEntregables)
        except:
            os.mkdir(directorioCSVsEntregables)

        nombreArchivo = str(self.fechaFin.year) + " - " + str(self.fechaFin.month) + " - " + self.cliente.nombre
        

        # renderizado
        doc.render(context)
        # se crea el directorio del dia para embocar los csv diarios semanales y mensuales
        directorioCSVsEntregablesDia = directorioCSVsEntregables + "/" + str(self.fechaFin.day) + "/"
        try:
            os.stat(directorioCSVsEntregablesDia)
        except:
            os.mkdir(directorioCSVsEntregablesDia)
#                   <-----/----- dataframe a csv -----\----->
        try:
            self.archivo.creacionCSV(dfThreatsOnly, self.cliente, self.tipo, directorioCSVsEntregablesDia, "dfThreatsOnly")
            self.archivo.creacionCSV(dfClearedEvent, self.cliente, self.tipo, directorioCSVsEntregablesDia, "dfClearedEvent")
            self.archivo.creacionCSV(dfExploits, self.cliente, self.tipo, directorioCSVsEntregablesDia, "dfExploits")
            self.archivo.creacionCSV(dfDevices, self.cliente, self.tipo, directorioCSVsEntregablesDia, "dfDevices")
        except Exception as e:
            self.log.escribir("Hubo un error en la creacion de CSV: " + str(e), self.cliente.nombre, "Error")
        # guardado de informes
        try:
            if self.tipo == "diario":
                doc.save(directorioInformes + "/" + str(self.fechaFin.year) + " - " + str(self.fechaFin.month) + " - " + str(self.fechaFin.day) + " - " + self.cliente.nombre + " Diario - Informe de Gestion - CylancePROTECT.docx")                               
                self.log.escribir("Se genero el informe " + self.tipo + " de manera correcta", self.cliente.nombre, "Informar")
            
            elif self.tipo == "semanal":
                doc.save(directorioInformes + "/" + str(self.fechaFin.year) + " - " + str(self.fechaFin.month) + " - " + str(self.fechaFin.day) + " - " + self.cliente.nombre + " Semanal - Informe de Gestion - CylancePROTECT.docx")

                self.log.escribir("Se genero el informe " + self.tipo + " de manera correcta", self.cliente.nombre, "Informar")
            
            elif self.tipo == "mensual":
                doc.save(directorioInformes + "/" + str(self.fechaFin.year) + " - " + str(self.fechaFin.month) + " - " + self.cliente.nombre + " Mensual - Informe de Gestion - CylancePROTECT.docx")
                
                self.log.escribir("Se genero el informe " + self.tipo + " de manera correcta", self.cliente.nombre, "Informar")
        except Exception as e:
            self.log.escribir("Hubo un error en la creacion de informes: " + str(e), self.cliente.nombre, "Error")


    # def generarListaLicencias(self, request, cliente):
    #     response = request.requestZoho(cliente, 'accounts')
    #     return request.matchearClientesZoho(response, cliente)

    def __del__(self):
        gc.collect()

