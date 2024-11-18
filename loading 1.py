import tkinter as tk


# Función para cambiar los colores de los círculos y moverlos horizontalmente
def actualizar_colores_y_posiciones():
    global color_idx, positions
    # Lista de colores que se van a utilizar en el degradado
    colores = ["#FF5733", "#FF8D1A", "#FFDF00", "#33FF57", "#33A1FF"]

    # Cambiar los colores de los círculos
    for i in range(5):
        canvas.itemconfig(circulos[i], fill=colores[(color_idx + i) % len(colores)])

    # Actualizar las posiciones horizontales de los círculos
    for i in range(5):
        new_x = positions[i] + 5  # Aumentar la posición x para mover los círculos hacia la derecha
        if new_x > window_width:  # Si un círculo sale de la pantalla, lo devolvemos al principio
            new_x = -radio * 2
        positions[i] = new_x
        canvas.coords(circulos[i], new_x - radio, center_y - radio, new_x + radio, center_y + radio)

    # Actualizar el índice de color
    color_idx = (color_idx + 1) % len(colores)

    # Volver a llamar a esta función cada 50ms para la animación continua
    root.after(50, actualizar_colores_y_posiciones)


# Crear la ventana principal
root = tk.Tk()
root.title("Loading Animation")

# Definir las dimensiones de la ventana
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Crear un canvas para dibujar los círculos
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white")
canvas.pack()

# Coordenadas y parámetros de los círculos
center_y = window_height // 2
radio = 30
espaciado = 15  # Espacio entre los círculos

# Inicializar las posiciones horizontales de los círculos
positions = [-2 * radio, -radio * 1.5, -radio, -radio / 2, 0]  # Posiciones iniciales fuera de la pantalla

# Crear los círculos en el canvas (sin contorno)
circulos = []
for i in range(5):
    circulo = canvas.create_oval(positions[i] - radio, center_y - radio,
                                 positions[i] + radio, center_y + radio,
                                 fill="#FFFFFF", outline="")  # Sin contorno
    circulos.append(circulo)

# Variable global para mantener el índice de los colores
color_idx = 0

# Iniciar la animación
actualizar_colores_y_posiciones()

# Ejecutar el bucle principal
root.mainloop()