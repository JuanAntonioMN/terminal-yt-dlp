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
        # --- Comando descargar videos por archivo ---
        parser_archivo=self.__subparsers.add_parser("download",help="Descargar videos")
        parser_archivo.add_argument("-u", "--url", required=True, help="Descargar videos")
        
        videos=self.__subparsers.add_parser("nombre comando",help="Funcion del comando")
        
  
    def limpiar_consola(self):
        # Windows
        if os.name == "nt":
            os.system("cls")
        # Linux / macOS
        else:
            os.system("clear")
        
    async def funciones(self,comando,args):
          # Ejecutar comando
          if comando.command=="download":
                await self.__descargas.descargar(args[2])
          
              
          else:
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
                
                #dpm download -u url
                
                #"dpm" "Canal" "-u" "url"
                

                
                # Si no empieza con 'dpm', obligamos a que esté
                
                if args and args[0] != "dpm":
                    print(f"Error se necesita el comando dpm")
                    continue
                
                args = args[1:]
                parsed = self.__comandos.parse_args(args)
                
                await self.funciones(parsed,args)
              
            except SystemExit:
                pass
            except KeyboardInterrupt:
                break
