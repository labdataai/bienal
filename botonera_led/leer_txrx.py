import serial
import time

# Configuración del puerto serie
arduino_port = 'COM3'  # Cambia esto al puerto donde está conectado tu Arduino (puede ser COM4, /dev/ttyUSB0, etc.)
baud_rate = 9600        # La misma velocidad que usamos en el Arduino (9600)
timeout_value = 1       # Tiempo de espera para la lectura (en segundos)

# Intentar conectarse al puerto serie
try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=timeout_value)
    print(f"Conectado al puerto {arduino_port}")
except Exception as e:
    print(f"Error al conectar con el puerto {arduino_port}: {e}")
    exit()

# Leer mensajes del puerto serie de manera continua
try:
    while True:
        # Leer una línea del puerto serie
        if arduino.in_waiting > 0:
            message = arduino.readline().decode('utf-8').strip()
            if message:
                print(f"Mensaje recibido: {message}")

        # Dormir brevemente para evitar sobrecargar la CPU
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nFinalizando la conexión...")
finally:
    arduino.close()
    print("Conexión cerrada.")
