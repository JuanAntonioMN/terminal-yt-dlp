import aiohttp
from dotenv import load_dotenv #Consumir variable ENV
import os #Libreria para el uso del sistema

class Conexion:
    def __init__(self):
        load_dotenv( ) #mandamos a llamar las variables
        
        self.__url=os.getenv("URL")
        
        
    async def conexion(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.__url, timeout=5) as response:
                    response.raise_for_status( )  # Lanza error si status code no es 2xx
                    return await response.text( )  # o .json() si esperas JSON
      
        except aiohttp.ClientResponseError as errh: #Errores de estado de la API 4xx o 5xx
            print("Error HTTP:", errh)

        except aiohttp.ClientConnectionError as errc: #Error de conexión con la API
            print("Error de conexión.",errc)

        except aiohttp.ClientTimeout as errt: #Error de tiempo de respuesta
            print("Error tiempo de espera agotado al intentar conectar con la API.")

        except aiohttp.ClientError  as err: #Ocurrio otro error
            print("Ocurrió un error inesperado:", err)
        

    def getUrl(self):
        return self.__url
    