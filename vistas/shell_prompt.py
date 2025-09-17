import argparse
import shlex
import os
import getpass
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML, FormattedText
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.styles import Style
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

        self.__completer = WordCompleter(
            [
                "dpm download -u",
                "dpm canal --mostrar",
                "dpm canal --nombre",
                "dpm canal --url",
                "dpm canal --cantidad",
                "exit",
                "quit",
                "cls",
                "clear",
            ],
            ignore_case=True,
        )

        self.__session = PromptSession(completer=self.__completer)

        self.__style = Style.from_dict({
            "username": "ansigreen bold",
            "at": "ansiyellow",
            "program": "ansiblue underline",
            "arrow": "ansired",
            "header": "bold underline ansiblue",
        })

    def comandos(self):
        parser_archivo = self.__subparsers.add_parser("download", help="Descargar videos")
        parser_archivo.add_argument("-u", "--url", required=True, help="Descargar videos")

        parser_canales=self.__subparsers.add_parser("canal",help="Operaciones con  Canales")
        parser_canales.add_argument("-n", "--nombre", help="Nombre del canal")
        parser_canales.add_argument("-m", "--mostrar", action="store_true",help="mostrar canales")
        parser_canales.add_argument("-u", "--url", help="URL del canal")
    def limpiar_consola(self):
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_tabla_canales(self, canales):


        if not canales:
            print("No se encontraron canales.")
            return

        if isinstance(canales, dict):
            canales = [canales]
        elif isinstance(canales,str):
            canales=[{"Nombre_Canal":canales}]

        encabezado = [
            ("class:header", f"{'ID':<5} {'Nombre':<30} {'URL':<50} {'Videos':<10} {'Comentarios':<30} {'Subtitulos':<30}")
        ]
        print_formatted_text(FormattedText(encabezado), style=self.__style)

        for canal in canales:
            fila = [
                ("", f"{str(canal.get('idCanal', '')):<5} "),
                ("", f"{canal.get('Nombre_Canal', ''):<30} "),
                ("", f"{canal.get('Url_Canal', ''):<50} "),
                ("", f"{str(canal.get('Cantidad_de_Videos', '')):<10} "),
                ("", f"{canal.get('Ruta_Comentarios', ''):<30} "),
                ("", f"{canal.get('Ruta_Subtitulos', ''):<30}")
            ]
            print_formatted_text(FormattedText(fila), style=self.__style)

    async def funciones(self, comando, args):
        if comando.command == "download":
            await self.__descargas.descargarUrl(args[2])

        elif comando.command == "canal":
            if comando.mostrar:
                canales = await self.__canales.canales()
                if isinstance(canales, str):
                    try:
                        canales = json.loads(canales)
                    except json.JSONDecodeError:
                        print("Error: no se pudo parsear los canales")
                        canales = []
                self.mostrar_tabla_canales(canales)
            elif comando.nombre:
                res=await self.__canales.buscarNombre(args[2])
                self.mostrar_tabla_canales(res)
            elif comando.url:
                resu=await self.__canales.buscarUrl(args[2])
                resu=[c for c in resu if isinstance(c,dict)]
                self.mostrar_tabla_canales(resu)
        else:
            print("Error: comando no válido")

    async def terminal(self):
        self.comandos()
        while True:
            try:
                prompt_text = HTML(
                    f"<username>{self.__user}</username>"
                    f"<at>@</at>"
                    f"<program>dpm</program>"
                    f"<arrow>> </arrow>"
                )

                comando = await self.__session.prompt_async(prompt_text, style=self.__style)

                if comando.strip().lower() in ["exit", "quit"]:
                    break
                elif comando.strip().lower() in ["cls", "clear"]:
                    self.limpiar_consola()
                    continue

                args = shlex.split(comando)

                if args and args[0] != "dpm":
                    print("Error: se necesita el comando dpm")
                    continue

                args = args[1:]
                parsed = self.__comandos.parse_args(args)

                await self.funciones(parsed, args)

            except SystemExit:
                pass
            except KeyboardInterrupt:
                break
