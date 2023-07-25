from BLL import BE_Mail
from DAL import DAL_Mapper_Mail

class Mail(object):

    ###metodo agregar que reciba como parametro una variable de tipo string llamada "mail" y que se la pase por parametro a una funcion mapperAgregar, de la clase Mapper_Mail, que se encuentra en el archivo DAL_Mapper_Mail.py###
    def Agregar(self, mail):
        try:
            mapper = DAL_Mapper_Mail.Mapper_Mail()
            mapper.mapperAgregar(mail)
        except:
            raise
    ###Meto Modificar###

    def Modificar(self, mail):
        try:
            mail.Modificar()
        except:
            raise
    
    ###Meto Borrar###

    def Borrar(self, mail):
        try:
            mail.Borrar()
        except:
            raise

        