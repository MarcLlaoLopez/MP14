import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter.scrolledtext import ScrolledText
import subprocess

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Escaneo de red")
        self.configure(bg="#282a36")

        # Estilo
        self.estilo = ttk.Style()
        self.estilo.configure("Titulo.TLabel", background="#282a36", foreground="#f8f8f2", font=("Helvetica", 16, "bold"))

        # Mostrar mensaje de bienvenida en el centro
        mensaje_bienvenida = ttk.Label(self, text="Bienvenidos a CyberPrawns", style="Titulo.TLabel")
        mensaje_bienvenida.pack(expand=True, pady=20)

        # Crear contenedor para los botones
        self.contenedor_botones = tk.Frame(self, bg="#282a36")
        self.contenedor_botones.pack(expand=True, padx=50, pady=20)

        self.boton_descubrir_hosts = ttk.Button(self.contenedor_botones, text="Descubrir hosts", command=self.descobrir_hosts, style="TButton")
        self.boton_descubrir_hosts.pack(fill=tk.X, pady=5)

        self.boton_escanear_puertos = ttk.Button(self.contenedor_botones, text="Escanear puertos", command=self.escanear_puertos, style="TButton")
        self.boton_escanear_puertos.pack(fill=tk.X, pady=5)

        self.boton_listar_servicios = ttk.Button(self.contenedor_botones, text="Listar servicios y versiones", command=self.listar_servicios, style="TButton")
        self.boton_listar_servicios.pack(fill=tk.X, pady=5)

        self.boton_listar_vulnerabilidades = ttk.Button(self.contenedor_botones, text="Listar vulnerabilidades", command=self.listar_vulnerabilidades, style="TButton")
        self.boton_listar_vulnerabilidades.pack(fill=tk.X, pady=5)

        self.boton_salir = ttk.Button(self.contenedor_botones, text="Salir", command=self.destroy, style="TButton")
        self.boton_salir.pack(fill=tk.X, pady=10)

        self.estilo_botones()

    def estilo_botones(self):
        style = ttk.Style()
        style.configure("TButton", foreground="#f8f8f2", background="#44475a", font=("Helvetica", 12, "bold"))

    def descobrir_hosts(self):
        ip = self.obtener_ip()
        if ip:
            try:
                proceso = subprocess.Popen(["nmap", "-sn", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                resultado, error = proceso.communicate()
                if resultado:
                    resultado_filtrado = self.filtrar_salida(resultado)
                    self.mostrar_resultado(resultado_filtrado)
                elif error:
                    self.mostrar_error(error)
            except Exception as e:
                self.mostrar_error(str(e))

    def escanear_puertos(self):
        ip = self.obtener_ip()
        puertos = self.obtener_puertos()
        if ip and puertos:
            try:
                proceso = subprocess.Popen(["nmap", "-p", puertos, ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                resultado, error = proceso.communicate()
                if resultado:
                    resultado_filtrado = self.filtrar_salida(resultado)
                    self.mostrar_resultado(resultado_filtrado)
                elif error:
                    self.mostrar_error(error)
            except Exception as e:
                self.mostrar_error(str(e))

    def listar_servicios(self):
        ip = self.obtener_ip()
        puertos = self.obtener_puertos()
        if ip and puertos:
            try:
                proceso = subprocess.Popen(["nmap", "-p", puertos, "-A", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                resultado, error = proceso.communicate()
                if resultado:
                    resultado_filtrado = self.filtrar_salida(resultado)
                    self.mostrar_resultado(resultado_filtrado)
                elif error:
                    self.mostrar_error(error)
            except Exception as e:
                self.mostrar_error(str(e))

    def listar_vulnerabilidades(self):
        ip = self.obtener_ip()
        puertos = self.obtener_puertos()
        if ip and puertos:
            try:
                opciones = ["-p", puertos, "--script", "vuln", ip]
                proceso = subprocess.Popen(["nmap"] + opciones, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                resultado, error = proceso.communicate()
                if resultado:
                    resultado_filtrado = self.filtrar_salida(resultado)
                    self.mostrar_resultado(resultado_filtrado)
                elif error:
                    self.mostrar_error(error)
            except Exception as e:
                self.mostrar_error(str(e))

    def obtener_ip(self):
        ip = simpledialog.askstring("Dirección IP", "Introduzca la dirección IP o red a escanear:")
        return ip

    def obtener_puertos(self):
        puertos = simpledialog.askstring("Puertos", "Introduzca los puertos a escanear (ejemplo: 80-100):")
        return puertos

    def filtrar_salida(self, resultado):
        lineas = resultado.split('\n')
        lineas_filtradas = [linea for linea in lineas if not linea.startswith(("Starting", "Nmap", "Host", "PORT"))]
        return '\n'.join(lineas_filtradas)

    def mostrar_resultado(self, resultado):
        ventana_resultado = tk.Toplevel(self)
        ventana_resultado.title("Resultado")
        ventana_resultado.geometry("600x400")

        cuadro_texto = ScrolledText(ventana_resultado, wrap=tk.WORD, font=("Helvetica", 12))
        cuadro_texto.insert(tk.END, resultado)
        cuadro_texto.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def mostrar_error(self, error):
        messagebox.showerror("Error", error)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()



"""import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Escaneo de red")
        self.configure(bg="#282a36")
        
        # Estilo
        self.estilo = ttk.Style()
        self.estilo.configure("Titulo.TLabel", background="#282a36", foreground="#f8f8f2", font=("Helvetica", 16, "bold"))

        # Mostrar mensaje de bienvenida en el centro
        mensaje_bienvenida = ttk.Label(self, text="Bienvenidos a CyberPrawns", style="Titulo.TLabel")
        mensaje_bienvenida.pack(expand=True, pady=20)
        
        # Crear contenedor para los botones
        self.contenedor_botones = tk.Frame(self, bg="#282a36")
        self.contenedor_botones.pack(expand=True, padx=50, pady=20)

        self.boton_descubrir_hosts = ttk.Button(self.contenedor_botones, text="Descubrir hosts", command=self.descobrir_hosts, style="TButton")
        self.boton_descubrir_hosts.pack(fill=tk.X, pady=5)

        self.boton_escanear_puertos = ttk.Button(self.contenedor_botones, text="Escanear puertos", command=self.escanear_puertos, style="TButton")
        self.boton_escanear_puertos.pack(fill=tk.X, pady=5)

        self.boton_listar_servicios = ttk.Button(self.contenedor_botones, text="Listar servicios y versiones", command=self.listar_servicios, style="TButton")
        self.boton_listar_servicios.pack(fill=tk.X, pady=5)

        self.boton_listar_vulnerabilidades = ttk.Button(self.contenedor_botones, text="Listar vulnerabilidades", command=self.listar_vulnerabilidades, style="TButton")
        self.boton_listar_vulnerabilidades.pack(fill=tk.X, pady=5)

        self.boton_salir = ttk.Button(self.contenedor_botones, text="Salir", command=self.destroy, style="TButton")
        self.boton_salir.pack(fill=tk.X, pady=10)

        self.estilo_botones()
    
    def estilo_botones(self):
        style = ttk.Style()
        style.configure("TButton", foreground="#f8f8f2", background="#44475a", font=("Helvetica", 12, "bold"))

    def descobrir_hosts(self):
        ip = self.obtener_ip()
        try:
            resultado = subprocess.check_output(["nmap", "-sn", ip])
            messagebox.showinfo("Resultado", resultado.decode("utf-8"))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def escanear_puertos(self):
        ip = self.obtener_ip()
        puertos = self.obtener_puertos()
        try:
            resultado = subprocess.check_output(["nmap", "-p", puertos, ip])
            messagebox.showinfo("Resultado", resultado.decode("utf-8"))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def listar_servicios(self):
        ip = self.obtener_ip()
        puertos = self.obtener_puertos()
        try:
            resultado = subprocess.check_output(["nmap", "-p", puertos, "-A", ip])
            messagebox.showinfo("Resultado", resultado.decode("utf-8"))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def listar_vulnerabilidades(self):
        ip = self.obtener_ip()
        puertos = self.obtener_puertos()
        try:
            opciones = ["-p", puertos, "--script", "vuln", ip]
            resultado = subprocess.check_output(["nmap"] + opciones)
            messagebox.showinfo("Resultado", resultado.decode("utf-8"))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def obtener_ip(self):
        return "127.0.0.1"  # Cambia esto por una entrada real del usuario

    def obtener_puertos(self):
        return "80-100"  # Cambia esto por una entrada real del usuario

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()"""
