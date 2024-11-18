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

# ----------------------
# Sección principal
main_frame = ttk.Frame(root)
main_frame.pack()

#root.after(2000, im.update_gallery_images,image_urls,img_labels )  # Repetir cada 1 segundo
#----------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------
# Cargar imágenes laterales (izquierda y derecha)
left_image_url="D:/github/prueba_ventana/imagenes/verticales/conections-between-brain-and-machine.gif"
right_image_url="D:/github/prueba_ventana/imagenes/verticales/conections-between-brain-and-machine.gif"

im.load_top_horizontal_image(root,left_image_url)
#im.load_right_vertical_image(root,right_image_url)

root.mainloop()