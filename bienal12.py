import tkinter as tk
import recursos.images as im
import recursos._perfil_usuario_front as pu
import recursos.ventanas as vent
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import requests
from io import BytesIO
import random

import AnimatedGIF
#from AnimatedGIF import *
import gif_animado2

#https://www.youtube.com/watch?v=Pbw7Km8jECs

# ----------------------------------------------------------------------------------------------------------------------
# Función para simular un efecto de pulsación en el loader
# ----------------------------------------------------------------------------------------------------------------------
#def pulse_loader():
#    root.after(500, pulse_loader)  # Llamar a la función de nuevo cada 500ms

# ----------------------------------------------------------------------------------------------------------------------
# Crear ventana principal
# ----------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("Perfil de Usuario")
#root.geometry("600x800")
root.configure(bg="#ffffff")

# ----------------------------------------------------------------------------------------------------------------------
# Configuración del estilo de los componentes
# ----------------------------------------------------------------------------------------------------------------------
style = ttk.Style()
style.configure("TFrame", background="#ffffff")
style.configure("TLabel", background="#ffffff")
style.configure("TButton", padding=5)

# ----------------------
# Sección del encabezado
header_frame = ttk.Frame(root)
header_frame.pack(pady=10)

# Información del usuario
pu.perfil_usuario(header_frame)

# ----------------------
# Sección principal
main_frame = ttk.Frame(root)
main_frame.pack()

# Lista de imágenes de la galería
image_urls = [
    "D:/github/prueba_ventana/imagenes/perfiles/photo-1426604966848-d7adac402bff.jpeg",
    "D:/github/prueba_ventana/imagenes/perfiles/photo-1497445462247-4330a224fdb1.jpeg",
    "D:/github/prueba_ventana/imagenes/perfiles/photo-1498471731312-b6d2b8280c61.jpeg",
    "D:/github/prueba_ventana/imagenes/perfiles/photo-1502630859934-b3b41d18206c.jpeg",
    "D:/github/prueba_ventana/imagenes/perfiles/photo-1511765224389-37f0e77cf0eb.jpeg",
    "D:/github/prueba_ventana/imagenes/perfiles/photo-1515023115689-589c33041d3c.jpeg",
]

img_labels=im.galeria_imagenes(main_frame,image_urls)

# Vincular la tecla ENTER a la función toggle_new_window
root.bind('<Return>', vent.toggle_new_window , root)

# Iniciar el cambio de imágenes
im.update_gallery_images(image_urls,img_labels,root)

#root.after(2000, im.update_gallery_images,image_urls,img_labels )  # Repetir cada 1 segundo
#----------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------
# Cargar imágenes laterales (izquierda y derecha)
left_image_url="D:/github/prueba_ventana/imagenes/verticales/conections-between-brain-and-machine.gif"
right_image_url="D:/github/prueba_ventana/imagenes/verticales/conections-between-brain-and-machine.gif"

im.load_left_vertical_image(root,left_image_url)
im.load_right_vertical_image(root,right_image_url)

# Agregar el recuadro gris oscuro en la parte inferior de la ventana
footer_height = int(root.winfo_screenheight() * 0.05)  # 5% de la altura de la pantalla
footer_width = int(root.winfo_screenwidth())  # 5% de la altura de la pantalla
style.configure("Footer.TFrame", background="#333333")  # Gris oscuro
footer_frame = ttk.Frame(root, height=footer_height, width=footer_width,  relief="solid", style="Footer.TFrame")
footer_frame.pack(side=tk.BOTTOM)
footer_label = ttk.Label(footer_frame, text="<<<< Presione el botón ❤ >>>>", font=("Arial", 20, "bold"), foreground="red", background="#333333")
footer_label.place(relx=0.5, rely=0.5, anchor="center")

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()