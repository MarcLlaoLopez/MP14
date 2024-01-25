#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import shodan

def obtener_informacion_ip():
    ip = ip_entry.get()

    try:
        api = shodan.Shodan(API_KEY)
        resultado = api.host(ip)

        # Obtener los nombres de dominio
        dominios = resultado['hostnames']

        # Obtener los puertos abiertos
        puertos = resultado['ports']

        # Mostrar los resultados en las etiquetas correspondientes
        dominios_label.config(text="Nombres de dominio asociados a la IP:")
        dominios_info.config(text=', '.join(dominios))
        
        puertos_label.config(text="Puertos abiertos:")
        puertos_info.config(text=', '.join(str(puerto) for puerto in puertos))

    except shodan.exception.APIError as e:
        dominios_label.config(text="")
        dominios_info.config(text="")
        puertos_label.config(text="")
        puertos_info.config(text="")
        info_label.config(text=f"Error de la API: {e}")

# Configurar la ventana
root = tk.Tk()
root.title("Obtener Información de IP")

# Configurar la API_KEY (reemplaza con tu clave)
API_KEY = 'UwUYdvRdSltXU2TZySwqLy4QKnQ5GCGi'

# Crear etiqueta y entrada para la IP
ip_label = ttk.Label(root, text="Introduce una dirección IP:")
ip_label.pack(pady=10)
ip_entry = ttk.Entry(root)
ip_entry.pack(pady=10)

# Crear botón para obtener información
obtener_info_button = ttk.Button(root, text="Obtener Información", command=obtener_informacion_ip)
obtener_info_button.pack(pady=10)

# Crear etiquetas para mostrar la información
dominios_label = ttk.Label(root, text="")
dominios_label.pack(pady=5)
dominios_info = ttk.Label(root, text="")
dominios_info.pack(pady=5)

puertos_label = ttk.Label(root, text="")
puertos_label.pack(pady=5)
puertos_info = ttk.Label(root, text="")
puertos_info.pack(pady=5)

info_label = ttk.Label(root, text="")
info_label.pack(pady=10)

root.mainloop()
