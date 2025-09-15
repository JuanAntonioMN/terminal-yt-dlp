import argparse #Para aceptar nuestros 
import shlex #Para limpiar nuestro array de comandos
import os #Para limpiar la consola
import getpass #Obtener información del usuariof
from .Descargas import Descargas
from .Videos import Videos


class Shell:
    
    def __init__(self):
        self.__comandos=argparse.ArgumentParser(prog="dpm", add_help=False)
        self.__subparsers = self.__comandos.add_subparsers(dest="command")
        self.__user=getpass.getuser( )
        self.__descargas=Descargas( )
        self.__videos= Videos( )
        
    def comandos(self):    #modificar este para crear los comandos 
        # --- Comando descargar videos por archivo ---
        parser_archivo=self.__subparsers.add_parser("download",help="Descargar videos")
        parser_archivo.add_argument("-u", "--url", required=True, help="Descargar videos")
        parser_archivo.add_argument("-b", )
        # comando para buscar videos por:
        parser_videos=self.__subparsers.add_parser("search", help="Buscar videos")
        parser_videos.add_argument ("-n","--nombre", help="Buscar videos nombre")
        parser_videos.add_argument ("-i","--id", help="Buscar videos ID")
        parser_videos.add_argument ("-u","--url", help="Buscar videos por url")
        parser_videos.add_argument ("-a","--all", action="store_true", help="Mostrar todos los videos")
                
  
    def limpiar_consola(self):
        # Windows
        if os.name == "nt":
            os.system("cls")
        # Linux / macOS
        else:
            os.system("clear")
        
    async def funciones(self,comando,args): #agregar las funciones de nuestro metodo de rutas
          # Ejecutar comando
        if comando.command=="download":
            await self.__descargas.descargar(args[2])
        elif comando.command == "search":
            if comando.nombre:
                datos= await self.__videos.buscarVideoNombre(args[2])
                print(datos)
            elif comando.id: 
                datos1 = await self.__videos.buscarVideoID(args[2])
                print(datos1)
            elif comando.url:
                datos2 = await self.__videos.buscarVideoURL(args[2])
                print(datos2)
            elif comando.all:
                datos3 = await self.__videos.mostrarVideos()
                print(datos3)
        else:
                print("No se reconocio el comando")
                                    
        #elif comando.command=="shearch":
        #await self.__videos.buscarVideoNombre(args[2])
        #elif comando.command=="sharei":  
        #await self.__videos.buscarVideoID(args[2])
        #elif comando.command=="shareu":
        #await self.__videos.buscarVideoURL(args[2])
        #elif comando.command=="showall":
        #await self.__videos.mostrarVideos( )
        #else:
        #print("Error en el comando no valido")
    
    async def terminal(self):
        self.comandos( ) #Inicializamos los comandos
        while True:
            try:
                comando=input(f"{self.__user}@dpm> ")
                
                if comando.strip( ).lower( ) in ["exit", "quit"]:
                    break
                elif comando.strip( ).lower( ) in ["cls","clear"]:
                    self.limpiar_consola( )
                    continue


                # Dividir como shell (respeta comillas)
                args = shlex.split(comando)
                
                #dpm download -u url
                
                #"dpm" "Canal" "-u" "url"
                

                
                # Si no empieza con 'dpm', obligamos a que esté
                
                if args and args[0] != "dpm":
                    print(f"Error se necesita el comando dpm")
                    continue
                
                args = args[1:]
                parsed = self.__comandos.parse_args(args)
                print(args)
                print(args[2])
                await self.funciones(parsed,args)
              
            except SystemExit:
                pass
            except KeyboardInterrupt:
                break