import subprocess

def descobrir_hosts(ip):
    try:
        resultado = subprocess.check_output(["nmap", "-sn", ip])
        return resultado.decode("utf-8")
    except Exception as e:
        return str(e)

def escanejar_ports(ip, puertos):
    try:
        resultado = subprocess.check_output(["nmap", "-p", puertos, ip])
        return resultado.decode("utf-8")
    except Exception as e:
        return str(e)

def llistar_serveis_versions(ip, puertos):
    try:
        resultado = subprocess.check_output(["nmap", "-p", puertos, "-A", ip])
        return resultado.decode("utf-8")
    except Exception as e:
        return str(e)

def llistar_vulnerabilitats(ip, puertos):
    try:
        opciones = ["-p", puertos, "--script", "vuln", ip]
        resultado = subprocess.check_output(["nmap"] + opciones)
        return resultado.decode("utf-8")
    except Exception as e:
        return str(e)

def main():
    try:
        num = int(input("Què vols fer? (1: Descobrir hosts, 2: Escanejar ports, 3: Llistar serveis i versions, 4: Llistar vulnerabilitats): "))
        
        if num == 1:
            ip = input("Introdueix la direcció IP o xarxa a escanejar: ")
            print(descobrir_hosts(ip))
        elif num == 2:
            ip = input("Introdueix la direcció IP a escanejar: ")
            puertos = input("Introdueix els ports a escanejar (exemple: 80-100): ")
            print(escanejar_ports(ip, puertos))
        elif num == 3:
            ip = input("Introdueix la direcció IP a escanejar: ")
            puertos = input("Introdueix els ports a escanejar (exemple: 80-100): ")
            print(llistar_serveis_versions(ip, puertos))
        elif num == 4:
            ip = input("Introdueix la direcció IP a escanejar: ")
            puertos = input("Introdueix els ports a escanejar (exemple: 80-100): ")
            print(llistar_vulnerabilitats(ip, puertos))
        else:
            print("Opció no vàlida.")
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")

if __name__ == "__main__":
    main()