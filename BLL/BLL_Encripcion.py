from BE import BE_Encripcion
from cryptography.fernet import Fernet
import json
import base64


class Encripcion(object):


    def __init__(self):
        BE_Encripcion.Encripcion.setKey(self, Fernet.generate_key())
        BE_Encripcion.Encripcion.setListaConexion(self, [])
        BE_Encripcion.Encripcion.setEstado(self, False)
        BE_Encripcion.Encripcion.setEstadoArchivo(self, False)

    def asignarAtributos(self, db, user, password, host, port):
        self.listaConexion.append(db)
        self.listaConexion.append(user)
        self.listaConexion.append(password)
        self.listaConexion.append(host)
        self.listaConexion.append(port)

    def establecerKeyPersonalizada(self):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        huahuna = "083c74c1b8a97e0f397c34ad9df97ea193ff69ff3d878dd2d0503eb0e012130e"
        anuhauh = fernet.encrypt(huahuna.encode())
        return base64.urlsafe_b64encode(anuhauh)

    def encriptarDatosConexion(self):
        if(self.estado == False):
            fernet = fernet = Fernet(self.key)
    
            self.listaConexion[0] = fernet.encrypt(self.listaConexion[0].encode())
            self.listaConexion[1] = fernet.encrypt(self.listaConexion[1].encode())
            self.listaConexion[2] = fernet.encrypt(self.listaConexion[2].encode())
            self.listaConexion[3] = fernet.encrypt(self.listaConexion[3].encode())
            self.listaConexion[4] = fernet.encrypt(self.listaConexion[4].encode())
    
            self.estado = True
        print("termino el metodo encriptarDatosConexion")

    def desencriptarDatosConexion(self):
        if(self.estado == True):
            fernet = fernet = Fernet(self.key)
    
            self.listaConexion[0] = fernet.decrypt(self.listaConexion[0]).decode()
            self.listaConexion[1] = fernet.decrypt(self.listaConexion[1]).decode()
            self.listaConexion[2] = fernet.decrypt(self.listaConexion[2]).decode()
            self.listaConexion[3] = fernet.decrypt(self.listaConexion[3]).decode()
            self.listaConexion[4] = fernet.decrypt(self.listaConexion[4]).decode()
    
            self.estado = False
        print("termino el metodo desencriptarDatosConexion")

    def encriptarDatosArchivo(self):

        if(self.estadoArchivo == False):
            key = self.establecerKeyPersonalizada()
            fernet = Fernet(key)

            with open(".//DATA//CONFIG//Conexion.json", 'r') as file:
                datos = json.load(file)

            self.listaConexion.append(datos["database"])
            self.listaConexion.append(datos["user"])
            self.listaConexion.append(datos["password"])
            self.listaConexion.append(datos["host"])
            self.listaConexion.append(datos["port"])

            db = fernet.encrypt(datos["database"].encode())
            user = fernet.encrypt(datos["user"].encode())
            password = fernet.encrypt(datos["password"].encode())
            host = fernet.encrypt(datos["host"].encode())
            port = fernet.encrypt(datos["port"].encode())

            datos["database"] = str(db)
            datos["user"] = str(user)
            datos["password"] = str(password)
            datos["host"] = str(host)
            datos["port"] = str(port)
            datos["estado"] = 1

            with open(".//DATA//CONFIG//Conexion.json", 'w') as f:
                json.dump(datos, f, indent=4, separators=(',',': '))

            self.estadoArchivo = True
            
    def desencriptarDatosArchivo(self):

        if(self.estadoArchivo == True):
            key = self.establecerKeyPersonalizada()
            fernet = Fernet(key)

            with open(".//DATA//CONFIG//Conexion.json", 'r') as file:
                datos = json.load(file)


            db = fernet.decrypt(datos["database"]).decode()
            user = fernet.decrypt(datos["user"]).decode()
            password = fernet.decrypt(datos["password"]).decode()
            host = fernet.decrypt(datos["host"]).decode()
            port = fernet.decrypt(datos["port"]).decode()

            print(db)

            datos["database"] = db
            datos["user"] = user
            datos["password"] = password
            datos["host"] = host
            datos["port"] = port
            datos["estado"] = 0

            with open(".//DATA//CONFIG//Conexion.json", 'w') as f:
                json.dump(datos, f, indent=4, separators=(',',': '))

            self.estadoArchivo = False
