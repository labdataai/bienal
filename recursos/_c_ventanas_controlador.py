import recursos.c_usuario_controlador as cu
import recursos.c_ventana_perfil as vp
import recursos.c_ventana_loading as vl
import recursos.c_ventana_texto as vt
import serial
import time

class c_ventanas_controllador():

    control_usuarios=None
    ventana_perfil=None
    ventana_loading=None
    ventana_texto=None
    estado_ventana_loading=False
    serial_port=None

    milisegundos_ventana_loading=5000

    def __init__(self):

        self.control_usuarios=cu.usuario_controlador()
        self.control_usuarios.cargar_usuarios()

        self.ventana_perfil=vp.ventana_perfil(self.control_usuarios)
        #self.ventana_perfil.set_enter_key(self.tecla_enter_ventana_perfil)

        self.ventana_loading = vl.ventana_loading()

        self.ventana_texto = vt.ventana_texto(self.control_usuarios)
        #self.ventana_texto.set_enter_key(self.tecla_enter_ventana_texto)

        self.serial_port = serial.Serial(port="COM3", baudrate=115200, timeout=.1)

    def leer_puerto_serie(self,ser):
        data = ""
        while data == "":
            if self.serial_port.in_waiting > 0:  # Verifica si hay datos disponibles
                data = self.serial_port.read(ser.in_waiting)  # Lee todos los datos disponibles
                print("Datos recibidos:", data)

            time.sleep(0.1)

    def tecla_enter_ventana_perfil(self,event):
        print("Tecla enter")
        if (self.estado_ventana_loading==False):
            #self.estado_ventana_loading=True
            #print(type(self.ventana_loading))
            self.ventana_perfil.set_actualizar_perfil(False)
            self.ventana_loading.mostrar_ventana_tiempo(self.milisegundos_ventana_loading)
            #self.ventana_texto
            self.ventana_texto.mostrar_ventana()
            self.ventana_texto.start()

            #self.ventana_loading.start()
        #else:
        #    self.estado_ventana_loading = False
        #    self.ventana_loading.ocultar_ventana()


    def tecla_enter_ventana_texto(self,event):
        self.ventana_texto.ocultar_ventana()
        self.ventana_perfil.set_actualizar_perfil(True)

    def main(self):
        self.ventana_perfil.start()


