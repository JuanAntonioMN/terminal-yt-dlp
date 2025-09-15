import argparse #Para aceptar nuestros 
import shlex #Para limpiar nuestro array de comandos
import os #Para limpiar la consola
import getpass #Obtener información del usuariof
from .Descargas import Descargas
from .Canales import Canales


class Shell:
    
    def __init__(self):
        self.__comandos=argparse.ArgumentParser(prog="dpm", add_help=False)
        self.__subparsers = self.__comandos.add_subparsers(dest="command")
        self.__user=getpass.getuser( )
        self.__descargas=Descargas( )
        self.__canales=Canales()
        
    def comandos(self):    
        # --- Comando descargar videos por archivo ---
        parser_archivo=self.__subparsers.add_parser("download",help="Descargar informacion por enlace o archivos")
        parser_archivo.add_argument("-u", "-a", required=True, help="Descargar videos")
        
        parser_canales=self.__subparsers.add_parser("canal",help="Operaciones con  Canales")
        parser_canales.add_argument("-m", "--mostrar", action="store_true",help="mostrar canales")
        parser_canales.add_argument("-n", "--nombre", help="Nombre del canal")
        parser_canales.add_argument("-u", "--url", help="URL del canal")
  
            
  
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
            elif comando.command == "canal":
                if comando.nombre:
                    resultado= await self.__canales.buscarNombre(args[2])
                   
                    print(resultado)
                elif comando.url:
                
                    resultados= await self.__canales.buscarUrl(comando.url)
                    
                    print(resultados)
            
                elif comando.mostrar:
                    res=await self.__canales.canales()
                    print (res)

            else:
                print("Error: comando no válido")
    
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
