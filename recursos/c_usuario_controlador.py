import os
import csv
import random as rn

class usuario_controlador():

    directorio=""
    archivo_perfiles="perfiles.csv"
    usuarios=[]
    usuario_elegido=0

    def __init__(self,directorio="./perfiles"):
        self.directorio=directorio

    def cargar_csv_a_diccionarios(self):
        ruta_archivo=self.directorio+"/"+self.archivo_perfiles
        lista_filas=[]
        with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo, delimiter=';')
            lista_filas = [fila for fila in lector_csv]

        return lista_filas

    def cargar_imagenes_galeria(self,nombre_usuario):
        nombres_archivos=[]
        directorio = ruta_archivo=self.directorio+"/"+nombre_usuario.lower()+"/galeria/"
        contenido=os.listdir(directorio)
        for archivo in contenido:
            #print(archivo)
            nombres_archivos.append(archivo)
        return nombres_archivos

    def cargar_usuarios(self):
        self.usuarios=self.cargar_csv_a_diccionarios()

        for usuario in self.usuarios:
            nombre=usuario["nombre"]
            #directorio_imagenes=self.directorio+"/"+nombre.lower()+"/"
            directorio_usuario = ruta_archivo = self.directorio + "/" + nombre.lower()
            directorio_galeria = directorio_usuario + "/galeria/"
            usuario["directorio_galeria"]=directorio_galeria
            usuario["directorio_usuario"] = directorio_usuario
            usuario["imagen_perfil"]=usuario["nombre"]+".jpg"
            nombres_archivos=self.cargar_imagenes_galeria(nombre)
            usuario["archivos_galeria"]=nombres_archivos
            usuario["textos"] = self.cargar_textos_perfil(nombre)

            #print(usuario)

    def cargar_textos_perfil(self,usuario):
        archivo_texto="textos_perfil.csv"

        ruta_archivo_texto=self.directorio+"/"+usuario.lower()+"/"+archivo_texto
        archivo_textos_usuario=open(ruta_archivo_texto, mode='r', encoding='utf-8')
        textos=archivo_textos_usuario.readlines()

        return textos


    def _cargar_textos_perfiles(self,usuario):
        archivo_texto="textos_perfil.csv"
        for usuario in self.usuarios:
            ruta_archivo_texto=self.directorio+"/"+usuario.lower()+"/"+archivo_texto
            archivo_textos_usuario=open(ruta_archivo_texto, mode='r', encoding='utf-8')
            textos=archivo_textos_usuario.readlines()
            usuario["textos"]=textos

        print(self.usuarios)

    def get_usuario_elegido(self):
        return self.usuario_elegido

    def seleccionar_usuario_random(self):
        indice=rn.randint(0, len(self.usuarios)-1)
        usuario=self.usuarios[indice]
        self.usuario_elegido=usuario

        return usuario

    def seleccionar_texto_perfil_random(self):
        indice = rn.randint(0, len(self.usuario_elegido["textos"]) - 1)
        texto = self.usuario_elegido["textos"][indice]
        return texto

