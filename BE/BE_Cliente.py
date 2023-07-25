class Cliente(object):
    __nombre = ""
    __region = ""
    __token = ""
    __tid = ""
    __aid = ""
    __sid = ""
    __logo = ""
    __periodicidad = ""
    __licencias = ""
    __tipoProducto = ""

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
       
    def getRegion(self):
        return self.region

    def setRegion(self, region):
        self.region = region 

    def getToken(self):
        return self.token

    def setToken(self, token):
        self.token = token 

    def getTid(self):
        return self.tid

    def setTid(self, tid):
        self.tid = tid 

    def getAid(self):
        return self.aid

    def setAid(self, aid):
        self.aid = aid 

    def getSid(self):
        return self.sid

    def setSid(self, sid):
        self.sid = sid 

    def getLogo(self):
        return self.logo

    def setLogo(self, logo):
        self.logo = logo 

    def getPeriodicidad(self):
        return self.periodicidad

    def setPeriodicidad(self, periodicidad):
        self.periodicidad = periodicidad

    def getLicencias(self):
        return self.licencias
    
    def setLicencias(self, licencias):
        self.licencias = licencias

    def getTipoProducto(self):
        return self.tipoProducto
    
    def setTipoProducto(self, tipoProducto):
        self.tipoProducto = tipoProducto






