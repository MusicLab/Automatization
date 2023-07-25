class Conexion(object):
    
    __conexion = False
    __conexionDB = ""
    __encripcion = ""
    __database = "" 
    __user = ""
    __password = ""
    __host = ""
    __port = "" 


    def getConexion(self):
        return self.conexion

    def setConexion(self, conexion):
        self.conexion = conexion

    def getConexionDB(self):
        return self.conexionDB

    def setConexionDB(self, conexionDB):
        self.conexionDB = conexionDB  

    def getEncripcion(self):
        return self.encripcion
    
    def setEncripcion(self, encripcion):
        self.encripcion = encripcion

    def getDatabase(self):
        return self.database
    
    def setDatabase(self, database):
        self.database = database

    def getUser(self):
        return self.user
    
    def setUser(self, user):
        self.user = user

    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password

    def getHost(self):
        return self.host
    
    def setHost(self, host):
        self.host = host

    def getPort(self):
        return self.port
    
    def setPort(self, port):
        self.port = port


