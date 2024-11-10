import tkinter as tk
from PIL import Image, ImageTk

gif_url="D:/UCA/Labo de datos/Proyectos/Bienal/Bienal/imagenes/64ee1832914441.569836c7b2ff3.gif"

import tkinter as tk
from PIL import Image, ImageTk
import threading
import time


class GifPlayer(tk.Label):
    def __init__(self, master, gif_path, delay=100):
        super().__init__(master)
        self.gif_path = gif_path
        self.delay = delay  # Retraso entre los frames en milisegundos
        self.frames = []
        self.current_frame = 0
        self.load_gif()
        self.configure(image=self.frames[0])

        # Iniciar el hilo para actualizar la animación
        self.anim_thread = threading.Thread(target=self.animate)
        self.anim_thread.daemon = True  # Hacer el hilo daemon para que termine cuando cierre la ventana
        self.anim_thread.start()

    def load_gif(self):
        # Cargar la imagen GIF usando PIL
        gif = Image.open(self.gif_path)
        self.frames = []

        try:
            # Obtener cada frame del GIF
            while True:
                self.frames.append(ImageTk.PhotoImage(gif.copy()))
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass  # Ya se cargaron todos los frames

    def animate(self):
        # Actualizar la imagen en el Label cada cierto tiempo
        while True:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.configure(image=self.frames[self.current_frame])
            time.sleep(self.delay / 1000)  # Convertir a segundos


def main():
    # Crear la ventana de Tkinter
    root = tk.Tk()
    root.title("GIF Animado en Tkinter")

    # Crear el player del gif y cargar el gif
    gif_player = GifPlayer(root, gif_url, delay=100)
    gif_player.pack()

    # Ejecutar el loop de la aplicación
    root.mainloop()


if __name__ == "__main__":
    main()