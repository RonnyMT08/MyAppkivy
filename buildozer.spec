[app]
# Nombre de la aplicación
title = MiAppKivy
# Nombre del paquete (único)
package.name = miappkivy
package.domain = org.example

# Archivo principal
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,env

# Icono de la app
icon.filename = %(source.dir)s/assets/icon.png

# Orientación de la pantalla
orientation = portrait

# Permisos de Android
android.permissions = INTERNET, CAMERA

# Versión de la app
version = 0.1

# Dependencias necesarias
requirements = python3,kivy,python-dotenv

# Ocultar consola (solo relevante en Windows)
console = False

# Archivos que no quieres incluir
exclude_patterns = tests, *.md, .venv

[buildozer]
# Plataforma destino
target = android

# Directorio de compilación
build_dir = .buildozer

# Modo de depuración
log_level = 2