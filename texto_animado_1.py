import tkinter as tk


# Función para animar el texto
def animar_texto():
    global index_linea
    if index_linea < len(lineas):
        # Mostrar la siguiente línea de texto
        canvas.create_text(window_width, window_height // 2 + (index_linea * 40), text=lineas[index_linea],
                           font=("Helvetica", 30, "bold"), fill="#333333", anchor="w")
        index_linea += 1

    # Mover todas las líneas de texto hacia la izquierda
    for item in canvas.find_all():
        canvas.move(item, -10, 0)  # Mover todos los textos 10 píxeles a la izquierda

    # Repetir la animación cada 100ms
    root.after(100, animar_texto)


# Crear la ventana principal
root = tk.Tk()
root.title("Texto Animado")

# Configurar la ventana para que ocupe toda la pantalla
window_width = root.winfo_screenwidth()  # Obtener el ancho de la pantalla
window_height = root.winfo_screenheight()  # Obtener la altura de la pantalla
root.geometry(f"{window_width}x{window_height}+0+0")  # Establecer tamaño de la ventana
root.overrideredirect(True)  # Eliminar la barra de título y bordes (pantalla completa)

# Crear un canvas para dibujar el texto
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white")
canvas.pack()

# Texto dividido en líneas
lineas = [
    "Este es un texto de ejemplo",
    "que aparece palabra por palabra.",
    "Cada línea se moverá",
    "de derecha a izquierda.",
    "¡Aquí vamos!"
]

# Variable para llevar el control de la línea que se muestra
index_linea = 0

# Iniciar la animación
animar_texto()

# Ejecutar el bucle principal
root.mainloop()