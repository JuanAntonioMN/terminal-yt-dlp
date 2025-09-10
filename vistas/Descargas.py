from api.conexion import Conexion
from api.Descargar import Descargar
import json
import os
class Descargas:
    def __init__(self):
        self.__conexion=Conexion( )
        self.__descargar=Descargar(self.__conexion)
    
    async def descargarUrl(self,url):
       datos=await self.__descargar.descargarURL(url)
       if datos:
          print(datos)
    
    async def descargarArchivo(self,ruta):
       try:
        
        if os.path.exists(ruta) and os.path.isfile(ruta):
           if ruta.lower().endswith(".txt"): 
                with open(ruta,"r") as datos:
                    enlace=datos.readlines( )
                listaEnlaces=[linea.strip( ) for linea in enlace if linea.strip( ) ]
                jsonEnlaces=json.dumps(listaEnlaces)
                await self.__descargar.descargarArchivo(jsonEnlaces)
           else:
               print("El archivo debe ser de tipo txt")
        else:
            print ("Error con la ruta del archivo")
       except Exception as e:
            return e
    