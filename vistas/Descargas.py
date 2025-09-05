from api.conexion import Conexion
from api.Descargar import Descargar
class Descargas:
    def __init__(self):
        self.__conexion=Conexion( )
        self.__descargar=Descargar(self.__conexion)
    
    async def descargar(self,url):
       datos=await self.__descargar.descargarVideo(url)
       if datos:
          print(datos)
        