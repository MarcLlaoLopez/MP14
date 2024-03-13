FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar ssh-audit
RUN apt-get update && apt-get install -y ssh-audit

# Instalar las dependencias de Python
RUN pip install shodan

# Instalar las dependencias de Python
RUN apt-get install -y nmap

# Instalar las dependencias de Python
RUN pip install python-telegram-bot

FROM python:3.8-alpine

# Instalar las dependencias necesarias para Tkinter en Alpine Linux
RUN apk add --no-cache tcl-dev tk-dev

# Copiar los archivos desde el sistema de archivos del host al sistema de archivos del contenedor
COPY --from=0 /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.8/site-packages/

# Copiar los archivos desde el sistema de archivos del host al sistema de archivos del contenedor
COPY / /app/

# Establecer el comando por defecto a ejecutar cuando se inicie el contenedor
CMD [ "python3", "/media/alumne/USB_32GB_Marc/SEGUNDO/MP14/Projecte.py" ]
