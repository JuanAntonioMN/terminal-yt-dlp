import requests #Librería para consumir API
from conexion import Conexion

class Canales:
    def __init__(self,conexion:Conexion):
        self.__conexion=conexion
        self.__url=conexion.getUrl( )
        
    #Obtenemos todos los canales con su información   
    def canales(self):
        pass
    
    
    #Buscamos un canal por su nombre
    def buscarNombre(self,nombre):
        pass
    
    #Buscar canal por url
    def buscarUrl(self,url):
        pass
    
    #Mostramos los videos de un canal
    def videosPorCanal(self,id):
        pass
    
    

    
        