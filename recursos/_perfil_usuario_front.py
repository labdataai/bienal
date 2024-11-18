import recursos.images as im
from tkinter import ttk

def estadisticas_perfil(header_frame):
    # Estadísticas del perfil
    stats_frame = ttk.Frame(header_frame)
    stats_frame.grid(row=1, column=0, columnspan=2, pady=10)
    stats_label = ttk.Label(stats_frame, text="164 publicaciones | 188 seguidores | 206 siguiendo")
    stats_label.pack()

def perfil_usuario(header_frame):
    # Cargar la imagen del perfil de forma circular
    profile_image_url = "D:/github/prueba_ventana/imagenes/perfil1.png"
    profile_image = im.load_circular_image(profile_image_url)
    profile_image_label = ttk.Label(header_frame, image=profile_image)
    profile_image_label.image=profile_image
    profile_image_label.grid(row=0, column=0, padx=10)

    user_info_frame = ttk.Frame(header_frame)
    user_info_frame.grid(row=0, column=1, padx=10)
    username_label = ttk.Label(user_info_frame, text="janedoe_", font=("Arial", 20, "bold"))
    username_label.pack()

    # Botón de "Editar Perfil"
    edit_button = ttk.Button(user_info_frame, text="Editar Perfil", style="Edit.TButton")
    edit_button.pack(pady=5)
    # Estilo personalizado para el botón
    #style.configure("Edit.TButton", background="#ffffff", foreground="#333333", bordercolor="#cccccc", borderwidth=1)
    #objetos_graficos.append(profile_image_label)

    estadisticas_perfil(header_frame)

    # Biografía
    bio_label = ttk.Label(header_frame, text="Jane Doe - Lorem ipsum dolor sit")
    bio_label.grid(row=2, column=0, columnspan=2, pady=5)

