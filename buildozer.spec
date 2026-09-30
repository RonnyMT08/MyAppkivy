[app]
# Nombre de la aplicación
title = Air-Soft

# Nombre del paquete (único)
package.name = miappkivy
package.domain = org.example

# Archivo principal
source.dir = .
source.include_exts = py,kv,png,jpg,ttf

# Icono de la app
icon.filename = %(source.dir)s/assets/images/icon.png

# Orientación de la pantalla
orientation = portrait

# Permisos de Android
android.permissions = INTERNET

# Versión de la app
version = 0.1

# Dependencias necesarias
requirements = python3==3.11,kivy,requests

# Ocultar consola (solo relevante en Windows)
console = False

# Archivos que no quieres incluir
exclude_patterns = tests, *.md, .venv

[buildozer]
# Plataforma destino
target = android

# Opciones de Android
android.api = 34
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.arch = arm64-v8a

# Directorio de compilación
build_dir = .buildozer

# Modo de depuración
log_level = 2