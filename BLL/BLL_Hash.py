from DAL import DAL_Mapper_Hash
from BE import BE_Hash

class Hash(object):

    mapper = DAL_Mapper_Hash.Mapper_Hash()

    def __init__(self, nombreArchivo = "", ruta = "", descripcion = ""):
        BE_Hash.Hash.setNombre(self, nombreArchivo)
        BE_Hash.Hash.setRuta(self, ruta)
        BE_Hash.Hash.setTipo(self, "SHA256")
        BE_Hash.Hash.setDescripcion(self, descripcion)

    def cargar(self, cliente, listType, razon, hash, categoria = "None"):
        self.mapper.mapperAgregar(cliente, listType, razon, hash, categoria)

    def cargarMultiHashes(self, listaClientes, listaHashes, listtype, razon, categoria):
        codigo = self.mapper.mapperAgregarHashes(listaClientes, listaHashes, listtype, razon, categoria)
        return codigo
        

    def eliminar(self, cliente, listType, hash):
        codigo = self.mapper.mapperEliminarHash(cliente, listType, hash)
        return codigo

#    def modificar(self, hash, hashNuevo):
#        DAL_Mapper_Hash.Mapper_Hash.mapperModificarHash(self.ruta, hash, hashNuevo)
#
#    def comparar(self, hash):
#        DAL_Mapper_Hash.Mapper_Hash.mapperCompararHash(self.ruta, hash)


