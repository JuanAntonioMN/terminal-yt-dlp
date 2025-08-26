import argparse #Para aceptar nuestros 
import shlex #Para limpiar nuestro array de comandos
import os #Para limpiar la consola
import getpass #Obtener información del usuario
from vistas.Canal import Canal
from vistas.Descargas import Descargas
from vistas.Video import Video


class Shell:
    
    def __init__(self):
        self.__comandos=argparse.ArgumentParser(prog="dpm", add_help=False)
        self.__subparsers = self.__comandos.add_subparsers(dest="command")
        self.__user=getpass.getuser( )
        self.__canal=Canal( )
        self.__video=Video( )
        self.__descargas=Descargas( )
        
    def comandos(self):
         # --- Comando insert ---
        parser_insert = self.__subparsers.add_parser("insert", help="Insertar URL")
        parser_insert.add_argument("-u", "--url", required=True, help="URL a insertar")
        
        # --- Comando Descargar videos youtube ---
        parser_descargar=self.__subparsers.add_parser("descargar",help="Descargar videos")
        parser_descargar.add_argument("-u", "--url", required=True, help="URL a descargar")
        
        # --- Comando descargar videos por archivo ---
        parser_archivo=self.__subparsers.add_parser("archivo",help="Descargar videos")
        parser_archivo.add_argument("-a", "--arch", required=True, help="archivo a descargar")
        
        # --- Comando mostrar ---
        parser_show=self.__subparsers.add_parser("show",help="Mostrar las urls")
    
        # --- Comando delete ---
        parser_delete =self.__subparsers.add_parser("delete", help="Eliminar URL")
        parser_delete.add_argument("-u", "--url", required=True, help="URL a eliminar")
  
    def limpiar_consola(self):
        
        # Windows
        if os.name == "nt":
            os.system("cls")
        # Linux / macOS
        else:
            os.system("clear")

        
    def funciones(self,comando):
          # Ejecutar comando
          if comando.command == "insert":
                 print("INSERTADO")
          elif comando.command == "delete":
                  print("ELIMINADO")
          elif comando.command =="show":
                 print("LISTANDO")
          elif comando.command=="descargar":
                    print("DESCARGANDO. . .")
          else:
                 print("Error en el comando no valido")
    
    def terminal(self):
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
                parsed = self.__comandos.parse_args(args)

                self.funciones(parsed)
              
            except SystemExit:
                pass
            except KeyboardInterrupt:
                break
