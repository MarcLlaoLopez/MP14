import subprocess

def main():
    print("Benvingut a l'eina de revisió de seguretat SSH-audit")
    host = input("Introdueix el nom d'amfitrió o la direcció IP del servidor SSH: ")
    print("Selecciona les opcions que desitges utilitzar:")

    while True:
        print_options_menu()

        opcio = input("Introdueix el número de l'opció que desitges: ")

        if opcio == "1":
            execute_ssh_audit(host)
        elif opcio == "2":
            custom_options = input("Introdueix les opcions personalitzades (separades per espais): ")
            execute_ssh_audit(host, custom_options)
        elif opcio == "3":
            show_help()
        elif opcio == "4":
            print("Adeu!")
            break
        else:
            print("Opció no vàlida. Si us plau, introdueix un número vàlid.")

def execute_ssh_audit(host, options=None):
    try:
        command = ["ssh-audit", host]
        if options:
            command.extend(options.split())
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print("ssh-audit no està instal·lat. Si us plau, instal·la-ho abans de continuar.")
    except subprocess.CalledProcessError as e:
        print(f"Error al executar ssh-audit: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def show_help():
    print("Aquesta eina permet escanejar la seguretat d'un servidor SSH.")
    print("Opcions disponibles:")
    print("- Escanejar amb opcions bàsiques: Realitza un escaneo simple sense opcions personalizadas.")
    print("- Escanejar amb opcions personalitzades: Permet especificar opcions personalizadas per ssh-audit.")
    print("- Ajuda: Mostra aquest missatge d'ajuda.")
    print("- Sortir: Finalitza l'aplicació.")

def print_options_menu():
    print("1. Escanejar amb opcions bàsiques")
    print("2. Escanejar amb opcions personalitzades")
    print("3. Ajuda")
    print("4. Sortir")

if __name__ == "__main__":
    main()