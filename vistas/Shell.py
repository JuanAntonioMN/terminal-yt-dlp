import argparse  # Para aceptar nuestros comandos
import shlex     # Para limpiar nuestro array de comandos
import os        # Para limpiar la consola
import getpass   # Obtener información del usuario
from .Descargas import Descargas
from .Canales import Canales
from .Videos import Videos


class Shell:
    
    def __init__(self):
        # Parser principal
        self.__comandos = argparse.ArgumentParser(prog="dpm", add_help=False)
        self.__subparsers = self.__comandos.add_subparsers(dest="command")
        self.__user = getpass.getuser()
        self.__descargas = Descargas()
        self.__canales = Canales()   # añadido en el segundo código
        self.__videos = Videos() #añadido
        
    def comandos(self):    
        
        # --- Comando descargar videos ---
        descargas= self.__subparsers.add_parser("download", help="Descargar información por enlace o archivos"
        )
        descargas.add_argument("-u","-a",required=True, help="Descargar informacion por enlace o archivos"
        )
      
        
        # --- Comando canales ---
        canales = self.__subparsers.add_parser(
            "canal", help="Operaciones con Canales"
        )
        canales.add_argument(
            "-m", "--mostrar", action="store_true", help="Mostrar canales"
        )
        canales.add_argument(
            "-n", "--nombre", help="Nombre del canal"
        )
        canales.add_argument(
            "-u", "--url", help="URL del canal"
        )
        
        # --- Comando video ---
        
        videos = self.__subparsers.add_parser(
            "videos", help= "Operaciones con videos"
        )
        videos.add_argument(
            "-n", "--nombre", help="Buscar videos por Nombre"
        )
        videos.add_argument(
            "-u", "--url", help="Buscar videos por URL"
        )
        videos.add_argument(
            "-i", "--id", help="Buscar videos por ID del canal"
        )
        videos.add_argument(
            "-m", "--mostrar", action="store_true", help= "Mostrar todos los videos"
        )
  
    def limpiar_consola(self):
        # Windows
        if os.name == "nt":
            os.system("cls")
        # Linux / macOS
        else:
            os.system("clear")
        
    async def funciones(self, comando, args):
        # Aquí añadimos el match-case como en el primer código
          # Validamos el comando
        match comando.command:
            case "download":
                opcion=args[1]
                #Descargar por archivo
                if opcion=="-a":
                    await self.__descargas.descargarArchivo(args[2])
                #Descargar por URL
                if opcion=="-u":
                    await self.__descargas.descargarUrl(args[2])


            case "canal":
                if comando.nombre:
                    resultado = await self.__canales.buscarNombre(args[2])
                    print(resultado)
                elif comando.url:
                    resultados = await self.__canales.buscarUrl(args[2])
                    print(resultados)
                elif comando.mostrar:
                    res = await self.__canales.canales()
                    print(res)
                else:
                    print("Error: opción de canal no válida")
                    
            case "videos":
                if comando.nombre:
                    datos = await self.__videos.buscarVideoNombre(args[2])
                    print(datos)
                elif comando.url:
                    datos = await self.__videos.buscarVideoURL(args[2])
                    print(datos)
                elif comando.id:
                    datos = await self.__videos.buscarVideoID(args[2])
                    print(datos)
                elif comando.mostrar:
                    datos = await self.__videos.mostrarVideos()
                    print(datos)
                else:
                    print("Error: Comando no válido")
                    
            case _:
                print("Error: comando no válido")
    
    async def terminal(self):
        self.comandos()  # Inicializamos los comandos
        while True:
            try:
                comando = input(f"{self.__user}@dpm> ")
                
                if comando.strip( ).lower( ) in ["exit", "quit"]:
                    break
                elif comando.strip( ).lower( ) in ["cls", "clear"]:
                    self.limpiar_consola( )
                    continue

                # Dividir como shell (respeta comillas)
                args = shlex.split(comando)
                
                # Si no empieza con 'dpm', obligamos a que esté
                if args and args[0] != "dpm":
                    print("Error: se necesita el comando dpm")
                    continue
                
                args = args[1:]
                comandos = self.__comandos.parse_args(args)
                print(args)
                await self.funciones(comandos, args)
              
            except SystemExit:
                # argparse lanza SystemExit si hay error en parseo
                pass
            except KeyboardInterrupt:
                break

