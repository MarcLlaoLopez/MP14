import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import socket

class Enum4LinuxApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Enum4Linux GUI")
        self.master.configure(bg="#282a36")

        # Obtener la IP local
        self.ip = self.obtener_ip_local()

        # Etiqueta para mostrar la IP local
        self.ip_label = ttk.Label(master, text=f"Tu dirección IP local es: {self.ip}", background="#282a36", foreground="#f8f8f2", font=("Helvetica", 12, "bold"))
        self.ip_label.pack(pady=10)

        # Botón para ejecutar enum4linux
        self.ejecutar_button = ttk.Button(master, text="Ejecutar enum4linux", command=self.ejecutar_enum4linux, style="TButton")
        self.ejecutar_button.pack(pady=10)

        # Etiqueta para mostrar el mensaje
        self.resultado_label = ttk.Label(master, text="", wraplength=500, justify="left", background="#282a36", foreground="#f8f8f2", font=("Helvetica", 10))
        self.resultado_label.pack(pady=10)

        # Botón de salida
        self.boton_salir = ttk.Button(master, text="Salir", command=self.salir, style="TButton")
        self.boton_salir.pack(pady=10)

    def obtener_ip_local(self):
        try:
            # Crear un socket UDP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))  # Conectar al servidor de Google DNS
            ip = s.getsockname()[0]  # Obtener la IP local
            s.close()
            return ip
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener la dirección IP local: {e}")
            return ""

    def ejecutar_enum4linux(self):
        try:
            command = f"enum4linux -a -o {self.ip}"  # Agregué la opción -a y un espacio después de -o
            resultado = subprocess.run(command, shell=True, capture_output=True, text=True)
            self.resultado_label.config(text="El resultado se visualiza en el terminal.")
            print(resultado.stdout)
        except subprocess.CalledProcessError as e:
            self.resultado_label.config(text=f"Error al ejecutar el comando enum4linux: {e}")
        except Exception as e:
            self.resultado_label.config(text=f"Ocurrió un error: {e}")

    def salir(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = Enum4LinuxApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
