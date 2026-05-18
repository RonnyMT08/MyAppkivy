FROM python:3.10-slim

# Instalar dependencias del sistema necesarias para Kivy
RUN apt-get update && apt-get install -y \
    libgl1 \
    libgles2 \
    libglu1-mesa \
    xvfb \
    libmtdev1 \
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
CMD ["xvfb-run", "python", "main.py"]
