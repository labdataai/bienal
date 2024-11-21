import tkinter as tk
import recursos.c_loading as cl
import recursos.images as im
import time

class ventana_loading():

    root=None
    canvas=None
    cargando=None
    proporcion_centro = 2
    controlador_ventanas=None

    def __init__(self,controlador_ventanas):
        #self.root = tk.Tk()
        self.root = tk.Toplevel()
        self.root.attributes("-fullscreen", True)
        self.ocultar_ventana()
        self.root.title("Loading Animation")
        window_width = self.root.winfo_screenwidth()  # Obtener el ancho de la pantalla
        window_height = self.root.winfo_screenheight()  # Obtener la altura de la pantalla
        self.root.geometry(f"{window_width}x{window_height}+0+0")  # Establecer tamaño de la ventana
        self.root.overrideredirect(False)  # Eliminar la barra de título y bordes (pantalla completa)
        self.controlador_ventanas=controlador_ventanas
        # Crear un canvas para dibujar los círculos

        footer_height = int(self.root.winfo_screenheight() * 0.05)
        #altura=int( (self.root.winfo_screenheight()-footer_height)/self.proporcion_centro)
        altura = int(self.root.winfo_screenheight()/2 )
        ancho=int(self.root.winfo_screenwidth())

        self.canvas = tk.Canvas(self.root, width=ancho, height=altura )

        #self.canvas.pack()

        ruta_imagen="./imagenes/verticales/conections-between-brain-and-machine.gif"
        self.cargar_imagen_superior(ruta_imagen)
        self.cargando=cl.loading(self.root,self.canvas)
        self.cargar_imagen_inferior(ruta_imagen)

        posicion_y=int( self.root.winfo_screenheight() /4)
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


    def esperar_boton(self):
        data=""

        ser=self.controlador_ventanas.serial_port
        #print("esperar_boton ventanta loading")
        if ser.in_waiting > 0:
            #while ser.in_waiting>0:
            #while len(data) < 18:
            data = data + ser.read(ser.in_waiting).decode(encoding='UTF-8').strip()
            while data[len(data)-1].isdigit() == False:
                data = data + ser.read(ser.in_waiting).decode(encoding='UTF-8').strip()
                time.sleep(0.1)
            print("data ventana loading:", data)
            self.stop()
            return

        self.root.after(50, self.esperar_boton)
        #ser.close()


    def mostrar_ventana(self):
        self.root.deiconify()  # Mostrar la ventana
        self.root.after(10, self.esperar_boton)
        self.start()


#    def ocultar_ventana(self):
#        self.root.withdraw()

#    def mostrar_ventana(self):
#        self.root.deiconify()
#        self.root.after(5, self.ocultar_ventana())