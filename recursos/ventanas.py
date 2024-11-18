import tkinter as tk

# ----------------------
# Variable de control para la nueva ventana
new_window_open = False
new_window = None

# ----------------------
# Función para abrir y cerrar la ventana sin marco
def toggle_new_window(root,event=None):
    global new_window_open, new_window

    if new_window_open:  # Si la ventana secundaria está abierta, cerrarla
        new_window.destroy()
        new_window_open = False
        im.update_gallery_images(image_urls,img_labels,root)  # Reanudar el cambio de imágenes
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
        update_gallery_images(image_urls,img_labels,root)  # Detener el cambio de imágenes mientras está abierta
