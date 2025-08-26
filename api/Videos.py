import requests #Libreria para consumir API
from conexion import Conexion

class Videos:
    def __init__(self,conexion:Conexion):
        self.__conexion=conexion
        self.__url=conexion.getUrl( )
        
        
    #Obtenemos todos los videos desde nuestra API
    def videos(self):
        if self.__conexion.conexion( ):
            try:
                response = requests.get(
                    f"{self.__url}/videos"
                )
                response.raise_for_status()
                return response.json( )
            except requests.exceptions.RequestException as e:
                print("Error al obtener los videos:", e)
        else:
            print("Ocurrio un error")
            
        return None
    

    #Buscamos un video por su id
    def buscarId(self,id):
        pass
    
    #Buscamos un video por su nombre
    def buscarNombre(self,nombre):
        pass
    
    #Buscamos un video por su url
    def buscarUrl(self,url):
        pass