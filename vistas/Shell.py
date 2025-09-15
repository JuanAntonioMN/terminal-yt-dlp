import argparse #Para aceptar nuestros 
import shlex #Para limpiar nuestro array de comandos
import os #Para limpiar la consola
import getpass #Obtener información del usuariof
from .Descargas import Descargas

class Shell:
    
    def __init__(self):
        self.__comandos=argparse.ArgumentParser(prog="dpm", add_help=False)
        self.__subparsers = self.__comandos.add_subparsers(dest="command")
        self.__user=getpass.getuser( )
        self.__descargas=Descargas( )
        
    def comandos(self):    
        # --- Comando descargar informacion de videos  ---
        descargas=self.__subparsers.add_parser("download",help="Descargar informacion por enlace o archivos")
        descargas.add_argument("-u","-a", required=True, help="Descargar informacion por enlace o archivos")
        
    
    def limpiar_consola(self):
        # Windows
        if os.name == "nt":
            os.system("cls")
        # Linux / macOS
        else:
            os.system("clear")
        
    async def funciones(self,comando,args):
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
            case _:
                 print("Error en el comando no valido")
    
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
                
             
                # Si no empieza con 'dpm', obligamos a que esté
                
                if args and args[0] != "dpm":
                    print(f"Error se necesita el comando dpm")
                    continue
                
                args = args[1:]
                comandos = self.__comandos.parse_args(args)
               
                await self.funciones(comandos,args)
              
            except SystemExit:
                pass
            except KeyboardInterrupt:
                break
