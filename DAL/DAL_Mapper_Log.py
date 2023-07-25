
class Mapper_Log():

    def __init__(self):
        print("Se creo un objeto Mapper_Log")

    def mapperLog(self, archivo, datos, cliente, tipo):
        archivo.escribirLogTXT(tipo + " - " + datos, cliente)




