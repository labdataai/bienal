#https://github.com/MrYsLab/microbit-robot/blob/master/remote_controllers/gui_controllers/tkinter/tk_controller.py

#device="MMI0"

import serial

serial_port = serial.Serial(port = "COM3", baudrate = 9600)
serial_port.readline()

