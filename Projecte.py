import tkinter as tk
import subprocess

def funcion_1():

    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("API Shodan")
    print("Mostrando opciones API Shodan")
    def funcion_1_api():
        try:
            # Ruta al programa externo que deseas ejecutar
            programa = "Consulta_API_Shodan/Consulta_API_Shodan1.py"  

            # Ejecuta el programa
            subprocess.Popen([programa])

            

        except Exception as e:
            print("Error al abrir el programa:", str(e))

    def funcion_2_api():
        try:
            # Ruta al programa externo que deseas ejecutar
            programa = "Consulta_API_Shodan/Consulta_API_Shodan2.py"  

            # Ejecuta el programa
            subprocess.Popen([programa])

        except Exception as e:
            print("Error al abrir el programa:", str(e))
    def funcion_3_api():
        try:
            # Ruta al programa externo que deseas ejecutar
            programa = "Consulta_API_Shodan/Consulta_API_Shodan3.py"  

            # Ejecuta el programa
            subprocess.Popen([programa])

        except Exception as e:
            print("Error al abrir el programa:", str(e))

    def funcion_4_api():
        try:
            # Ruta al programa externo que deseas ejecutar
            programa = "Consulta_API_Shodan/Consulta_API_Shodan4.py"  

            # Ejecuta el programa
            subprocess.Popen([programa])

        except Exception as e:
            print("Error al abrir el programa:", str(e))

    boton_1_api = tk.Button(ventana_emergente, text="Preguntar IP y mostrar información", command=funcion_1_api)
    boton_2_api = tk.Button(ventana_emergente, text="Mostrar unicamente los nombres de dominio", command=funcion_2_api)
    boton_3_api = tk.Button(ventana_emergente, text="Que servicio hay en cada uno de los puertos abiertos", command=funcion_3_api)
    boton_4_api = tk.Button(ventana_emergente, text="Escribe el nombre de un servicio", command=funcion_4_api)

    boton_1_api.pack(pady=10)
    boton_2_api.pack(pady=10)
    boton_3_api.pack(pady=10)
    boton_4_api.pack(pady=10)

def abrir_ventana_emergente():
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Ennumeració")
    print("Ennumeració")

    def ennumeracio():
        try:
            # Ruta al programa externo que deseas ejecutar
            programa = "Ennumeració/Ennumeració.py"  

            # Ejecuta el programa
            subprocess.Popen(["python3", programa])

        except Exception as e:
            print("Error al abrir el programa:", str(e))

    boton_ennumeracio = tk.Button(ventana_emergente, text="Preguntar IP y mostrar información", command=ennumeracio)
    boton_ennumeracio.pack(pady=10)

def ventana():
    ventana = tk.Toplevel
    ventana.title("Escaneig")
    

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Projecte")

# Crear botones
boton_1 = tk.Button(ventana, text="Abrir Consulta API SHODAN", command=funcion_1)
boton_2 = tk.Button(ventana, text="Ennumeració", command=abrir_ventana_emergente)

boton_1.pack(pady=10)
boton_2.pack(pady=10)

# Inicia el bucle principal de la aplicación
ventana.mainloop()
