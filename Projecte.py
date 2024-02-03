import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import os

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Projecte")
        self.configure(bg="#282a36")

        # Mostrar mensaje de bienvenida en el centro
        mensaje_bienvenida = tk.Label(self, text="Bienvenidos a CyberPrawns", bg="#282a36", fg="#f8f8f2", font=("Helvetica", 16, "bold"))
        mensaje_bienvenida.pack(expand=True, pady=50)

        # Crear contenedor para los botones de operaciones
        self.contenedor_botones = tk.Frame(self, bg="#282a36")
        self.contenedor_botones.pack(expand=True, padx=50, pady=20)

        # Botón para la consulta a la API de Shodan
        self.boton_api_shodan = ttk.Button(self.contenedor_botones, text="Consulta API SHODAN", command=self.mostrar_opciones_shodan, style="TButton")
        self.boton_api_shodan.pack(fill=tk.X, pady=5)

        # Botones de otras operaciones
        self.boton_ennumeracio = ttk.Button(self.contenedor_botones, text="Ennumeració", command=self.abrir_ennumeracio, style="TButton")
        self.boton_ennumeracio.pack(fill=tk.X, pady=5)

        self.boton_escaneig = ttk.Button(self.contenedor_botones, text="Escaneig", command=self.abrir_escaneig, style="TButton")
        self.boton_escaneig.pack(fill=tk.X, pady=5)

        self.boton_sshaudit = ttk.Button(self.contenedor_botones, text="SSHAudit", command=self.abrir_sshaudit, style="TButton")
        self.boton_sshaudit.pack(fill=tk.X, pady=5)

        self.boton_acerca_de = ttk.Button(self.contenedor_botones, text="Acerca de", command=self.abrir_acerca_de, style="TButton")
        self.boton_acerca_de.pack(fill=tk.X, pady=5)

        self.estilo_botones()

    def estilo_botones(self):
        style = ttk.Style()
        style.configure("TButton", foreground="#f8f8f2", background="#44475a", font=("Helvetica", 12, "bold"))

    def abrir_ennumeracio(self):
        try:
            programa = "Ennumeració/Ennumeració.py"
            if os.path.exists(programa):
                subprocess.Popen(["python3", programa])
            else:
                messagebox.showerror("Error", "El programa de enumeración no se encuentra.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el programa: {e}")

    def abrir_escaneig(self):
        try:
            programa = "Escaneig/escaneig.py"
            if os.path.exists(programa):
                subprocess.Popen(["python3", programa])
            else:
                messagebox.showerror("Error", "El programa de escaneo no se encuentra.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el programa: {e}")

    def abrir_sshaudit(self):
        try:
            programa = "SSH_Audit/ssh_audit.py"
            if os.path.exists(programa):
                subprocess.Popen(["python3", programa])
            else:
                messagebox.showerror("Error", "El programa de auditoría SSH no se encuentra.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el programa: {e}")

    def abrir_acerca_de(self):
        messagebox.showinfo("Acerca de", "Esta aplicación ha sido desarrollada por Los CyberPrawns.")

    def mostrar_opciones_shodan(self):
        opciones = [
            ("Preguntar IP y mostrar información", "Consulta_API_Shodan/Consulta_API_Shodan1.py"),
            ("Mostrar únicamente los nombres de dominio", "Consulta_API_Shodan/Consulta_API_Shodan2.py"),
            ("Qué servicio hay en cada uno de los puertos abiertos", "Consulta_API_Shodan/Consulta_API_Shodan3.py"),
            ("Escribe el nombre de un servicio", "Consulta_API_Shodan/Consulta_API_Shodan4.py")
        ]
        menu = tk.Menu(self, tearoff=0)
        for texto, programa in opciones:
            menu.add_command(label=texto, command=lambda p=programa: subprocess.Popen(["python3", p]))
        self.boton_api_shodan.bind("<Button-1>", lambda event: menu.post(event.x_root, event.y_root))

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
