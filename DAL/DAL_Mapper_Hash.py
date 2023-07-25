from DAL import DAL_Mapper
from DAL import DAL_Conexion
from BLL import BLL_Log

class Mapper_Hash(DAL_Mapper.Mapper):

    log = BLL_Log.Log()

    def __init__(self):
        conexion = DAL_Conexion.Conexion()
        self.conexion = conexion
        print("Se creo un objeto Mapper_Hash")

    def mapperAgregar(self, cliente, listType, razon, hash, categoria):
        print(hash)
        try:
            conexion = DAL_Conexion.Conexion() 
            API = conexion.conectar(cliente)

            post = API.add_to_global_list(listType, razon, hash, categoria)
            print("Post: {}".format(post.status_code))

            if post.status_code == 200:
                self.log.escribir("Se agrego un hash correctamente", cliente.nombre, "informar")
            else:
                self.log.escribir("Hubo un problema con la carga de hashes:" + str(post.status_code), cliente.nombre, "error")

            return post.status_code
        except Exception as e:
            self.log.escribir("Hubo un problema con la carga de hashes: " + str(e), "General", "error")
            return post.status_code

    def mapperAgregarHashes(self, listaClientes, listaHashes, listtype, razon, categoria):
        try:
            for cliente in listaClientes:
                    for sha in listaHashes:
                        if len(listaHashes) == 1:
                            print(sha)
                            codigo = self.mapperAgregar(cliente, listtype, razon, sha, categoria)
                        else:
                            codigo = self.mapperAgregar(cliente, listtype, razon, sha[0], categoria)

            self.log.escribir("Se agregaron " + str(len(listaHashes)) + " hashes con la multi carga correctamente", "General", "informar") 
            return codigo           
        except Exception as e:
            self.log.escribir("Hubo un problema con la multi carga de " + str(len(listaHashes)) + " hashes: " + str(e), "General", "error")
            return codigo  

    def mapperEliminarHash(self, cliente, listType, hash):

        try:
            conexion = DAL_Conexion.Conexion() 
            API = conexion.conectar(cliente)

            post = API.delete_from_global_list(listType, hash)
            print("Post: {}".format(post.status_code))

            if post.status_code == 200:
                self.log.escribir("Se elimino un hash correctamente", cliente.nombre, "informar")
            else:
                self.log.escribir("Hubo un problema con la eliminacion de hashes: " + str(post.status_code), cliente.nombre, "error")
        
            return post.status_code
        except Exception as e:
            self.log.escribir("Hubo un problema con la eliminacion de hashes: " + str(e), "General", "error")

