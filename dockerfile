FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar las dependencias de tkinter
RUN apt-get update && apt-get install -y python3-tk

# Instalar ssh-audit
RUN apt-get update && apt-get install -y ssh-audit

# Instalar las dependencias de Python
RUN pip install shodan

# Instalar las dependencias de Python
RUN pip install nmap-python

# Instalar las dependencias de Python
RUN pip install nmap-python python-telegram-bot

# Instalar enum4linux
RUN apt-get update && apt-get install -y enum4linux

# Copiar los archivos desde el sistema de archivos del host al sistema de archivos del contenedor
COPY /media/alumne/USB\ 32GB\ Marc/SEGUNDO/MP14 /app/

# Establecer el comando por defecto a ejecutar cuando se inicie el contenedor
CMD [ "python3", "archivo4.py" ]
