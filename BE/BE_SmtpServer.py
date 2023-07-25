class SmtpServer(object):
    __server = ""
    __port = ""
    __email = ""
    __password = ""
    __conexionSmtp = ""

    def setServer(self, server):
        self.server = server
    
    def getServer(self):
        return self.server

    def setPort(self, port):
        self.port = port
    
    def getPort(self):
        return self.port
    

    def setMail(self, mail):
        self.mail = mail
    
    def getMail(self):
        return self.mail
    
    def setPassword(self, password):
        self.password = password
    
    def getPassword(self):
        return self.password
    
    def setConexionSmtp(self, conexionSmtp):
        self.conexionSmtp = conexionSmtp
    
    def getConexionSmtp(self):
        return self.conexionSmtp