from api.conexion import Conexion
from api.ClienteVideos import ClienteVideos
import json
from rich.console import Console
from rich.table import Table

class Videos:
      def __init__(self):
            conexion = Conexion( )
            self.__cliente = ClienteVideos(conexion)
            self.__console = Console()
        
      def mostrar_tabla_videos(self, videos):
            if not videos:
                  self.__console.print("[red]⚠ No se encontraron videos[/red]")
                  return
       
            if isinstance(videos, dict):
                  videos = [videos]
            elif isinstance(videos, str):
                  try:
                   videos = json.loads(videos)
                  except json.JSONDecodeError:
                   videos = [{"Nombre_Video": videos}]

                  table =Table (title="📺 Lista de Videos")
                  table.add_column("ID", style="magenta")
                  table.add_column("Nombre", style="cyan")
                  table.add_column("Fecha", style="green")
                  table.add_column("Url", style="yellow")
                  table.add_column("Canal", style="red")
            
            for v in videos:
                  table.add_row(
                  str(v.get("idVideo", "")),
                  v.get("Nombre_Video", ""),
                  v.get("Fecha_Video", ""),
                  v.get("Url_Video", ""),
                  str(v.get("idCanal", "")),
                  )
            self.__console.print(table)            
        
      async def buscarVideoNombre(self, nombre: str):
            try:
                  datos = await self.__cliente.buscarVideoNombre(nombre)
                  self.mostrar_tabla_videos(datos)
            except Exception as e:
                  return self.__console.print(f"[red]❌ Error al obtener el video: {e}[/red]")

      async def buscarVideoID(self, id:int):
            try:
                  datos = await self.__cliente.buscarVideoID(id)
                  self.mostrar_tabla_videos(datos)
            except Exception as e:
                  self.__console.print(f"[red]❌ Error al obtener el video: {e}[/red]")
          
      async def buscarVideoURL(self, url: str):
            try:
                  datos = await self.__cliente.buscarVideoUrl(url)
                  self.mostrar_tabla_videos(datos)
            except Exception as e:
                  self.__console.print(f"[red]❌ Error al obtener el video: {e}[/red]")
          
      async def mostrarVideos(self):
            try:
                  datos = await self.__cliente.mostrarVideos()
                  if datos:
                        self.mostrar_tabla_videos(datos)
                  else:
                        print("No hay videos para mostrar") 
            except Exception as e:
                  self.__console.print(f"[red]❌ Error al obtener los videos: {e}[/red]")
