import tkinter as tk


# Función para cambiar los colores de los círculos, creando el efecto "loading"
def actualizar_colores():
    global color_idx
    # Colores en degradado: negro -> gris claro
    colores = ["#000000", "#2F2F2F", "#555555", "#808080", "#A9A9A9", "#D3D3D3"]

    # Cambiar los colores de los círculos de manera cíclica
    for i in range(num_circulos):
        # El color del círculo i se asigna cíclicamente en el array
        canvas.itemconfig(circulos[i], fill=colores[(color_idx + i) % len(colores)])

    # Actualizar el índice de color para el próximo ciclo
    color_idx = (color_idx + 1) % len(colores)

    # Volver a llamar a esta función cada 300ms para mantener la animación fluida
    root.after(300, actualizar_colores)


# Crear la ventana principal
root = tk.Tk()
root.title("Loading Animation")

# Definir las dimensiones de la ventana (utilizar toda la resolución disponible)
window_width = root.winfo_screenwidth()  # Obtener el ancho de la pantalla
window_height = 400  # Altura fija
root.geometry(f"{window_width}x{window_height}")

# Crear un canvas para dibujar los círculos
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white")
canvas.pack()

# Coordenadas de los círculos (fijos en el centro vertical de la ventana)
center_y = window_height // 2
radio = 50

# Número de círculos
num_circulos = 6

# Calcular la distancia horizontal entre los círculos (utilizando el ancho completo de la ventana)
espaciado = (window_width - 2 * radio) // (num_circulos + 1)

# Posiciones horizontales de los círculos (equidistantes)
positions_x = [espaciado * (i + 1) + radio for i in range(num_circulos)]

# Crear los círculos en el canvas (sin contorno)
circulos = []
for i in range(num_circulos):
    # Color inicial negro
    circulo = canvas.create_oval(positions_x[i] - radio, center_y - radio,
                                 positions_x[i] + radio, center_y + radio,
                                 fill="#000000", outline="")  # Negro inicial
    circulos.append(circulo)

# Variable global para mantener el índice de los colores
color_idx = 0

# Iniciar la animación
actualizar_colores()

# Ejecutar el bucle principal
root.mainloop()