import aiohttp
import os #Libreria para el uso del sistema
from dotenv import load_dotenv
from .conexion import Conexion

class ClienteVideos:
    def __init__(self, conexion: Conexion):
        self.__conexion = conexion
        self.__url = self.__conexion.getUrl()

    #Buscar videos por id de canal
    async def buscarVideoID(self, id_video:int):
        url = f"{self.__url}/videos/videosCanal"
        await self.__conexion.conexion( )
        param = {"id": id_video}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=param) as resp:
                resp.raise_for_status()
                datos=await resp.json()
                if datos:
                    return  datos
                return None
            
    #Buscar videos por nombre
    async def buscarVideoNombre(self, nombre: str):
        url = f"{self.__url}/videos/buscarVideoNombre/{nombre}"
        await self.__conexion.conexion( )
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                resp.raise_for_status( )
                datos= await resp.json()
                if datos:
                    return datos
                return None

    #Buscar videos por url
    async def buscarVideoUrl(self, url_video: str):
        url = f"{self.__url}/videos/buscarVideoUrl"
        await self.__conexion.conexion( )
        param = {"url": url_video.strip()}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=param) as resp:
                resp.raise_for_status( )
                datos= await resp.json()
                if datos:
                    return datos
                return None

    #mostrar todos los videos
    async def mostrarVideos(self):
        url = f"{self.__url}/videos/mostrarVideos/"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                return None