

class loading():

    root = None
    canvas= None
    colores = ["#000000", "#2F2F2F", "#555555", "#808080", "#A9A9A9", "#D3D3D3"]
    circulos = []
    color_idx=0
    num_circulos=6
    radio=65
    window_width=0
    window_height=0
    proporcion_centro=2

    def __init__(self,root,canvas):
        self.root=root
        #self.ocultar_ventana()
        self.canvas=canvas
        self.window_width=root.winfo_screenwidth()
        self.window_height=root.winfo_screenheight()

        self.crear_circulos()
        self.actualizar_colores()
        self.mostrar_texto()

    def crear_circulos(self):

        #footer_height = int(self.root.winfo_screenheight() * 0.05)
        #canvas_altura = (self.root.winfo_screenheight() - footer_height) // self.proporcion_centro
        canvas_altura = int(self.root.winfo_screenheight() / 2)
        canvas_posicion_y = int(self.root.winfo_screenheight() / 4)
        #canvas_posicion_y = int((self.root.winfo_screenheight() - footer_height - canvas_altura) / 2)

        #center_y=canvas_posicion_y+(canvas_altura//2)
        center_y = (canvas_altura // 2)
        #center_y = self.window_height // 2
        espaciado = (self.window_width - 2 * self.radio) // (self.num_circulos + 1)
        positions_x = [ espaciado * (i + 1) + self.radio for i in range(self.num_circulos)]

        for i in range(self.num_circulos):
            # Color inicial negro
            circulo = self.canvas.create_oval(positions_x[i] - self.radio, center_y - self.radio,
                                         positions_x[i] + self.radio, center_y + self.radio,
                                         fill="#000000", outline="")  # Negro inicial
            self.circulos.append(circulo)

    def actualizar_colores(self):
        # Colores en degradado: negro -> gris claro

        # Cambiar los colores de los círculos de manera cíclica
        for i in range(self.num_circulos):
            # El color del círculo i se asigna cíclicamente en el array
            self.canvas.itemconfig(self.circulos[i], fill=self.colores[(self.color_idx - i) % len(self.colores)])

        # Actualizar el índice de color para el próximo ciclo
        self.color_idx = (self.color_idx + 1) % len(self.colores)

        # Volver a llamar a esta función cada 300ms para mantener la animación fluida
        self.root.after(300, self.actualizar_colores)

    def mostrar_texto(self):
        #footer_height = int(self.root.winfo_screenheight() * 0.05)
        #canvas_altura = (self.root.winfo_screenheight() - footer_height) // self.proporcion_centro
        #canvas_altura =  self.root.winfo_screenheight() // 3
        #canvas_posicion_y = int((self.root.winfo_screenheight() - canvas_altura) )
        #center_y=canvas_posicion_y#+canvas_altura//2

        canvas_altura = int(self.root.winfo_screenheight() / 2)
        #y_texto=canvas_altura//2+self.radio*2
        y_texto=int(canvas_altura*4/5) #+ self.radio
        #center_y = self.window_height // 2
        texto = self.canvas.create_text(self.window_width // 2, y_texto , text="PROCESANDO...",
                                   font=("Helvetica", 40, "bold"), fill="#333333")


#    def ocultar_ventana(self):
#        self.root.withdraw()

#    def mostrar_ventana(self):
#        self.root.deiconify()
#        self.root.after(5, self.ocultar_ventana())

