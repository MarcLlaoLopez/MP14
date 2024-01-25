#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import subprocess

def ejecutar_enum4linux():
    ip = ip_entry.get()

    try:
        command = f"enum4linux -a -o {ip}"  # Agregué la opción -a y un espacio después de -o
        resultado = subprocess.run(command, shell=True, capture_output=True, text=True)
        resultado_label.config(text="El resultado se visualiza en el terminal.")
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        resultado_label.config(text=f"Error al ejecutar el comando enum4linux: {e}")
    except Exception as e:
        resultado_label.config(text=f"Ocurrió un error: {e}")

# Configurar la ventana
root = tk.Tk()
root.title("Enum4Linux GUI")

# Etiqueta y entrada para la IP
ip_label = ttk.Label(root, text="Introduce la dirección IP:")
ip_label.pack(pady=10)
ip_entry = ttk.Entry(root)
ip_entry.pack(pady=10)

# Botón para ejecutar enum4linux
ejecutar_button = ttk.Button(root, text="Ejecutar enum4linux", command=ejecutar_enum4linux)
ejecutar_button.pack(pady=10)

# Etiqueta para mostrar el mensaje
resultado_label = ttk.Label(root, text="", wraplength=500, justify="left")
resultado_label.pack(pady=10)

root.mainloop()
