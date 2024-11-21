import time
import tkinter as tk
from tkinter import ttk
import recursos.c_loading as cl
import recursos.images as im
import recursos.c_galeria as gal
import serial
import time

class ventana_perfil():

    root = None
    canvas=None
    header_frame=None
    controlador_usuarios=None
    elementos_perfil_usuario={}
    usuario_random = None
    user_info_frame=None
    username_label=None
    main_frame=None
    gallery_frame=None
    images_lables=[]
    controlador_ventanas=None

    actualizar_perfil=True
    ser=None

    def cargar_root(self):
        self.root = tk.Tk()

    def __init__(self,controlador_usuarios,controlador_ventanas):

        self.controlador_usuarios = controlador_usuarios
        self.actualizar_perfil = True
        #self.root = tk.Tk()
        self.cargar_root()
        self.root.title("Ventana principal")
        self.root.attributes("-fullscreen", True)
        self.controlador_ventanas=controlador_ventanas

        #self.ocultar_ventana()

        window_width = self.root.winfo_screenwidth()  # Obtener el ancho de la pantalla
        window_height = self.root.winfo_screenheight()  # Obtener la altura de la pantalla

        #self.root.geometry(f"{window_width}x{window_height}+0+0")  # Establecer tamaño de la ventana
        self.root.overrideredirect(False)  # Eliminar la barra de título y bordes (pantalla completa)

        ruta_imagen="D:/github/prueba_ventana/imagenes/verticales/conections-between-brain-and-machine.gif"
        self.cargar_imagen_izquierda(ruta_imagen)
        self.cargar_imagen_derecha(ruta_imagen)

        #Borrar
        s = ttk.Style()
        # Create style used by default for all Frames
        s.configure('Frame1.TFrame', background='yellow')

        #self.header_frame = ttk.Frame(self.root, style='Frame1.TFrame')
        self.header_frame = ttk.Frame(self.root)
        self.header_frame.pack(pady=10)

        self.user_info_frame = ttk.Frame(self.header_frame)
        self.user_info_frame.grid(row=0, column=1, padx=10)
        #self.username_label = ttk.Label(self.user_info_frame, text="", font=("Arial", 20, "bold"), background="red", width="10")
        self.username_label = ttk.Label(self.user_info_frame, text="", font=("Arial", 20, "bold"), width="10")

        self.main_frame = ttk.Frame(self.root)
        self.gallery_frame = ttk.Frame(self.root) #Antes estaba self.main_frame
        #self.gallery_frame.pack(pady=0)

        self.main_frame.pack()

        #self.cargar_secciones_datos_usuario()
        #edit_button = ttk.Button(self.user_info_frame, text="Editar Perfil", style="Edit.TButton")
        #edit_button.pack(pady=5)

        #self.mostrar_ventana()
        self.cargar_pie()

    def esperar_boton(self):
        data=""
        #print("esperar_boton ventanta perfil")
        if self.actualizar_perfil==True:
            ser=self.controlador_ventanas.serial_port
            if ser.in_waiting > 0:
                #while ser.in_waiting > 0:
                #while len(data) < 18:
                data = data + ser.read(ser.in_waiting).decode(encoding='UTF-8').strip()
                while data[len(data)-1].isdigit() == False:
                    data = data + ser.read(ser.in_waiting).decode(encoding='UTF-8').strip()
                    time.sleep(0.1)
                print("data serie ventana perfil:", data)
                self.root.after(200, self.esperar_boton)  # Repetir cada x segundo
                #if del nro exacto
                self.controlador_ventanas.tecla_enter_ventana_perfil()

        self.root.after(200, self.esperar_boton)  # Repetir cada x segundo


    def start(self):
        self.cargar_secciones_datos_usuario()
        self.esperar_boton()
        self.root.mainloop()


    def cargar_secciones_datos_usuario(self):
        if self.actualizar_perfil:
            self.cargar_seccion_perfil_usuario()
            self.cargar_centro()

        self.root.after(2000, self.cargar_secciones_datos_usuario)  # Repetir cada x segundo


    def imagen_perfil(self,imagen_perfil):
        # Cargar la imagen del perfil de forma circular

        window_width = self.root.winfo_screenwidth()  # Obtener el ancho de la pantalla
        window_height = self.root.winfo_screenheight()  # Obtener la altura de la pantalla

        size_imagen_perfil=(window_height//7,window_height//7)
        profile_image = im.load_circular_image(imagen_perfil,size_imagen_perfil)
        #profile_image_label = ttk.Label(self.header_frame, image=profile_image ,background="red")
        profile_image_label = ttk.Label(self.header_frame, image=profile_image)
        profile_image_label.image = profile_image
        profile_image_label.grid(row=0, column=0, padx=10)


    def cargar_seccion_perfil_usuario(self):

        self.usuario_random=self.controlador_usuarios.seleccionar_usuario_random()

        imagen_perfil=self.usuario_random["directorio_usuario"]+"/"+self.usuario_random["imagen_perfil"]
        self.imagen_perfil(imagen_perfil)

        #username_label = ttk.Label(self.user_info_frame, text=self.usuario_random["nombre"], font=("Arial", 20, "bold"))
        self.username_label.config(text=self.usuario_random["nombre"])
        self.username_label.pack()

        # Botón de "Editar Perfil"
        #edit_button = ttk.Button(self.user_info_frame, text="Editar Perfil", style="Edit.TButton")
        #edit_button.pack(pady=5)
        # Estilo personalizado para el botón
        # style.configure("Edit.TButton", background="#ffffff", foreground="#333333", bordercolor="#cccccc", borderwidth=1)
        # objetos_graficos.append(profile_image_label)

        # Biografía
        #bio_label = ttk.Label(self.header_frame, text=self.usuario_random["descripcion"] ,background="red")
        bio_label = ttk.Label(self.header_frame, text=self.usuario_random["descripcion"])
        bio_label.grid(row=2, column=0, columnspan=2, pady=10)  #Estaba con pady=5

        self.estadisticas_perfil()


    def estadisticas_perfil(self):
        # Estadísticas del perfil
        stats_frame = ttk.Frame(self.header_frame)
        stats_frame.grid(row=1, column=0, columnspan=2, pady=10)
        #"164 publicaciones | 188 seguidores | 206 siguiendo"

        cant_publicaciones=self.usuario_random["publicaciones"]
        cant_seguidores = self.usuario_random["seguidores"]
        cant_publicaciones = self.usuario_random["seguidos"]
        linea=cant_publicaciones+" publicaciones | "+cant_seguidores+" seguidores | "+cant_publicaciones+" siguiendo"
        #stats_label = ttk.Label(stats_frame, text=linea , background="green")
        stats_label = ttk.Label(stats_frame, text=linea)
        stats_label.pack()


    def cargar_imagen_izquierda(self, ruta_imagen):
        im.load_left_vertical_image(self.root, ruta_imagen)

    def cargar_imagen_derecha(self, ruta_imagen):
        im.load_right_vertical_image(self.root, ruta_imagen)

    def cargar_pie(self):
        style = ttk.Style()
        footer_height = int(self.root.winfo_screenheight() * 0.1)  # 5% de la altura de la pantalla
        footer_width = int(self.root.winfo_screenwidth())  # 5% de la altura de la pantalla
        style.configure("Footer.TFrame", background="#333333")  # Gris oscuro
        footer_frame = ttk.Frame(self.root, height=footer_height, width=footer_width, relief="solid", style="Footer.TFrame")
        footer_frame.pack(side=tk.BOTTOM)

        self.footer_label = ttk.Label(footer_frame, text="<<<< Presione el botón ❤ >>>>", font=("Arial", 30, "bold"),
                                 foreground="red", background="#333333")
        self.footer_label.place(relx=0.5, rely=0.5, anchor="center")

        self.root.after(10,self.actualizar_pie)


    def actualizar_pie(self):
        texto="<<<< Presione el botón ❤ >>>>"
        #print("texto boton",self.footer_label.cget("text"))
        if self.footer_label.cget("text") == " ":
            self.footer_label.config(text=texto)
        else:
            self.footer_label.config(text=" ")

        self.root.after(500, self.actualizar_pie)


    def set_actualizar_perfil(self,estado):
        self.actualizar_perfil=estado

    def cargar_centro(self):
        # Iniciar el cambio de imágenes
        # Lista de imágenes de la galería
        #main_frame = ttk.Frame(self.root)
        #main_frame.pack()

        #image_urls=self.usuario_random["archivos_galeria"]
        #print(image_urls)
        #main_frame= ttk.Frame(self.root)
        #main_frame.pack()

        #for widget in self.gallery_frame.winfo_children():
        #    widget.destroy()

        window_width = self.root.winfo_screenwidth()  # Obtener el ancho de la pantalla
        window_height = self.root.winfo_screenheight()  # Obtener la altura de la pantalla

        #print("window_width",window_width)
        #print("window_height", window_height)

        if self.actualizar_perfil:
            proporcion_imagen=0.185
            image_size=(int(window_width*proporcion_imagen),int(window_width*proporcion_imagen))

            galeria=gal.galeria_imagenes(self.main_frame)
            galeria.galeria_imagenes(self.usuario_random,self.gallery_frame, self.images_lables,image_size)

        #self.root.after(2000, self.cargar_secciones_datos_usuario)  # Repetir cada x segundo

        #self.gallery_frame.pack_forget()
        #print("type",type(self.gallery_frame))
        #print(self.gallery_frame.winfo_children())

        #img_labels = im.galeria_imagenes(main_frame, image_urls)
        #im.update_gallery_images(image_urls, img_labels, self.root)
