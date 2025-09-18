import aiohttp
from .conexion import Conexion

class ClienteCanal:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__url = conexion.getUrl( )

    async def mostrarCanales(self):
        await self.__conexion.conexion( )
        


        async with aiohttp.ClientSession( ) as session:
            async with session.get(f"{self.__url}/canal/canales") as resp:
                if resp.status == 200:
                    return await resp.json( )
                return None

    async def buscarPorNombre(self, Nombre_Canal: str):
        async with aiohttp.ClientSession( ) as session:
            async with session.get(f"{self.__url}/canal/buscarCanalNombre/{Nombre_Canal}") as resp:#validaar que al url este bien estructurada
                if resp.status == 200:
                    return await resp.json()
                return None

    async def buscarPorUrl(self, url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.__url}/canal/buscarCanalUrl", params={"Url_Canal": url}) as resp:
                if resp.status == 200:
                    return await resp.json()
                return None

    async def cantidadVideos(self, Nombre_Canal: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.__url}/canal/CantidadVideos/{Nombre_Canal}") as resp:
                if resp.status == 200:
                    return await resp.json()
                return None

