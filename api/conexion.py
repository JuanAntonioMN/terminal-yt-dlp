import aiohttp
from dotenv import load_dotenv #Consumir variable ENV
import os #Libreria para el uso del sistema
from rich.console import Console
class Conexion:
    def __init__(self):
        load_dotenv( ) #mandamos a llamar las variables
        self.__url=os.getenv("URL")
        self.__console=Console( )
        
        
    async def conexion(self):
        try:
            async with aiohttp.ClientSession( ) as session:
                async with session.get(self.__url, timeout=5) as response:
                    response.raise_for_status( )  # Lanza error si status code no es 2xx
                    return await response.text( )  # o .json() si esperas JSON
      
        except aiohttp.ClientResponseError: #Errores de estado de la API 4xx o 5xx
            self.__console.print("\n[bold red]Error HTTP[/bold red]")

        except aiohttp.ClientConnectionError: #Error de conexión con la API
            self.__console.print("\n[bold red]Error de conexión al servidor.[/bold red]")

        except aiohttp.ClientTimeout: #Error de tiempo de respuesta
            self.__console.print("\n[bold red]Error tiempo de espera agotado al intentar conectar con la API.[/bold red]")

        except aiohttp.ClientError: #Ocurrio otro error
            self.__console.print("\n[bold yellow]Ocurrió un error inesperado[/bold yellow]")
        

    def getUrl(self):
        return self.__url
    