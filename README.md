# Tarea_programada_2
Herramienta para procesamiento de imágenes

# Generador de Catálogos e Informes de Imágenes

## Descripción
Este proyecto consiste en un programa en Python que automatiza el procesamiento de imágenes y genera un reporte tipo catálogo.
El sistema toma un conjunto de imágenes y realiza automáticamente varias transformaciones, además de generar un informe con información relevante de cada archivo.

---

## Funcionalidades principales

- Procesamiento por lotes de imágenes (.jpg y .png)
- Redimensionamiento de imágenes (máximo 800x800 píxeles)
- Conversión a escala de grises
- Inserción de marca de agua
- Generación de reporte en:
  - Excel (XlsxWriter)
---

## Estructura del proyecto

/proyecto
│── imagenes_entrada/     # Carpeta con imágenes originales
│── imagenes_salida/      # Carpeta con imágenes procesadas
│── camara_firma.png/     # Marca de agua
│── funciones.py          # Funciones para procesamiento de imágenes
│── main.py               # Script principal
│── requirements.txt      # Dependencias del proyecto
│── README.md             # Documentación básica

---

## Cómo ejecutar el proyecto

### 1. Crear entorno virtual
python -m venv venv

### 2. Activar entorno virtual
venv\Scripts\activate

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Ejecutar el programa
python main.py

---

## Salida del programa

Imágenes procesadas en la carpeta output/
Archivo de reporte:
reporte_imagenes.xlsx o
catalogo_imagenes.pdf

---


## Requisitos

Python 3.x
Biblioteca Pillow
XlsxWriter

---


## Contexto del proyecto
Este proyecto fue desarrollado como parte de la Tarea Programada #2, con el objetivo de automatizar el procesamiento de imágenes y la generación de reportes detallados. [Tarea programada #2 | PDF]

---

## Autor
Paola Orozco

