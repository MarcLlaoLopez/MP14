#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import shodan

def buscar_ips_por_servicio():
    servicio = servicio_entry.get()

    try:
        api = shodan.Shodan(API_KEY)
        resultados = api.search(f"product:{servicio}")

        # Limpiar resultados anteriores
        resultados_text.delete('1.0', tk.END)

        # Mostrar información de las IPs y puertos
        resultados_text.insert(tk.END, f"Resultados para el servicio '{servicio}':\n")
        for resultado in resultados['matches']:
            resultados_text.insert(tk.END, f"IP: {resultado['ip_str']} - Puerto: {resultado['port']}\n")

    except shodan.exception.APIError as e:
        resultados_text.delete('1.0', tk.END)
        resultados_text.insert(tk.END, f"Error de la API: {e}")

# Configurar la ventana
root = tk.Tk()
root.title("Buscar IPs por Servicio")

# Configurar la API_KEY (reemplaza con tu clave)
API_KEY = 'UwUYdvRdSltXU2TZySwqLy4QKnQ5GCGi'

# Crear etiqueta y entrada para el nombre del servicio
servicio_label = ttk.Label(root, text="Introduce el nombre del servicio (por ejemplo, proftpd):")
servicio_label.pack(pady=10)
servicio_entry = ttk.Entry(root)
servicio_entry.pack(pady=10)

# Crear botón para buscar IPs por servicio
buscar_button = ttk.Button(root, text="Buscar IPs por Servicio", command=buscar_ips_por_servicio)
buscar_button.pack(pady=10)

# Crear un área de texto para mostrar los resultados
resultados_text = tk.Text(root, height=10, width=50)
resultados_text.pack(pady=10)

root.mainloop()
