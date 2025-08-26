import argparse #Para aceptar nuestros 
import shlex #Para limpiar nuestro array de comandos
import os #Para limpiar la consola
import getpass #Obtener información del usuario

urls=[]

def insert(url):
    urls.append(url)
    print(f"✅ Insertando {url}")
    

def delete(url):
    urls.remove(url)
    print(f"🗑️ Eliminando {url}")

def show( ):
    for url in urls:
        print(url)

def descargar( ):
    print("Descarga YouTube")

def build_parser( ):
    parser = argparse.ArgumentParser(prog="dpm", add_help=False)
    subparsers = parser.add_subparsers(dest="command")

    # --- Comando insert ---
    
    parser_insert = subparsers.add_parser("insert", help="Insertar URL")
    parser_insert.add_argument("-u", "--url", required=True, help="URL a insertar")
    
    # --- Comando Descargar videos youtube ---
    
    parser_descargar=subparsers.add_parser("descargar",help="Descargar videos")
    parser_descargar.add_argument("-u", "--url", required=True, help="URL a descargar")
    
    
    # --- Comando descargar videos por archivo ---
     
    parser_archivo=subparsers.add_parser("Archivo",help="Descargar videos")
    parser_archivo.add_argument("-a", "--arch", required=True, help="archivo a descargar")
    

    # --- Comando mostrar ---
    parser_show=subparsers.add_parser("show",help="Mostrar las urls")
 
    # --- Comando delete ---
    parser_delete = subparsers.add_parser("delete", help="Eliminar URL")
    parser_delete.add_argument("-u", "--url", required=True, help="URL a eliminar")

    return parser

def limpiar_consola( ):
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Linux / macOS
    else:
        os.system("clear")



def usuario( ):
    user=getpass.getuser( )
    return user

def main( ):
    parser = build_parser( )
    print("🚀 Bienvenido a DPM (Demo Package Manager)")
    print("Escribe 'exit' para salir.\n")
    user=usuario( )
    while True:
        try:
            # Leer comando
            raw = input(f"{user}> ")

            if raw.strip( ).lower( ) in ["exit", "quit"]:
                break
            elif raw.strip( ).lower( ) in ["cls","clear"]:
                limpiar_consola( )
                continue

            # Dividir como shell (respeta comillas)
            args = shlex.split(raw)

            # Si no empieza con 'dpm', obligamos a que esté
            
            if args and args[0] != "dpm":
                print(f"Error se necesita el comando dpm")
                continue
            
            args = args[1:]
            parsed = parser.parse_args(args)
            # Parsear argumentos
            parsed = parser.parse_args(args)

            # Ejecutar comando
            if parsed.command == "insert":
                insert(parsed.url)
            elif parsed.command == "delete":
                delete(parsed.url)
            elif parsed.command =="show":
                show( )
            elif parsed.command=="descargar":
                descargar( )
            else:
                print("❌ Comando no reconocido")

        except SystemExit:
            pass
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main( )