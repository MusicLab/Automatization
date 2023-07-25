import json
import gc
from BE import BE_Cliente
from DAL import DAL_Mapper_Cliente

class Cliente(object):
    
    def __init__(self, nombre  = "", region  = "", token  = "", tid  = "", aid  = "", sid  = "", logo = "", periodicidad = "", licencias = "", tipoPorducto = ""):
        BE_Cliente.Cliente.setNombre(self, nombre)
        BE_Cliente.Cliente.setRegion(self, region)
        BE_Cliente.Cliente.setToken(self, token)
        BE_Cliente.Cliente.setTid(self, tid)
        BE_Cliente.Cliente.setAid(self, aid)
        BE_Cliente.Cliente.setSid(self, sid)
        BE_Cliente.Cliente.setLogo(self, logo)
        BE_Cliente.Cliente.setPeriodicidad(self, periodicidad)
        BE_Cliente.Cliente.setLicencias(self, licencias)
        BE_Cliente.Cliente.setTipoProducto(self, tipoPorducto)

    def crearListaDB(self):
        listaClientes = []
        for linea in DAL_Mapper_Cliente.Mapper_Cliente().mapperLeerClientesDB():
            cliente = Cliente(linea[1], linea[2], linea[3], linea[0], linea[4], linea[5], linea[6], linea[7], linea[8], linea[9])
            listaClientes.append(cliente) 
        return listaClientes
    
    def leerClientesDB(self):        
        return DAL_Mapper_Cliente.Mapper_Cliente().mapperLeerClientesDB()   
    

    def agregarDB(self, nombre, region, token, tid, aid, sid, logo, periodicidad, licencias, tipoProducto):
        DAL_Mapper_Cliente.Mapper_Cliente().mapperAgregarClienteDB(nombre, region, token, tid, aid, sid, logo, periodicidad, licencias, tipoProducto)

    def modificarDB(self, nombre, region, token, tid, aid, sid, logo, periodicidad, licencias, tipoProducto = ""):
        DAL_Mapper_Cliente.Mapper_Cliente().mapperModificarClienteDB(nombre, region, token, tid, aid, sid, logo, periodicidad, licencias, tipoProducto)

    def borrarDB(self, tid):
        DAL_Mapper_Cliente.Mapper_Cliente().mapperBorrarClienteDB(tid)


    def crearListaVieja(self):
        lista = []
        with open (".//DATA//CLIENTES//Tokens.json", "r", encoding='utf-8') as file:
            listaClientes = json.load(file)
            for linea in listaClientes:
                cliente = Cliente(linea["cliente"], linea["region"], linea["token"], linea["tenantID"], linea["appID"], linea["secretID"], linea["logo"], linea["periodicidad"])
                lista.append(cliente) 
        return lista
    
    def agregar(self, nombre, region, token, tid, aid, sid, logo, periodicidad):
        DAL_Mapper_Cliente.Mapper_Cliente().mapperAgregar(nombre, region, token, tid, aid, sid, logo, periodicidad)

    def modificar(self, clienteAModificar, nombre, region, token, tid, aid, sid, logo, periodicidad):
        DAL_Mapper_Cliente.Mapper_Cliente().mapperModificar(clienteAModificar, nombre, region, token, tid, aid, sid, logo, periodicidad)

    def borrar(self, cliente):
        DAL_Mapper_Cliente.Mapper_Cliente().mapperBorrar(cliente)

    def leerClientes(self):
        return DAL_Mapper_Cliente.Mapper_Cliente().mapperLeerClientes()

    def actualizarLogo(self, clienteAModificar,logo):
        DAL_Mapper_Cliente.Mapper_Cliente().mapperModificarSoloLogo(clienteAModificar, logo)

    def leerClienteEspecifico(self, nombre):
        datos = DAL_Mapper_Cliente.Mapper_Cliente().mapperLeerClienteDBEspecifico(nombre)
        cliente = Cliente(datos[0][1], datos[0][2], datos[0][3], datos[0][0], datos[0][4], datos[0][5], datos[0][6], datos[0][7], datos[0][8], datos[0][9])
        return cliente
     
    
    def convertirListaClientesADict(self, listaClientes):
        dictClientes = []
        for linea in listaClientes:
            cliente = Cliente(linea[1], linea[2], linea[3], linea[0], linea[4], linea[5], linea[6], linea[7], linea[8], linea[9])
            dictClientes.append(cliente.__dict__)
        
        return dictClientes


    def __del__(self):
        gc.collect()
