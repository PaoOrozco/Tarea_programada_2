"""
Script principal para el procesamiento automático de imágenes.

Este programa recorre un directorio de entrada que contiene imágenes,
les aplica transformaciones (redimensionado, escala de grises y marca de agua),
y guarda los resultados en un directorio de salida.

Además, genera un reporte en formato Excel con información relevante
de cada imagen procesada.

Dependencias:
- Pillow
- xlsxwriter

Autor: Paola Orozco
"""

import os
from PIL import Image
from funciones import aplicar_marca_agua, calcular_resize, convertir_grises, generar_reporte

# Configuración de los directorios de entrada y salida de datos y la ruta de la marca de agua.
directorio_entrada = "imagenes_entrada"
directorio_salida = "imagenes_salida"
marca_ruta = "camara_firma.png"

os.makedirs(directorio_salida, exist_ok=True)

# Lista donde se guardan los datos para el reporte final
reporte_final = [] 

# Ciclo for para procesar cada imagen en el directorio de entrada
for archivo in os.listdir(directorio_entrada):
    if archivo.lower().endswith((".jpg", ".png")):

        ruta_entrada = os.path.join(directorio_entrada, archivo)
        
        try:
            # Abrir imagen
            imagen = Image.open(ruta_entrada)
            ancho_original, alto_original = imagen.size
            formato = imagen.format

            # Redimensionar (lado mayor = 800)
            nuevas_dimensiones = calcular_resize(ancho_original, alto_original, max_lado=800)
            imagen = imagen.resize(nuevas_dimensiones)

            # Escala de grises
            imagen = convertir_grises(imagen)

            # Aplicar la marca de agua
            imagen = aplicar_marca_agua(imagen, Image.open(marca_ruta).convert("RGBA"))

            # Ruta de salida de la imagen procesada
            ruta_salida = os.path.join(directorio_salida, archivo)
            
            # Guardar imagen procesada
            imagen.save(ruta_salida, quality=90)                  
            estado = "Procesada"
            print(f"Procesada: {archivo}")
                       
            # Guardar datos para Excel
            reporte_final.append([
                archivo,
                formato,
                ancho_original,
                alto_original,
                estado
            ])

        except Exception as e:
            print(f"Error en {archivo}: {e}")

# Generar el reporte en Excel
reporte_ruta = os.path.join(directorio_salida, "reporte_imagenes.xlsx") 
generar_reporte(reporte_ruta, reporte_final)

print("Reporte generado:", reporte_ruta)

