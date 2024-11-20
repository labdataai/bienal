# ----------------------------------------------------------------------------------------------------------------------
# Función para cargar imágenes desde una URL y hacerlas circulares
# ----------------------------------------------------------------------------------------------------------------------
from PIL import Image, ImageTk, ImageDraw
from tkinter import ttk
import random

def load_circular_image(url, size=(152, 152)):
    img_data = Image.open(url).convert("RGBA")

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
    img_data = Image.open(url).convert("RGBA")
    img_data = img_data.resize(size, Image.LANCZOS)  # Usando LANCZOS
    return ImageTk.PhotoImage(img_data)

# ----------------------------------------------------------------------------------------------------------------------
# Función para cargar imágenes ajustadas a un tamaño vertical
# ----------------------------------------------------------------------------------------------------------------------
def load_left_vertical_image(root, url, width_percentage=10):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width  = (screen_width * width_percentage // 100)
    height = width
    cant_imagenes=(screen_height//height+1)

    left_image=load_vertical_image(root, url, screen_width, screen_height, width_percentage)

    img_labels = []
    for index in range(cant_imagenes):
        img = left_image  # Cargar la primera imagen
        img_label = ttk.Label(root, image=img)
        img_label.image = img  # Mantener una referencia
        img_label.place(x=0, y=index*height)
        img_labels.append(img_label)

def load_right_vertical_image(root, url, width_percentage=10):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width  = int(screen_width * width_percentage / 100)
    height = width
    cant_imagenes=int(screen_height/height+1)

    left_image=load_vertical_image(root, url, screen_width, screen_height, width_percentage)

    img_labels = []
    for index in range(cant_imagenes):
        img = left_image  # Cargar la primera imagen
        img_label = ttk.Label(root, image=img)
        img_label.image = img  # Mantener una referencia
        img_label.place(relx=1, y=index*height, anchor="ne")
        img_labels.append(img_label)


def load_horizontal_image(root, url, top=True):

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    footer_height = int(root.winfo_screenheight() * 0.1)
    altura_canvas = int((root.winfo_screenheight() - footer_height) / 2)
    altura = (root.winfo_screenheight() - altura_canvas ) //2
    altura = root.winfo_screenheight()//4

    #height=int(screen_height/3)
    height=altura
    width=int(screen_height/3)
    cant_imagenes=int(screen_width/width)
    #print("cant_imagenes:",cant_imagenes)

    left_image = Image.open(url).convert("RGBA")
    left_image = left_image.resize((width, altura), Image.LANCZOS)
    left_image=ImageTk.PhotoImage(left_image)
    img_labels = []

    for index in range(cant_imagenes+2):
        img = left_image  # Cargar la primera imagen
        img_label = ttk.Label(root, image=img)
        img_label.image = img  # Mantener una referencia
        if top:
            img_label.place(x=index*width, y=0, anchor="ne")
        else:
            img_label.place(x=index*width, y=screen_height-height, anchor="ne")

        img_labels.append(img_label)



def load_vertical_image(root, url, screen_width, screen_height,  width_percentage=10):
    # Obtener el tamaño de la ventana principal
    #screen_width = root.winfo_screenwidth()
    #screen_height = root.winfo_screenheight()

    # Calcular el tamaño de la imagen
    width  = int(screen_width * width_percentage / 100)
    height = width
    #height = int(screen_height)

    # Cargar la imagen desde la URL y redimensionarla
    img_data = Image.open(url).convert("RGBA")
    img_data = img_data.resize((width, height), Image.LANCZOS)

    return ImageTk.PhotoImage(img_data)


def _load_vertical_image(url, screen_width, screen_height,  width_percentage=10):
    # Obtener el tamaño de la ventana principal
    #screen_width = root.winfo_screenwidth()
    #screen_height = root.winfo_screenheight()

    # Calcular el tamaño de la imagen
    width = int(screen_width * width_percentage / 100)
    height=width
    #height = int(screen_height)

    # Cargar la imagen desde la URL y redimensionarla
    img_data = Image.open(url).convert("RGBA")
    img_data = img_data.resize((width, height), Image.LANCZOS)

    return ImageTk.PhotoImage(img_data)


def galeria_imagenes(main_frame,image_urls):
    # Galería de imágenes
    gallery_frame = ttk.Frame(main_frame)
    gallery_frame.pack(pady=10)

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

    return img_labels


# ----------------------------------------------------------------------------------------------------------------------
# Función para actualizar las imágenes de la galería al azar
# ----------------------------------------------------------------------------------------------------------------------
def update_gallery_images(image_urls,img_labels,root):
    random_urls = random.sample(image_urls, len(image_urls))  # Aleatorizar las URLs

    for index, url in enumerate(random_urls):
        img = load_image(url)  # Cargar cada imagen
        img_labels[index].config(image=img)  # Actualizar la etiqueta de la imagen
        img_labels[index].image = img  # Mantener una referencia

    #if not new_window_open:  # Solo actualizar si la ventana secundaria no está abierta
    root.after(2000, update_gallery_images, image_urls,img_labels ,root)  # Repetir cada 1 segundo