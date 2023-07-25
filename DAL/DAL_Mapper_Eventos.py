import json
from BLL import BLL_Log
from BLL import BLL_Fecha
from DAL import DAL_Mapper
from DAL import DAL_Conexion
import datetime
import requests




class Mapper_Eventos(DAL_Mapper.Mapper):
    def __init__(self):
        conexion = DAL_Conexion.Conexion()
        self.conexion = conexion
        print("Se creo un objeto Mapper_Eventos")




    def leerEventos(self, cliente, tipoEvento, fechaInicio = "", fechaFin = ""):
        log = BLL_Log.Log()
        self.conexion.conectarDB()
        cur = self.conexion.conexionDB.cursor()

        try:
            if tipoEvento == "Exploits":
                query = """
                SELECT *
                FROM exploitsEntreFechas(%s, %s, %s)
                """
                cur.execute(query, (fechaInicio, fechaFin, cliente.tid))
                
        
            elif tipoEvento == "ThreatsOnly":
                query = """
                SELECT *
                FROM threatsEntreFechas(%s, %s, %s, %s)
                """
                cur.execute(query, (fechaInicio, fechaFin, cliente.tid, tipoEvento))
            
            elif tipoEvento == "Threats":
                query = """
                SELECT *
                FROM threatsEntreFechas2(%s, %s, %s, %s)
                """
                cur.execute(query, (fechaInicio, fechaFin, cliente.tid))
                
                
            
            elif tipoEvento == "ClearedEvent":
                query = """
                SELECT *
                FROM threatsEntreFechas(%s, %s, %s, %s)
                """
                cur.execute(query, (fechaInicio, fechaFin, cliente.tid, tipoEvento))
                

            elif tipoEvento == "Devices":
                query = """
                SELECT *
                FROM devicesEntreFechas(%s, %s, %s)
                """

                cur.execute(query, (fechaInicio, fechaFin.date(), cliente.tid))

            elif tipoEvento == "cantEquiposLic":
                query = """
                SELECT *
                FROM obtener_cant_equipos_licencias(%s, %s)
                """

                cur.execute(query, (cliente.tid, fechaFin.date()))
                

         
    #----------------------Reemplazo Pandas---------------------------------------------
           

            elif tipoEvento == "ThreatsFilestatusCleared":
                try:
                    sql = "select * from contar_threats_devicename(%s, %s, %s, %s)"
                    cur.execute(sql, (cliente.tid, fechaInicio.date() ,fechaFin.date(), "Cleared",))
                    column_names = [desc[0] for desc in cur.description]
                    print(column_names)
                except Exception as e:
                    log.escribir("No se pudo traer los datos de ThreatsFilestatus: " + cliente.nombre + " - " + str(e), "Error")

            elif tipoEvento == "ThreatsFilestatusQuarantined":
                try:
                    sql = "select * from contar_threats_devicename(%s, %s, %s, %s)"
                    cur.execute(sql, (cliente.tid, fechaInicio.date() ,fechaFin.date(), "quarantined",))
                    column_names = [desc[0] for desc in cur.description]
                    print(column_names)
                except Exception as e:
                    log.escribir("No se pudo traer los datos de ThreatsFilestatus: " + cliente.nombre + " - " + str(e), "Error")


            elif tipoEvento == "ThreatsUsuarios":
                query = """
                    SELECT DeviceName, LastLoggedInUser, COUNT(DeviceName) AS CountDevicename, COUNT(LastLoggedInUser) as CountLastLoggedInUser
                    FROM GetLastLoggedInUsers(%s, %s, %s, %s)
                    GROUP BY DeviceName, LastLoggedInUser
                    ORDER BY CountDevicename DESC, CountLastLoggedInUser DESC;
                """
                cur.execute(query, (fechaInicio, fechaFin, fechaFin.date(), cliente.tid))
                

# ----------------------------------Count-------------------------
            elif tipoEvento == "ClearedEventCount":
                    if cliente != "todos":
                        cur.callproc("getClearedEventCount", (fechaInicio, fechaFin, cliente.tid))
                    else:
                        cur.callproc("getClearedEventCount", (fechaInicio, fechaFin))

            elif tipoEvento == "ThreatOnlyCount":
                    if cliente:
                        cur.callproc("getThreatOnlyCount", (fechaInicio, fechaFin, cliente.tid))
                    else:
                        cur.callproc("getThreatOnlyCount", (fechaInicio, fechaFin))
                
            elif tipoEvento == "ExploitCount":
                if cliente != "todos":
                    cur.callproc("getExploitCount", (fechaInicio, fechaFin, cliente.tid))
                else:
                    cur.callproc("getExploitCount", (fechaInicio, fechaFin))

            elif tipoEvento == "DeviceCount":
                if cliente != "todos":
                    cur.callproc("getDeviceCount", (fechaInicio, fechaFin, cliente.tid))
                    column_names = [desc[0] for desc in cur.description]
                else:
                    cur.callproc("getDeviceCount", (fechaInicio, fechaFin))
            
    # ----------------------------------------------------------------------------------------        
            elif tipoEvento == "DevicesSinProt":
                try:
                    sql = "select * from get_devices_sin_proteccion(%s, %s)"
                    cur.execute(sql, (fechaFin.date(), cliente.tid,))
                    column_names = [desc[0] for desc in cur.description]
                    print(column_names)
                except Exception as e:
                    log.escribir("No se pudo traer los datos de Dispositivos sin proteccion: " + cliente.nombre + " - " + str(e), "Error")

            elif tipoEvento == "DevicesSinZonas":
                try:
                    sql = "select * from get_devices_sin_zonas(%s, %s)"
                    cur.execute(sql, (fechaFin.date(), cliente.tid,))
                    column_names = [desc[0] for desc in cur.description]
                    print(column_names)
                except Exception as e:
                    log.escribir("No se pudo traer los datos de Dispositivos sin zonas: " + cliente.nombre + " - " + str(e), "Error")

            elif tipoEvento == "TokensZoho":
                try:
                    sql = "select * from get_tokens(%s)"
                    cur.execute(sql, (cliente.tid,))
                    column_names = [desc[0] for desc in cur.description]
                except Exception as e:
                    log.escribir("No se pudo traer los datos de tokens de Zoho: " + cliente.nombre + " - " + str(e), "Error")

            else:
                log.escribir("Se paso mal el parametro tipoEvento: " + tipoEvento + " - " + cliente.nombre, "Error")
            
            
            column_names = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            cur.close()
            return {
                "rows" : rows,
                "columns" : column_names
            }
        
        except Exception as e:
            log.escribir("No se pudo traer los datos de eventos: " + cliente.nombre + " - " + str(e), "Error")
        
        
    def escribirEventos(self, cliente, df, tipoEventos):
        fecha = BLL_Fecha.Fecha().fechaInicio("diario")
        fecha = fecha.isoformat(sep='T')
        self.conexion.conectarDB()
        cur = self.conexion.conexionDB.cursor()
        # fix apostrofes
        df = df.replace("'", "", regex=True)
        df = df.replace("´", "", regex=True)
        mask = df.isnull()
        df = df.fillna("None")
        df = df.to_json(orient='records')
        df = json.loads(df)
        df = [str(x).replace("'", '"') for x in df]
        df = [str(x).replace("\\\\", '\\') for x in df]
        tid = "'" + cliente.tid + "'"
        fecha = "'" + fecha + "'"
        
        if tipoEventos == "exploit":
            print("exploits mensual")
            f = f'SELECT insertar_exploits({tid}, ARRAY{df}::JSON[]);'
        if tipoEventos == "threat":
            print("threats mensual")
            f = f'SELECT insertar_threats({tid}, ARRAY{df}::JSON[]);'
        if tipoEventos == "device":
            print("devices mensual")
            f = f'SELECT insertar_devices({tid}, {fecha}, ARRAY{df}::JSON[]);'
        
        cur.execute(f)
        self.conexion.conexionDB.commit()
        cur.close()

    def mapperRequestZoho(self, api_endpoint, access_token, params=None):
        url = f'https://www.zohoapis.com/crm/v2/{api_endpoint}'
        print(url)
        headers = {
            'Authorization': f'Zoho-oauthtoken {access_token}'
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def mapperMatchearClientes(self, response, cliente):
        clientes_coincidentes = []

        for account_crm in response['data']:
            print(account_crm['Account_Name'])
            if account_crm['Account_Name'] == cliente.nombre:

                cliente_coincidente = {
                    'id': account_crm['id'],
                    'nombre': account_crm['Account_Name'],
                    'licencias': account_crm['Cantidad_de_Licencias']
                }
                clientes_coincidentes.append(cliente_coincidente)

        return clientes_coincidentes
    

    def mapperInsertarDatosZoho(self, cliente, id_cliente, refresh_token = None, sid = None):
        log = BLL_Log.Log()
        try:
            self.conexion.conectarDB()
            cur = self.conexion.conexionDB.cursor()
            sql = "CALL insertar_datos_zoho(%s, %s, %s, %s)"
            cur.execute(sql, (cliente.tid, refresh_token, sid, id_cliente,))
            self.conexion.conexionDB.commit()
            cur.close()
            log.escribir("Se insertaron datos de Zoho correctamente", cliente.nombre, "Informar")
        except Exception as e:
            log.escribir("No se pudieron insertar los datos de Zoho: " + str(e), cliente.nombre, "Error")
