# Autor: Nicolas Luengas
# 15/05/2026
# Requerimentos:
# - pyserial
# - keyboard

import serial
import keyboard
import time
import serial.tools.list_ports
from tkinter import messagebox

action = {
  "camara": "ctrl+e",
  "micro": "ctrl+d",
  "mano": "ctrl+alt+h",
  }

connection = ""
#portcount = 1
def trycon():
    global connection
    ports = serial.tools.list_ports.comports()
    chips = ["CP210", "CH340", "FTDI", "USB Serial", "FT232", "USB Serial Port"]
    for port in ports:
        port_desc = port.description.upper()
        hwid = port.hwid.upper()
        for chip in chips:
            if chip.upper() in port_desc or chip.upper() in hwid:
                connection = serial.Serial(port=port.device, baudrate=115200, timeout=.1) 
                return True
    return False

def read():
        global connection 
        time.sleep(0.05) 
        data = connection.readline() 
        return str(data)

### INIT ZONE
if __name__ == '__main__':
    messagebox.showinfo("Asistente de Google Meet", "Conecte su Asistente de Google Meet a su PC")
    if trycon():
            messagebox.showinfo("Asistente de Google Meet", "Dispositivo detectado, ejecutandose en segundo plano.")
    else:
            messagebox.showinfo("Asistente de Google Meet", "Ocurrio un error, intentelo de nuevo o no lo intente y no lo use lo.")
            exit()
while True:
        value = read() 
        if "camera" in value:
            print("Camara")
            keyboard.send(action["camara"])
        if "microp" in value:
            print("Microfono")
            keyboard.send(action["micro"])
        if "handup" in value:
            print("Accionar mano")
            keyboard.send(action["mano"])

        #if "discco" in value:
        #    print("Desconectarse")
        

