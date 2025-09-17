from api.conexion import Conexion
from api.ClienteVideos import ClienteVideos

class Videos:
   def __init__(self):
        conexion = Conexion( )
        self.__cliente = ClienteVideos(conexion)
        
   async def buscarVideoNombre(self, nombre: str):
      datos = await self.__cliente.buscarVideoNombre(nombre)
      if datos:
         print(datos)    
      else:
         print("No se encontraron videos con ese nombre.")
                
   async def buscarVideoID(self, id:int):
      datos = await self.__cliente.buscarVideoID(id)
      if datos:
            print(datos)
      else:
            print("No se encontraron videos para ese canal.")
          
   async def buscarVideoURL(self, url: str):
      datos = await self.__cliente.buscarVideoUrl(url)
      if datos:
            print(datos)
      else:
            print("No se encontraron videos con esa URL.")
          
   async def mostrarVideos(self):
      datos = await self.__cliente.mostrarVideos()
      if datos:
            print(datos)    
      else:
            print("No hay videos en la base de datos.")