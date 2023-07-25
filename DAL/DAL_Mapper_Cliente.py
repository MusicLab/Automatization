import json
from BLL import BLL_Log
from BLL import BLL_Fecha
from DAL import DAL_Mapper
from DAL import DAL_Conexion
import gc


class Mapper_Cliente(DAL_Mapper.Mapper):

    def __init__(self):
        conexion = DAL_Conexion.Conexion()
        self.conexion = conexion
        print("Se creo un objeto Mapper_Cliente")

    
    def mapperLeerClientesDB(self):
        log = BLL_Log.Log()
        self.conexion = DAL_Conexion.Conexion()
        try:
            self.conexion.conectarDB()
            cur = self.conexion.conexionDB.cursor()
            cur.execute("SELECT * FROM clientes")
            rows = cur.fetchall()
            cur.close()
            self.conexion.desconectarDB()
            return rows
        except Exception as e:
            log.escribir("No se pudo leer los clientes en la DB" + str(e), "Error")

    def mapperLeerClienteDBEspecifico(self, nombre):
        log = BLL_Log.Log()
        self.conexion = DAL_Conexion.Conexion()
        try:
            self.conexion.conectarDB()
            cur = self.conexion.conexionDB.cursor()
            cur.execute("SELECT * FROM clientes WHERE nombre_cliente = %s", (nombre,))
            rows = cur.fetchall()
            cur.close()
            self.conexion.desconectarDB()
            return rows
        except Exception as e:
            log.escribir("No se pudo leer los clientes en la DB" + str(e), "Error")

    
    def mapperAgregarClienteDB(self, nombre, region, token, tid, aid, sid, logo, periodicidad, licencias, tipoProducto):
        self.conexion = DAL_Conexion.Conexion()
        self.conexion.conectarDB()
        log = BLL_Log.Log()
        datos = (tid, nombre, region, token, aid, sid, logo, periodicidad, licencias, tipoProducto)
        try:
            query = "INSERT INTO clientes (tid, nombre_cliente, region, token, aid, sid, logo, periodicidad, licencias, tipo_producto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cur = self.conexion.conexionDB.cursor()
            cur.execute(query, datos)
            self.conexion.conexionDB.commit()
            cur.close()
            self.conexion.desconectarDB()
            log.escribir("Se agrego cliente: " + nombre, "Informar")
        except Exception as e:
            log.escribir("No se pudo agregar a la BD el cliente: " + nombre, "Error")

    def mapperAgregar(self, nombre, region, token, tid, aid, sid, logo, periodicidad):
        datos = {"cliente": nombre, "region": region, "token": token, "tenantID": tid, "appID": aid, "secretID": sid, "logo": logo, "periodicidad": periodicidad}

        with open(".//DATA//CLIENTES//Tokens.json", "r") as archivo:
            lines = json.load(archivo)
            lines.append(datos)
        with open(".//DATA//CLIENTES//Tokens.json", 'w') as f:
            json.dump(lines, f, indent=4, separators=(',',': '))

        fecha = BLL_Fecha.Fecha()
        log = BLL_Log.Log()
        log.escribir("Se agrego cliente: " + nombre, "Informar")



    def mapperModificar(self, clienteAModificar, nombre, region, token, tid, aid, sid, logo, periodicidad):
        with open(".//DATA//CLIENTES//Tokens.json", "r") as archivo:
            lines = json.load(archivo)
            
        with open(".//DATA//CLIENTES//Tokens.json", 'w') as f:
            for line in lines:
                if line["cliente"] == clienteAModificar:
                    line["cliente"] = nombre
                    line["region"] = region
                    line["token"] = token
                    line["tenantID"] = tid
                    line["appID"] = aid
                    line["secretID"] = sid
                    line["logo"] = logo
                    line["periodicidad"] = periodicidad
                    break
            json.dump(lines, f, indent=4, separators=(',',': '))

        fecha = BLL_Fecha.Fecha()
        log = BLL_Log.Log()
        log.escribir("Se modifico cliente: " + nombre, "Informar")


    def mapperModificarClienteDB(self, nombre, region, token, tid, aid, sid, logo, periodicidad, licencias, tipoProducto):
        fecha = BLL_Fecha.Fecha()
        log = BLL_Log.Log()
        #log.escribir("Se Modif cliente: " + nombre, "Informar")
        try:
            self.conexion.conectarDB()
            cur = self.conexion.conexionDB.cursor()
            cur.callproc('actualizarcliente', {
                                                "cliente_id": tid,
                                                "nuevo_nombre": nombre,
                                                "nueva_region": region,
                                                "nuevo_token": token, 
                                                "nuevo_aid": aid,
                                                "nuevo_sid": sid,
                                                "nuevo_logo": logo,
                                                "nueva_periodicidad": periodicidad,
                                                "nueva_cant_licencias": licencias,
                                                "nuevo_tipo_producto": tipoProducto
                                            })
            self.conexion.conexionDB.commit()
            cur.close()
            self.conexion.desconectarDB()
        except Exception as e:
            log.escribir("No se pudo modificar a la BD el cliente " + nombre + ": " + + str(e), "Error")

    def mapperBorrar(self, nombre):
        with open(".//DATA//CLIENTES//Tokens.json", "r") as archivo:
            lines = json.load(archivo)

        with open(".//DATA//CLIENTES//Tokens.json", 'w') as f:
            for line in lines:
                if line["cliente"] == nombre:
                    lines.remove(line)
            json.dump(lines, f, indent=4, separators=(',',': '))

        BLL_Log.Log().escribir("Se borro cliente: " + nombre, "Informar")

    def mapperBorrarClienteDB(self, tid):

        log = BLL_Log.Log()
        try:
            self.conexion.conectarDB()
            cur = self.conexion.conexionDB.cursor()
            f =  tid
            sql = "CALL eliminar_datos(%s)"
            cur.execute(sql, (f,))
            self.conexion.conexionDB.commit()
            cur.close()
            log.escribir("Se borro cliente con el tid: " + tid, "Informar")
        except Exception as e:
            log.escribir("No se pudo borrar cliente con el tid: " + tid + str(e), "Error")

    def mapperLeerClientes(self):
        with open(".//DATA//CLIENTES//Tokens.json", "r") as archivo:
            clientes = json.load(archivo)

        return clientes

    def mapperModificarSoloLogo(self, clienteAModificar, logo):
        with open(".//DATA//CLIENTES//Tokens.json", "r") as archivo:
            lines = json.load(archivo)
            
        with open(".//DATA//CLIENTES//Tokens.json", 'w') as f:
            for line in lines:
                if line["cliente"] == clienteAModificar:
                    line["logo"] = logo
                    break
            json.dump(lines, f, indent=4, separators=(',',': '))

    def __del__(self):
        gc.collect()

