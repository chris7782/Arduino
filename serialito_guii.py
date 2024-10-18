import tkinter as GUI
import serial
import time

ventana = GUI.Tk()
arduino = None  # Definir arduino como variable global

def conectar():
    global arduino
    Puerto = Entrycom.get()
    try:
        arduino = serial.Serial(port=Puerto, baudrate=115200, timeout=.1)
        print("Conectado a", Puerto)
    except:
        print("Error al conectar")

def SEND():
    global arduino
    if arduino and arduino.is_open:
        x = spindata.get()
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        data = arduino.readline().decode('utf-8').strip()
        Labelrecive.config(text=f"Dato recibido = {data}")
    else:
        print("No está conectado")

def Cerrar():
    global arduino
    if arduino and arduino.is_open:
        arduino.close()
    ventana.destroy()

# Configuración de la ventana y widgets
labelcom_name = GUI.Label(text="Escribe el nombre del puerto:")
Entrycom = GUI.Entry(ventana)
Botonconet = GUI.Button(ventana, text="Conectar", command=conectar)
spindata = GUI.Spinbox(ventana, from_=0, to=10)
Botonsend = GUI.Button(ventana, text="Enviar", command=SEND)
Labelrecive = GUI.Label(ventana, text="Dato recibido:")
BotonCerrar = GUI.Button(ventana, text="Salir", command=Cerrar)

# Disposición en la ventana
labelcom_name.pack(padx=1, pady=2)
Entrycom.pack(padx=1, pady=2)
Botonconet.pack(padx=1, pady=2)
spindata.pack(padx=1, pady=2)
Botonsend.pack(padx=1, pady=2)
Labelrecive.pack(padx=1, pady=2)
BotonCerrar.pack(padx=1, pady=2)

ventana.mainloop()
