from .conexion import Conexion
import aiohttp
import asyncio
class Descargar:
    
    def __init__(self,conexion:Conexion):
        self.__conexion=conexion
        self.__url=conexion.getUrl( )
        
    #Descargamos un Video, PlayList, Canal
    async def descargarVideo(self,url): #Valida la url 
            await self.__conexion.conexion( )
            try:
               
               async with aiohttp.ClientSession( ) as session:
                async with session.get(f"{self.__url}/descargas/url", params={"url": url}) as resp:
                    resp.raise_for_status( )
                    datos = await resp.json( )
                return datos
            except aiohttp.ClientError as e:
                return None
      
                        


    
    