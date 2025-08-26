from pathlib import Path

ruta=Path("C:/Users/JUAN ANTONIO/Desktop/archivo.txt")

if not ruta.exists():
    print("La ruta no existe:", ruta)
    
elif not ruta.is_file():
    print("La ruta indicada no es un archivo, es una carpeta.")
else:
    print("Archivo válido, listo para abrir y enviar.")
   
