import tkinter as tk


# Función para animar el texto, haciéndolo crecer desde el centro
def animar_texto():
    global tamaño_fuente

    # Aumentar el tamaño de la fuente poco a poco
    if tamaño_fuente < tamaño_final:
        tamaño_fuente += 2  # Aumentamos el tamaño de la fuente
        # Limpiar el canvas y crear el texto con el nuevo tamaño
        canvas.delete("all")
        canvas.create_text(window_width // 2, window_height // 2, text=texto, font=("Helvetica", tamaño_fuente, "bold"),
                           fill="#333333", anchor="center")

        # Repetir la animación después de 50ms
        root.after(50, animar_texto)


# Crear la ventana principal
root = tk.Tk()
root.title("Texto Animado: Agrandado")

# Configurar la ventana para que ocupe toda la pantalla
window_width = root.winfo_screenwidth()  # Obtener el ancho de la pantalla
window_height = root.winfo_screenheight()  # Obtener la altura de la pantalla
root.geometry(f"{window_width}x{window_height}+0+0")  # Establecer tamaño de la ventana
root.overrideredirect(True)  # Eliminar la barra de título y bordes (pantalla completa)

# Crear un canvas para dibujar el texto
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="white")
canvas.pack()

# Texto a mostrar
texto = "Este es el texto que crece."

# Tamaño inicial y tamaño final de la fuente
tamaño_fuente = 10
tamaño_final = 80  # Tamaño final del texto

# Iniciar la animación
animar_texto()

# Ejecutar el bucle principal
root.mainloop()