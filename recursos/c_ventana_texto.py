import tkinter as tk
from tkinter import ttk
import recursos.c_loading as cl
import recursos.images as im
import recursos.c_ventana_perfil as vp

class ventana_texto(vp.ventana_perfil):

    def cargar_root(self):
        self.root=tk.Toplevel()
        self.ocultar_ventana()

    def cargar_secciones_datos_usuario(self):

        print("Se ejecuto esta")
        self.cargar_seccion_perfil_usuario()
        self.cargar_centro()

    proporcion_centro=2
    def cargar_seccion_perfil_usuario(self):

        self.usuario_random=self.controlador_usuarios.get_usuario_elegido()

        print("usuario_random",self.usuario_random["nombre"])

        imagen_perfil=self.usuario_random["directorio_usuario"]+"/"+self.usuario_random["imagen_perfil"]
        self.imagen_perfil(imagen_perfil)

        #username_label = ttk.Label(self.user_info_frame, text=self.usuario_random["nombre"], font=("Arial", 20, "bold"))
        self.username_label.config(text=self.usuario_random["nombre"])
        self.username_label.pack()

        # Botón de "Editar Perfil"
        #edit_button = ttk.Button(self.user_info_frame, text="Editar Perfil", style="Edit.TButton")
        #edit_button.pack(pady=5)
        #Estilo personalizado para el botón
        #style.configure("Edit.TButton", background="#ffffff", foreground="#333333", bordercolor="#cccccc", borderwidth=1)
        #objetos_graficos.append(profile_image_label)

        # Biografía
        bio_label = ttk.Label(self.header_frame, text=self.usuario_random["descripcion"])
        bio_label.grid(row=2, column=0, columnspan=2, pady=5)

        self.estadisticas_perfil()


    def cargar_centro(self):
        footer_height = int(self.root.winfo_screenheight() * 0.05)
        altura=int( (self.root.winfo_screenheight()-footer_height)/self.proporcion_centro)
        ancho=int(self.root.winfo_screenwidth())
        self.canvas = tk.Canvas(self.root, width=ancho, height=altura, bg="white")

        posicion_y=int((self.root.winfo_screenheight()-footer_height-altura)/2)
        self.canvas.place(y=posicion_y)

        texto=self.controlador_usuarios.seleccionar_texto_perfil_random()
        self.canvas.create_text(ancho // 2, altura // 2,text=texto, font=("Helvetica", 20, "bold"),fill="#333333", anchor="center")
        #self.canvas.pack()

    def start(self):
        self.cargar_secciones_datos_usuario()
        self.root.mainloop()

    def stop(self):
        self.ocultar_ventana()
        #self.root.quit()

    def ocultar_ventana(self):
        self.root.withdraw()  # Oculta la ventana

    def mostrar_ventana(self):
        self.root.deiconify()  # Mostrar la ventana
        #self.start()