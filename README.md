# Air Soft - Kivy App

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
7. [Pendientes de Desarrollo](#7-pendientes-de-desarrollo)

## 1. Características

- Autenticación de usuarios
- Navegación entre pantallas con ScreenManager
- Interfaz personalizada con Kivy Language (.kv)
- Estructura modular de vistas
- Carga automática de archivos .kv

## 2. Estructura del Proyecto

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

## 3. Instalación

### 3.1. Crear entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3.2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Uso

### 4.1. Ejecutar en desarrollo

```bash
python main.py
```

### 4.2. Compilar APK

```bash
# Debug
buildozer android debug

# Release
buildozer android release
```

## 5. Permisos en Linux

Para que el teclado y mouse funcionen correctamente durante el desarrollo:

```bash
sudo usermod -aG input $USER
newgrp input
```

Reinicia la sesión después de aplicar los cambios.

## 6. Recursos

- [Iconos - Flaticon](https://www.flaticon.es)
- [Documentación Kivy](https://kivy.org/doc/stable/)

## 7. Pendientes de Desarrollo

### 7.1. Autenticación
- [ ] Validar credenciales contra una API o base de datos (actualmente hardcodeado)
- [ ] Hashear contraseñas (bcrypt, argon2)
- [ ] Token de sesión (JWT) y persistencia de sesión
- [ ] Registro de usuarios
- [ ] Recuperación de contraseña

### 7.2. Vistas sin implementar
- [ ] **Mapas**: mostrar mapa real (Google Maps, Mapbox, uOSM)
- [ ] **Kits**: listado de kits con imágenes, precios y detalles
- [ ] **Modos**: descripción de modos de juego
- [ ] **Publica**: pantalla de juegos públicos
- [ ] **Privada**: pantalla de juegos privados
- [ ] **Reservas**: formulario de reserva con fecha, hora y cupo
- [ ] **Cuenta**: perfil de usuario, edición de datos, historial
- [ ] **Contacto**: formulario funcional con backend

### 7.3. Funcionalidad transversal
- [ ] Conectividad con backend (REST API o Firebase)
- [ ] Manejo de estado global (patrón Store o Redux-like)
- [ ] Notificaciones push
- [ ] Almacenamiento local (SQLite, SharedPreferences)
- [ ] Manejo de errores de red y estados de carga (spinners)
- [ ] Validación de formularios (email, teléfono, contraseñas)
- [ ] Internacionalización (i18n)

### 7.4. UX/UI
- [ ] Indicadores de carga (Spinner, Skeleton)
- [ ] Confirmación de acciones destructivas (diálogos)
- [ ] Notificaciones toast / snackbar
- [ ] Modo oscuro
- [ ] Responsive para tablets
- [ ] Animaciones de transición entre pantallas

### 7.5. Calidad
- [ ] Tests unitarios (pytest)
- [ ] Tests de integración (Kivy testing)
- [ ] CI/CD (GitHub Actions)
- [ ] Documentación de API
- [ ] Manejo de logs estructurado
