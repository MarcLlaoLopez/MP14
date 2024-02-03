import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
import subprocess

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SSH Audit")
        self.configure(bg="#282a36")
        
        # Crear contenedor para los botones
        self.contenedor_botones = tk.Frame(self, bg="#282a36")
        self.contenedor_botones.pack(expand=True)

        self.boton_1 = ttk.Button(self.contenedor_botones, text="Escanejar amb opcions bàsiques", command=self.ejecutar_opcion1, style="TButton")
        self.boton_1.pack(pady=10)

        self.boton_2 = ttk.Button(self.contenedor_botones, text="Escanejar amb opcions personalitzades", command=self.ejecutar_opcion2, style="TButton")
        self.boton_2.pack(pady=10)

        self.boton_3 = ttk.Button(self.contenedor_botones, text="Ajuda", command=self.mostrar_ajuda, style="TButton")
        self.boton_3.pack(pady=10)

        self.boton_4 = ttk.Button(self.contenedor_botones, text="Sortir", command=self.destroy, style="TButton")
        self.boton_4.pack(pady=10)

    def ejecutar_opcion1(self):
        host = simpledialog.askstring("Host", "Introdueix el nom d'amfitrió o la direcció IP del servidor SSH:")
        if host:
            self.ejecutar_ssh_audit(host)

    def ejecutar_opcion2(self):
        host = simpledialog.askstring("Host", "Introdueix el nom d'amfitrió o la direcció IP del servidor SSH:")
        if host:
            custom_options = simpledialog.askstring("Opcions personalitzades", "Introdueix les opcions personalitzades (separades per espais):")
            if custom_options is not None:
                self.ejecutar_ssh_audit(host, custom_options)

    def mostrar_ajuda(self):
        mensaje_ayuda = "Esta herramienta permite escanear la seguridad de un servidor SSH.\n\n" \
                    "Opciones disponibles:\n" \
                    "- Escanejar con opciones básicas: Realiza un escaneo simple sin opciones personalizadas.\n" \
                    "- Escanejar con opciones personalizadas: Permite especificar opciones personalizadas para ssh-audit.\n" \
                    "- Sortir: Finaliza la aplicación."
        messagebox.showinfo("Ajuda", mensaje_ayuda)


    def ejecutar_ssh_audit(self, host, custom_options=None):
        try:
            command = ["ssh-audit", host]
            if custom_options:
                command.extend(custom_options.split())
            subprocess.run(command, check=True)
        except FileNotFoundError:
            messagebox.showerror("Error", "ssh-audit no està instal·lat. Si us plau, instal·la-ho abans de continuar.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error al executar ssh-audit: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperat: {e}")

# Crear la ventana principal
app = VentanaPrincipal()
app.mainloop()
