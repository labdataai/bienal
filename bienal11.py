import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import requests
from io import BytesIO
import random

import AnimatedGIF
from AnimatedGIF import *
import gif_animado2

# ----------------------------------------------------------------------------------------------------------------------
# Función para cargar imágenes desde una URL y hacerlas circulares
# ----------------------------------------------------------------------------------------------------------------------
def load_circular_image(url, size=(152, 152)):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content)).convert("RGBA")

    # Redimensionar la imagen usando LANCZOS
    img_data = img_data.resize(size, Image.LANCZOS)

    # Crear una máscara circular
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)

    # Aplicar la máscara a la imagen
    img_data.putalpha(mask)
    return ImageTk.PhotoImage(img_data)


# ----------------------------------------------------------------------------------------------------------------------
# Función para cargar imágenes sin modificar
# ----------------------------------------------------------------------------------------------------------------------
def load_image(url, size=(325, 325)):
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content)).convert("RGBA")
    img_data = img_data.resize(size, Image.LANCZOS)  # Usando LANCZOS
    return ImageTk.PhotoImage(img_data)


# ----------------------------------------------------------------------------------------------------------------------
# Función para cargar imágenes ajustadas a un tamaño vertical
# ----------------------------------------------------------------------------------------------------------------------
def load_vertical_image(url, width_percentage=10):
    # Obtener el tamaño de la ventana principal
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular el tamaño de la imagen
    width = int(screen_width * width_percentage / 100)
    height = int(screen_height)

    # Cargar la imagen desde la URL y redimensionarla
    response = requests.get(url)
    img_data = Image.open(BytesIO(response.content)).convert("RGBA")
    img_data = img_data.resize((width, height), Image.LANCZOS)

    return ImageTk.PhotoImage(img_data)

# ----------------------------------------------------------------------------------------------------------------------
# Función para actualizar las imágenes de la galería al azar
# ----------------------------------------------------------------------------------------------------------------------
def update_gallery_images():
    random_urls = random.sample(image_urls, len(image_urls))  # Aleatorizar las URLs

    for index, url in enumerate(random_urls):
        img = load_image(url)  # Cargar cada imagen
        img_labels[index].config(image=img)  # Actualizar la etiqueta de la imagen
        img_labels[index].image = img  # Mantener una referencia

    #if not new_window_open:  # Solo actualizar si la ventana secundaria no está abierta
    root.after(2000, update_gallery_images)  # Repetir cada 1 segundo


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

# Cargar la imagen del perfil de forma circular
profile_image_url = "https://images.unsplash.com/photo-1513721032312-6a18a42c8763?w=152&h=152&fit=crop&crop=faces"
profile_image = load_circular_image(profile_image_url)
profile_image_label = ttk.Label(header_frame, image=profile_image)
profile_image_label.grid(row=0, column=0, padx=10)

# Información del usuario
user_info_frame = ttk.Frame(header_frame)
user_info_frame.grid(row=0, column=1, padx=10)

username_label = ttk.Label(user_info_frame, text="janedoe_", font=("Arial", 20, "bold"))
username_label.pack()

# Estilo personalizado para el botón
style.configure("Edit.TButton", background="#ffffff", foreground="#333333", bordercolor="#cccccc", borderwidth=1)

# Botón de "Editar Perfil"
edit_button = ttk.Button(user_info_frame, text="Editar Perfil", style="Edit.TButton")
edit_button.pack(pady=5)

# Estadísticas del perfil
stats_frame = ttk.Frame(header_frame)
stats_frame.grid(row=1, column=0, columnspan=2, pady=10)

stats_label = ttk.Label(stats_frame, text="164 publicaciones | 188 seguidores | 206 siguiendo")
stats_label.pack()

# Biografía
bio_label = ttk.Label(header_frame, text="Jane Doe - Lorem ipsum dolor sit")
bio_label.grid(row=2, column=0, columnspan=2, pady=5)

# ----------------------
# Sección principal
main_frame = ttk.Frame(root)
main_frame.pack()

# Galería de imágenes
gallery_frame = ttk.Frame(main_frame)
gallery_frame.pack(pady=10)

# Lista de imágenes de la galería
image_urls = [
    "https://images.unsplash.com/photo-1511765224389-37f0e77cf0eb?w=500&h=500&fit=crop",
    "https://images.unsplash.com/photo-1497445462247-4330a224fdb1?w=500&h=500&fit=crop",
    "https://images.unsplash.com/photo-1426604966848-d7adac402bff?w=500&h=500&fit=crop",
    "https://images.unsplash.com/photo-1502630859934-b3b41d18206c?w=500&h=500&fit=crop",
    "https://images.unsplash.com/photo-1498471731312-b6d2b8280c61?w=500&h=500&fit=crop",
    "https://images.unsplash.com/photo-1515023115689-589c33041d3c?w=500&h=500&fit=crop",
]

# Crear etiquetas para las imágenes en la galería
img_labels = []
for index in range(6):
    img = load_image(image_urls[index])  # Cargar la primera imagen
    img_label = ttk.Label(gallery_frame, image=img)
    img_label.image = img  # Mantener una referencia
    img_labels.append(img_label)

    # Calcular la posición en la cuadrícula
    row = index // 3
    column = index % 3
    img_label.grid(row=row, column=column, padx=5, pady=5)



# ----------------------
# Función para abrir y cerrar la ventana sin marco
def toggle_new_window(event=None):
    global new_window_open, new_window

    if new_window_open:  # Si la ventana secundaria está abierta, cerrarla
        new_window.destroy()
        new_window_open = False
        update_gallery_images()  # Reanudar el cambio de imágenes
    else:  # Si la ventana secundaria no está abierta, abrirla

        new_window = tk.Toplevel(root)
        new_window.title("")  # Sin título
        new_window.geometry(f"{root.winfo_width()}x{int(root.winfo_height()*1.1)}")  # Mismo tamaño que la ventana principal
        new_window.geometry(f"{root.winfo_width()}x{int(root.winfo_height()*1.1)}")  # Mismo tamaño que la ventana principal
        new_window.configure(bg="white")
        new_window.overrideredirect(True)  # Quitar el marco

        label_gif = ttk.Label(new_window)
        centro_x = int(new_window.winfo_width() / 2)
        centro_y = int(new_window.winfo_height() / 2)
        label_gif.place(x=centro_x, y=centro_y, relheight=1)
        label_gif.place(relx=0.5, rely=0.5, anchor="center")

        # Cargar el GIF
        gif_url = "D:/UCA/Labo de datos/Proyectos/Bienal/Bienal/imagenes/64ee1832914441.569836c7b2ff3.gif"
        ag2=AnimatedGIF.AnimatedGif(new_window, gif_url)
        ag2.start_thread()
        #gif_player = gif_animado2.GifPlayer(label_gif, gif_url, delay=100)
        ag2.pack(expand=True)


        # Crear la etiqueta que contiene el
        # GIF
        #gif_label = ttk.Label(new_window, image=gif_image)
        #gif_label.image = gif_image  # Mantener una referencia
        #gif_label.place(relx=0.5, rely=0.5, anchor="center")

        new_window_open = True
        update_gallery_images()  # Detener el cambio de imágenes mientras está abierta


# ----------------------
# Variable de control para la nueva ventana
new_window_open = False
new_window = None

# Vincular la tecla ENTER a la función toggle_new_window
root.bind('<Return>', toggle_new_window)
# Iniciar el cambio de imágenes
update_gallery_images()
# ----------------------

# ----------------------
# Cargar imágenes laterales (izquierda y derecha)
left_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcJxLFWeQqS3Nb0KBiI6thfiz1CV5pc5A_moArnS7JQZT2rS1y57SwFNI9QK-zNy1qTGo&usqp=CAU"
right_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcJxLFWeQqS3Nb0KBiI6thfiz1CV5pc5A_moArnS7JQZT2rS1y57SwFNI9QK-zNy1qTGo&usqp=CAU"

left_image = load_vertical_image(left_image_url)
right_image = load_vertical_image(right_image_url)

# Etiqueta para la imagen del lado izquierdo
left_image_label = ttk.Label(root, image=left_image)
left_image_label.image = left_image
left_image_label.place(x=0, y=0, relheight=1)  # Coloca la imagen a la izquierda

# Etiqueta para la imagen del lado derecho
right_image_label = ttk.Label(root, image=right_image)
right_image_label.image = right_image
right_image_label.place(relx=1, y=0, anchor="ne", relheight=1)


# Agregar el recuadro gris oscuro en la parte inferior de la ventana
footer_height = int(root.winfo_screenheight() * 0.05)  # 5% de la altura de la pantalla
footer_width = int(root.winfo_screenwidth())  # 5% de la altura de la pantalla

footer_frame = ttk.Frame(root, height=footer_height, width=footer_width,  relief="solid", style="Footer.TFrame")
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Estilo para el recuadro
style.configure("Footer.TFrame", background="#333333")  # Gris oscuro

# Crear el label con el texto dentro del recuadro
footer_label = ttk.Label(footer_frame, text="Presione el botón", font=("Arial", 14, "bold"), foreground="white", background="#333333")
footer_label.place(relx=0.5, rely=0.5, anchor="center")




# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()