
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import requests
from io import BytesIO
import random
from AnimatedGIF import *

root = tk.Tk()
root.title("Perfil de Usuario")
#root.geometry("600x800")
root.configure(bg="#ffffff")

#gif_url = "https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif"
gif_url="D:/UCA/Labo de datos/Proyectos/Bienal/Bienal/imagenes/64ee1832914441.569836c7b2ff3.gif"
footer_frame = ttk.Frame(root,  relief="solid", style="Footer.TFrame")

ag=AnimatedGif(root,gif_url)
ag.start()

root.mainloop()