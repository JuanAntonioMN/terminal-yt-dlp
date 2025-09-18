from api.conexion import Conexion
from api.ClienteCanal import ClienteCanal
from rich.console import Console
from rich.table import Table
import json

class Canales:
    def __init__(self):
        self.__conexion = Conexion()
        self.__cliente = ClienteCanal(self.__conexion)
        self.console = Console()

    def mostrar_tabla(self, canales):
       
        if not canales:
            self.console.print("[red]⚠ No se encontraron canales[/red]") 

        if isinstance(canales, dict):
            data = [canales]
        if isinstance(canales,str):
            data=json.loads(canales)

        table = Table(title="📺 Lista de Canales")
        table.add_column("ID", style="magenta")
        table.add_column("Nombre", style="cyan")
        table.add_column("URL", style="green")
        table.add_column("Videos", style="yellow")
        table.add_column("Comentarios", style="red")
        table.add_column("Subtítulos", style="blue")
        
       
        for canal in data:
           table.add_row(
               str(canal["idCanal"]),
               canal["Nombre_Canal"],
               canal["Url_Canal"],
               str(canal["Cantidad_de_Videos"]),
               canal["Ruta_Comentarios"],
               canal["Ruta_Subtitulos"],
            )

        self.console.print(table)

    async def canales(self):
        try:
            data = await self.__cliente.mostrarCanales()
            self.mostrar_tabla(data)
        except Exception as e:
            self.console.print(f"[red]❌ Error al obtener canales: {e}[/red]")

    async def buscarNombre(self, nombre: str):
        try:
            data = await self.__cliente.buscarPorNombre(nombre)
            self.mostrar_tabla(data)
        except Exception as e:
            self.console.print(f"[red]❌ Error al buscar canal por nombre: {e}[/red]")

    async def buscarUrl(self, url: str):
        try:
            data = await self.__cliente.buscarPorUrl(url)
            self.mostrar_tabla(data)
        except Exception as e:
            self.console.print(f"[red]❌ Error al buscar canal por URL: {e}[/red]")

    async def cantidadVideos(self, nombre: str):
        try:
            cantidad = await self.__cliente.cantidadVideos(nombre)
            if cantidad:
                self.console.print(
                    f"[yellow]📊 El canal [bold]{nombre}[/bold] tiene [green]{cantidad}[/green] videos.[/yellow]"
                )
            else:
                self.console.print(f"[red]⚠ Canal '{nombre}' no encontrado[/red]")
        except Exception as e:
            self.console.print(f"[red]❌ Error al obtener cantidad de videos: {e}[/red]")
