from api.conexion import Conexion
from api.Descargar import Descargar
import json
import os
from rich.progress import track
from rich.console import Console
import asyncio
from rich.progress import Progress




class Descargas:
    def __init__(self):
        self.__conexion=Conexion( )
        self.__descargar=Descargar(self.__conexion)
        self.__console = Console( )
    
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
            mensaje=datos.get("Mensaje")
            if estado in (304, 404, 409, 500):
                self.__console.print(f"\n[bold red]{mensaje}[/bold red]")
                progress.stop( )
               
            # Paso 4: guardar
            progress.update(task, advance=1, description="Guardando información")
            await asyncio.sleep(1)

            # Paso 5: finalizar
            progress.update(task, advance=1, description="Finalizando")
            await asyncio.sleep(1)
                
            if estado == 200:
                video=datos.get("Video")
                self.__console.print(f"\nId Canal: {video["id_canal"]}")
                self.__console.print(f"\nNombre del video: {video["nombre"]}")
                self.__console.print(f"\nFecha del video: {video["fecha"]}")
                self.__console.print(f"\nUrl del video: {video["url"]}")
                self.__console.print(f"\n[bold green]{mensaje}[/bold green]")

          
    async def descargarArchivo(self,ruta):
       try:
        if os.path.exists(ruta) and os.path.isfile(ruta):
           if ruta.lower( ).endswith(".txt"): 
                with open(ruta,"r") as datos:
                    enlace=datos.readlines( )
                listaEnlaces=[linea.strip( ) for linea in enlace if linea.strip( ) ]
                jsonEnlaces=json.dumps(listaEnlaces)
                
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
                    datos=await self.__descargar.descargarArchivo(jsonEnlaces)
                    estado = datos.get("Estado")
                    mensaje=datos.get("Mensaje")
                    if estado in (304, 404, 409, 500):
                        self.__console.print(f"[bold red] {mensaje}")
                        progress.stop( )
                    
                    # Paso 4: guardar
                    progress.update(task, advance=1, description="Guardando información")
                    await asyncio.sleep(1)
                    
                    # Paso 5: finalizar
                    progress.update(task, advance=1, description="Finalizando")
                    await asyncio.sleep(1)
                    if estado == 200:
                        self.__console.print(f"\n[bold green]{mensaje}.[/bold green]")
                        print(datos.get("Video"))
                    else:
                        self.__console.print(f"\n[bold yellow] Error inesperado.[/bold yellow]")
           else:
               self.__console.print("\n[bold yellow]El archivo debe ser de tipo txt.[/bold yellow]")
        else:
            self.__console.print("\n[bold red]Error con la ruta del archivo.[/bold red]")
       except Exception as e:
            self.__console.print(f"\n[bold yellow]{e}.[/bold yellow]")

    