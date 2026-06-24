

import xlsxwriter


# Función que calcula las nuevas dimensiones.
def calcular_resize(ancho_original, alto_original, max_lado=800):
    
    # No agrandar imágenes pequeñas
    if max(ancho_original, alto_original) <= max_lado:
        return (ancho_original, alto_original)

    # Calcula nuevas dimensiones manteniendo la relación de aspecto con base en el lado mayor
    if ancho_original >= alto_original:
        ancho_deseado = max_lado
        relacion = alto_original / ancho_original
        alto_deseado = int(ancho_deseado * relacion)
    else:
        alto_deseado = max_lado
        relacion = ancho_original / alto_original
        ancho_deseado = int(alto_deseado * relacion)

    return (ancho_deseado, alto_deseado)



# Función que convierte la imagen a escala de grises.
def convertir_grises(imagen):
    return imagen.convert("L").convert("RGB")



# Función que aplica la marca de agua.
def aplicar_marca_agua(imagen, marca_agua, margen=10):
    
    # Escalar marca de agua proporcionalmente
    ratio_marca_agua = 0.1  # 10% del ancho de la imagen
    nuevo_ancho_firma = int(imagen.size[0] * ratio_marca_agua)
    aspecto_firma = marca_agua.size[1] / marca_agua.size[0]

    marca_agua = marca_agua.resize(
        (nuevo_ancho_firma, int(nuevo_ancho_firma * aspecto_firma))
    )

    # Posición (esquina inferior derecha)
    x = imagen.size[0] - marca_agua.size[0] - margen
    y = imagen.size[1] - marca_agua.size[1] - margen

    # Pegar marca de agua
    imagen.paste(marca_agua, (x, y), marca_agua)

    return imagen


# Función para generar reporte en XlsxWriter
def generar_reporte(reporte_ruta, reporte_final):
    workbook = xlsxwriter.Workbook(reporte_ruta)
    worksheet = workbook.add_worksheet("datos")

    # Encabezados
    headers = ["Nombre archivo", "Formato", "Ancho", "Alto", "Estado"]

    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Escribir datos
    for fila, dato in enumerate(reporte_final, start=1):
        for col, valor in enumerate(dato):
            worksheet.write(fila, col, valor)

    workbook.close()



