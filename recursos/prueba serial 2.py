import serial
import time
import threading
# Función para leer los datos del puerto serie

def leer_puerto_serie(ser):
    data=""
    while True:

        if ser.in_waiting > 0:  # Verifica si hay datos disponibles
            data = ser.read(ser.in_waiting)  # Lee todos los datos disponibles
            print("Datos recibidos:", data.decode(encoding='UTF-8'))
            #
        time.sleep(0.1)  # Añadir una pequeña espera para no sobrecargar el CPU

# Configura el puerto serie
#puerto = '/dev/ttyUSB0'  # En sistemas Linux (ajustar según el puerto en tu caso)
puerto = 'COM3'  # En Windows (ajustar según el puerto en tu caso)
baudrate = 9600


ser = serial.Serial(puerto, baudrate, timeout=0.1)

leer_puerto_serie(ser)


