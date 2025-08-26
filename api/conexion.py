import requests #Libreria para consumir API
from dotenv import load_dotenv #Consumir variable ENV
import os #Libreria para el uso del sistema

class Conexion:
    def __init__(self):
        load_dotenv( ) #mandamos a llamar las variables
        self.__url=os.getenv("URL")
        
    def conexion(self):
        try:
            response=requests.get(self.__url,timeout=5) #Inicializamos los errores
            response.raise_for_status( )  # Lanza error si el status code no es 2xx
            return True
        except requests.exceptions.HTTPError as errh: #Errores de estado de la API 4xx o 5xx
            print("Error HTTP:", errh)

        except requests.exceptions.ConnectionError as errc: #Error de conexión con la API
            print("Error de conexión.",errc)

        except requests.exceptions.Timeout as errt: #Error de tiempo de respuesta
            print("Error tiempo de espera agotado al intentar conectar con la API.")

        except requests.exceptions.RequestException as err: #Ocurrio otro error
            print("Ocurrió un error inesperado:", err)
        return False

    def getUrl(self):
        return self.__url
    