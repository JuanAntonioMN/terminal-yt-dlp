import requests #Libreria para consumir API
from conexion import Conexion

class Descargar:
    
    def __init__(self,conexion:Conexion):
        self.__conexion=conexion
        self.__url=conexion.getUrl( )
        
    #Descargamos un Video, PlayList, Canal
    def descargarVideo(self,url): #Valida la url 
        if self.__conexion.conexion( ):
            try:
                response = requests.post(
                    f"{self.__url}/videos", 
                    json={
                        "url": url
                        }
                )
                response.raise_for_status( )
                return response.json( )
            except requests.exceptions.RequestException as e:
                print("Error con la url", e)
        else:
            print("Ocurrio un error")
                            
        return None

    def decargarArchivo(self,archivo):
        pass
    
    
    
    