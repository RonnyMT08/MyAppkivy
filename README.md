k# Air Soft - Kivy App

Aplicación móvil construida con **Kivy** para gestión de reservas de Air Soft.

## Índice

1. [Características](#características)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Instalación](#instalación)
   1. [Crear entorno virtual](#1-crear-entorno-virtual)
   2. [Instalar dependencias](#2-instalar-dependencias)
4. [Uso](#uso)
   1. [Ejecutar en desarrollo](#ejecutar-en-desarrollo)
   2. [Compilar APK](#compilar-apk)
5. [Permisos en Linux](#permisos-en-linux)
6. [Recursos](#recursos)

## Características

- Autenticación de usuarios
- Navegación entre pantallas con ScreenManager
- Interfaz personalizada con Kivy Language (.kv)
- Estructura modular de vistas
- Carga automática de archivos .kv

## Estructura del Proyecto

```
MyAppkivy/
├── main.py                  # Punto de entrada de la aplicación
├── views/                   # Vistas (pantallas) de la aplicación
│   ├── login.py / login.kv
│   ├── home.py / home.kv
│   ├── navbase.py / navbase.kv
│   ├── homebase.py / homebase.kv
│   ├── contacto.py / contacto.kv
│   ├── reservas.py / reservas.kv
│   ├── cuenta.py / cuenta.kv
│   ├── mapas.py / mapas.kv
│   ├── kits.py / kits.kv
│   ├── modos.py / modos.kv
│   ├── publica.py / publica.kv
│   └── privada.py / privada.kv
├── widgets/                 # Widgets personalizados
│   ├── custom_buttons.py
│   └── custom_buttons.kv
├── assets/                  # Recursos (imágenes, fuentes, iconos)
├── buildozer.spec           # Configuración para compilar APK
└── requirements.txt         # Dependencias Python
```

## Instalación

### 1. Crear entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar en desarrollo

```bash
python main.py
```

### Compilar APK

#### Dependencias del sistema (Linux)

Instalar antes de compilar:

```bash
sudo apt-get install -y \
    python3-dev \
    zlib1g-dev \
    default-jdk \
    autoconf \
    libtool \
    pkg-config \
    libncurses-dev \
    cmake \
    libffi-dev \
    libssl-dev \
    cython3
```

> **Nota:** `libncurses-dev` incluye tanto `libncurses5-dev` como `libncursesw5-dev`. Si `default-jdk` no está disponible, usá `apt search openjdk | grep jdk` para ver las versiones instalables.

#### Instalación de Buildozer

```bash
pip install buildozer
```

> **Nota:** Cython es obligatorio para compilar Kivy a código nativo de Android. Buildozer lo busca en el Python del sistema, no en tu `.venv`.

#### Inicializar (solo la primera vez)

```bash
buildozer init
```

Esto genera el archivo `buildozer.spec` con la configuración de tu app.

#### Comandos básicos

| Comando | Descripción |
|---------|-------------|
| `buildozer android debug` | Compila APK de desarrollo en `bin/` |
| `buildozer android release` | Compila APK de producción en `bin/` |
| `buildozer android debug deploy run` | Instala y ejecuta en dispositivo conectado |
| `buildozer android debug logcat` | Muestra logs del dispositivo en tiempo real |
| `buildozer -v android debug` | Modo verbose (más detalle de errores) |

#### Flujo de trabajo habitual

```bash
# 1. Desarrollar y probar en PC
python main.py

# 2. Compilar APK
buildozer android debug

# 3. Probar en Android (conectar dispositivo por USB)
buildozer android debug deploy run

# 4. Ver logs si algo falla
buildozer android debug logcat
```

> **Nota:** Buildozer solo funciona en Linux. En Windows usá WSL.

## Permisos en Linux

Para que el teclado y mouse funcionen correctamente durante el desarrollo:

```bash
sudo usermod -aG input $USER
newgrp input
```

Reinicia la sesión después de aplicar los cambios.

## Recursos

- [Iconos - Flaticon](https://www.flaticon.es)
- [Documentación Kivy](https://kivy.org/doc/stable/)
