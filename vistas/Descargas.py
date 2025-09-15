from api.conexion import Conexion
from api.Descargar import Descargar
import json
import os
from rich.progress import track
import time
from rich.console import Console
import asyncio
from rich.progress import Progress

console = Console()


class Descargas:
    def __init__(self):
        self.__conexion=Conexion( )
        self.__descargar=Descargar(self.__conexion)
    
    async def descargarUrl(self, url):
        # Creamos la barra
        with Progress( ) as progress:
            task = progress.add_task("[cyan]Descargando...", total=5)

            # Paso 1: validar URL
            progress.update(task, advance=1, description="Validando URL")
            await asyncio.sleep(1)

            # Paso 2: extrayendo metadatos
            progress.update(task, advance=1, description="Extrayendo metadatos")
            await asyncio.sleep(1)

            # Paso 3: descargar datos (aquí se hace la petición real 👇)
            progress.update(task, advance=1, description="Descargando datos")
            datos = await self.__descargar.descargarURL(url)
            estado = datos.get("Estado")
            if estado in (304, 404, 409, 500):
               print(f"[Error] {datos.get('Mensaje')}")
               progress.stop( )
               
            # Paso 4: guardar
            progress.update(task, advance=1, description="Guardando información")
            await asyncio.sleep(1)

            # Paso 5: finalizar
            progress.update(task, advance=1, description="Finalizando")
            await asyncio.sleep(1)
            if estado == 200:
                print(f"[OK] {datos.get('Mensaje')}")
                print(datos.get("Video"))
            else:
                print(f"[Warning] Error inesperado")

       
    async def descargarArchivo(self,ruta):
       try:
        if os.path.exists(ruta) and os.path.isfile(ruta):
           if ruta.lower( ).endswith(".txt"): 
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
    