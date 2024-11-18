import os
import csv

def cargar_csv_a_diccionarios(ruta_archivo):
    # Abre el archivo CSV en modo lectura
    with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        # Crear un lector de CSV especificando el delimitador como punto y coma
        lector_csv = csv.DictReader(archivo, delimiter=';')

        # La función DictReader convierte cada fila en un diccionario usando los encabezados
        lista_filas = [fila for fila in lector_csv]

    return lista_filas


def cargar_nombres_archivos(directorio):
    nombres_archivos = []

    # Itera sobre los archivos en el directorio
    for archivo in os.listdir(directorio):
        # Filtrar los archivos que terminan en '.csv'
        #if archivo.endswith('.csv'):
        nombres_archivos.append(archivo)

    return nombres_archivos


# Ejemplo de uso
directorio = 'D:/github/prueba_ventana/'  # Ruta del directorio con los archivos CSV
nombres = cargar_nombres_archivos(directorio)
for fila in nombres:
    print(fila)

# Ejemplo de uso
ruta = 'D:/github/prueba_ventana/perfiles.csv'  # Ruta del archivo CSV
datos = cargar_csv_a_diccionarios(ruta)

# Imprimir los datos cargados
for fila in datos:
    print(fila)