FROM python:3.10-slim

# Instalar dependencias del sistema necesarias para Kivy
RUN apt-get update && apt-get install -y \
    #soporte multi touch
    libmtdev1 \
    libmtdev-dev\
    #soporte portapapeles
    xclip xsel\
    #soporte grafico
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libgl1-mesa-dev \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Actualizar pip y herramientas
RUN pip install --upgrade pip setuptools wheel

# Copiar primero requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Ejecutar la aplicación dentro de xvfb
CMD ["python", "main.py"]
