# Air Soft - KIWI - Python 

## Índice

* [1. Instrucciones](#1-instrucciones)
  * [1.1. Instalación de Python](#11-instalacion-de-python)
  * [1.2. Creación de entorno virtual](#12-creacion-de-entorno-virtual)
  * [1.3. Instalación de requerimientos](#13-instalacion-de-requerimientos)
* [2. Funcionamiento](#2-funcionamiento)
  * [2.1. Compilación del .apk](#21-compilacion-del-apk)
  * [2.2. Lanzar la apk](#22-lanzar-la-apk)


## 1. Instrucciones

### 1.1. Instalación de Python

Instalación de paquetes necesarios.

```bash
python3 --version  #para ver si tienes python3 instalado.
python3.13-venv --version #para ver si tienes instalado el paquete para entornos virtuales con python.
```

En caso de no contar con lo anterior:

```bash
apt install python3 
apt install pyhton3.13-venv
```

### 1.2. Creación de entorno virtual

Crear un directorio para almacenar los archivos necesarios para el entorno virtual.

```bash
python3 -m venv .venv
```

Activar el entorno virtual.

```bash
source .venv/bin/activate
```

Importante:

- Siempre se debe activar el entorno virtual antes de accerder a la aplicación.

### 1.3. Instalación de requerimientos

```bash
pip install -r requirements.txt
```

## 2. Funcionamiento

Para correr la aplicación.

``` python
python main.py
```

### 2.1. Compilación del .apk

Si actualizas cualquier recurso del directorio necesitas volver a compilar el .apk

Las .apk se guardan en bin/

Para crear una version actualizada localmente:

``` bash
buildozer android debug
```

### 2.2. Lanzar la apk

Para tener una nueva version .apk en produccion.

``` bash
buildozer android release
```

Se necesita configurar una firma para lanzar una apk final.











