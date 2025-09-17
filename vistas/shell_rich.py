import argparse  # Para aceptar nuestros comandos
import shlex     # Para limpiar nuestro array de comandos
import os        # Para limpiar la consola
import getpass   # Obtener información del usuario
from rich.console import Console #para imprimir
from rich.table import Table#para generar tablas
from rich.prompt import Prompt# es en vez del input

from .Descargas import Descargas
from .Canales import Canales
import json

class Shell:
    def __init__(self):
        self.__comandos = argparse.ArgumentParser(prog="dpm", add_help=False)
        self.__subparsers = self.__comandos.add_subparsers(dest="command")

        self.__user = getpass.getuser()
        self.__descargas = Descargas()
        self.__canales = Canales()

        # Consola Rich
        self.console = Console() #reemplaza los print normales
    def mostrar_tabla_canales(self, canales):
        if not canales:
            self.console.print("[red]⚠ No se encontraron canales[/red]")
            return

        table = Table(title="📺 Lista de Canales")
        table.add_column("ID", style="magenta")
        table.add_column("Nombre", style="cyan")
        table.add_column("URL", style="green")
        table.add_column("Videos", style="yellow")
        table.add_column("Comentarios", style="red")
        table.add_column("Subtítulos", style="blue")

        # Filtrar solo diccionarios válidos
        canales = [c for c in canales if isinstance(c, dict)]

        for c in canales:
            table.add_row(
                str(c.get("idCanal", "")),
                c.get("Nombre_Canal", ""),
                c.get("Url_Canal", ""),
                str(c.get("Cantidad_de_Videos", "")),
                c.get("Ruta_Comentarios", ""),
                c.get("Ruta_Subtitulos", "")
            )

        self.console.print(table)

    def comandos(self):
        # --- Comando descargar videos ---
        parser_archivo = self.__subparsers.add_parser("download", help="Descargar videos")
        parser_archivo.add_argument("-u", "--url", required=True, help="Descargar videos")

        # --- Comando operaciones con canales ---
        parser_canales = self.__subparsers.add_parser("canal", help="Operaciones con Canales")
        parser_canales.add_argument("-n","--nombre",help="nombre del canal")
        parser_canales.add_argument("-m", "--mostrar", action="store_true",help="mostrar canales")
        parser_canales.add_argument("-u", "--url", help="URL del canal")
        parser_canales.add_argument("--comentarios", help="Ruta comentarios")
        parser_canales.add_argument("--subtitulos", help="Ruta subtítulos")

    def limpiar_consola(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    async def funciones(self, comando, args):
        # Ejecutar comando
        if comando.command == "download":
            await self.__descargas.descargar(args[2])
            self.console.print("[green]✅ Descarga completada[/green]")

        elif comando.command == "canal":
            if comando.mostrar:
                canales = await self.__canales.canales()
                if isinstance (canales,str):
                    canales=json.loads(canales)
                    self.mostrar_tabla_canales(canales)

            elif comando.nombre:
                res =await self.__canales.buscarNombre(args[2])
                if isinstance(res,str):
                    res=[{"NOmbre canal":res}]
                elif isinstance(res,dict):
                    res=[res]
                self.mostrar_tabla_canales(res)
            elif comando.url:
                resu=await self.__canales.buscarUrl(args[2])
                resu=[c for c in resu if isinstance(c,dict)]
                self.mostrar_tabla_canales(resu)

        else:
            self.console.print("[red bold]❌ Error: comando no válido[/red bold]")

    async def terminal(self):
        self.comandos()  # Inicializamos los comandos
        while True:
            try:
                #
                comando = Prompt.ask(f"[bold green]{self.__user}@dpm[/bold green]")

                if comando.strip().lower() in ["exit", "quit"]:
                    self.console.print("[magenta]👋 Saliendo de la terminal...[/magenta]")
                    break
                elif comando.strip().lower() in ["cls", "clear"]:
                    self.limpiar_consola()
                    continue

                # Dividir como shell (respeta comillas)
                args = shlex.split(comando)

                if args and args[0] != "dpm":
                    self.console.print("[red]❌ Error: se necesita el comando 'dpm'[/red]")
                    continue

                args = args[1:]
                parsed = self.__comandos.parse_args(args)

                await self.funciones(parsed, args)

            except SystemExit:
                pass
            except KeyboardInterrupt:
                self.console.print("\n[red]⚡ Interrumpido por el usuario[/red]")
                break
