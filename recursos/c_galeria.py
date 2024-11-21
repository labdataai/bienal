from PIL import Image, ImageTk, ImageDraw
from tkinter import ttk
import random as rn

class galeria_imagenes():

    main_frame=None
    gallery_frame=None

    def __init__(self,gallery_frame):
        self.gallery_frame=gallery_frame
        #self.main_frame=main_frame
        #self.gallery_frame = ttk.Frame(self.main_frame)
        #self.gallery_frame.pack(pady=10)


    def load_image(self,url, size=(325, 325)):
        img_data = Image.open(url).convert("RGBA")
        img_data = img_data.resize(size, Image.LANCZOS)  # Usando LANCZOS
        return ImageTk.PhotoImage(img_data)


    def galeria_imagenes(self, usuario ,gallery_frame ,img_labels,image_size):

        #print("Se ejecuta galeria_imagenes")
        # Galería de imágenes
        #gallery_frame = ttk.Frame(self.main_frame)
        #gallery_frame.pack(pady=10)

        # Crear etiquetas para las imágenes en la galería
        cant_imagenes=6
        directorio=usuario["directorio_galeria"]
        cant_fotos=len(usuario["archivos_galeria"])

        ids_imagenes=rn.sample(range(0, cant_fotos), cant_imagenes)
        #print("ids_imagenes: ",ids_imagenes)
        img_labels = []

        #proporcion_imagen=0.3
        #image_size=(int(size_windows[1]*proporcion_imagen),int(size_windows[1]*proporcion_imagen))

        #print("image_size",image_size)

        i=0
        for index in ids_imagenes:
            archivo=usuario["directorio_galeria"]+"/"+usuario["archivos_galeria"][index]
            #print(archivo)
            img = self.load_image(archivo,image_size)  # Cargar la primera imagen
            img_label = ttk.Label(self.gallery_frame, image=img)
            img_label.image = img  # Mantener una referencia
            img_label.config(image=img)
            img_labels.append(img_label)

            # Calcular la posición en la cuadrícula
            row = i // 3
            column = i % 3
            #print("row",row,"column",column)
            img_label.grid(row=row, column=column, padx=5, pady=5)
            i=i+1


        return img_labels