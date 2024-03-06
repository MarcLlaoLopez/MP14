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
RUN apt-get install -y nmap

# Instalar las dependencias de Python
RUN pip install python-telegram-bot

FROM python:3.8-alpine

RUN apk upgrade --no-cache
RUN apk add --no-cache rust cargo openssl-dev libffi-dev py3-pip python3 samba-client samba-common-tools yaml-dev
RUN apk add --no-cache --virtual build-dependencies build-base git \
  && git clone --depth 1 https://github.com/cddmp/enum4linux-ng.git \
  && pip install --no-cache-dir -r enum4linux-ng/requirements.txt \
  && apk del build-dependencies


# Copiar los archivos desde el sistema de archivos del host al sistema de archivos del contenedor
COPY / /app/

# Establecer el comando por defecto a ejecutar cuando se inicie el contenedor
CMD [ "python3", "/media/alumne/USB_32GB_Marc/SEGUNDO/MP14/Projecte.py" ]
