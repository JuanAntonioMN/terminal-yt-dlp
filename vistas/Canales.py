from api.conexion import Conexion

from api.ClienteCanal import ClienteCanal

class Canales:
    def __init__(self):
        self.__conexion = Conexion()
        self.__cliente = ClienteCanal(self.__conexion)

    async def canales(self):
        canales = await self.__cliente.mostrarCanales()
        return canales

    async def buscarNombre(self, nombre: str):
        canal = await self.__cliente.buscarPorNombre(nombre)
        return canal

    async def buscarUrl(self, url: str):
        canal = await self.__cliente.buscarPorUrl(url)
        return canal
            
    async def cantidadVideos(self, nombre: str):
        canal = await self.__cliente.cantidadVideos(nombre)
        if canal:
            print(canal)
        else:
            print("No encontrado")
