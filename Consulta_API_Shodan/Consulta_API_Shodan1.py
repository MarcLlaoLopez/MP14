#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import shodan

def obtener_informacion_ip():
    ip = ip_entry.get()

    try:
        api = shodan.Shodan(API_KEY)
        resultado = api.host(ip)

        info_label.config(text=f"IP: {resultado['ip_str']}\n"
                                f"País: {resultado['country_name']}\n"
                                f"Organización: {resultado.get('org', 'No disponible')}\n"
                                f"Ports abiertos: {', '.join(str(port) for port in resultado['ports'])}")
    except shodan.exception.APIError as e:
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

# Crear etiqueta para mostrar la información
info_label = ttk.Label(root, text="")
info_label.pack(pady=10)

root.mainloop()
