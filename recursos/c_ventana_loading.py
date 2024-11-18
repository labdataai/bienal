import tkinter as tk
import recursos.c_loading as cl
import recursos.images as im

class ventana_loading():

    root=None
    canvas=None
    cargando=None
    proporcion_centro = 2

    def __init__(self):
        #self.root = tk.Tk()
        self.root = tk.Toplevel()
        self.root.attributes("-fullscreen", True)
        self.ocultar_ventana()
        self.root.title("Loading Animation")
        window_width = self.root.winfo_screenwidth()  # Obtener el ancho de la pantalla
        window_height = self.root.winfo_screenheight()  # Obtener la altura de la pantalla
        self.root.geometry(f"{window_width}x{window_height}+0+0")  # Establecer tamaño de la ventana
        self.root.overrideredirect(False)  # Eliminar la barra de título y bordes (pantalla completa)
        # Crear un canvas para dibujar los círculos

        footer_height = int(self.root.winfo_screenheight() * 0.05)
        altura=int( (self.root.winfo_screenheight()-footer_height)/self.proporcion_centro)
        ancho=int(self.root.winfo_screenwidth())

        self.canvas = tk.Canvas(self.root, width=ancho, height=altura, bg="white")

        #self.canvas.pack()

        ruta_imagen="D:/github/prueba_ventana/imagenes/verticales/conections-between-brain-and-machine.gif"
        self.cargar_imagen_superior(ruta_imagen)
        self.cargando=cl.loading(self.root,self.canvas)
        self.cargar_imagen_inferior(ruta_imagen)

        posicion_y=int( (self.root.winfo_screenheight()-footer_height-altura) /2)
        self.canvas.place(y=posicion_y)

        #self.mostrar_ventana()

    def start(self):
        self.root.mainloop()

    def stop(self):
        self.ocultar_ventana()
        self.root.quit()

    def cargar_imagen_superior(self,ruta_imagen):
        im.load_horizontal_image(self.root,ruta_imagen,True)

    def cargar_imagen_inferior(self,ruta_imagen):
        im.load_horizontal_image(self.root,ruta_imagen,False)

    def ocultar_ventana(self):
        self.root.withdraw()  # Oculta la ventana

    def mostrar_ventana_tiempo(self, mili_segs):
        self.root.deiconify()  # Mostrar la ventana
        self.root.after(mili_segs, self.stop)
        self.start()



#    def ocultar_ventana(self):
#        self.root.withdraw()

#    def mostrar_ventana(self):
#        self.root.deiconify()
#        self.root.after(5, self.ocultar_ventana())