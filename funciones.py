import xlsxwriter

# Función que calcula las nuevas dimensiones.
def calcular_resize(ancho_original, alto_original, max_lado=800):
    """
    Calcula nuevas dimensiones para una imagen manteniendo la relación de aspecto.

    Si la imagen es más pequeña que el tamaño máximo permitido, no la agranda.

    Parámetros:
    ancho_original (int): Ancho original de la imagen en píxeles.
    alto_original (int): Alto original de la imagen en píxeles.
    max_lado (int, opcional): Tamaño máximo permitido para el lado mayor. Default es 800.

    Retorna:
    tuple: (nuevo_ancho, nuevo_alto) ajustados proporcionalmente.
    """
    
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
    """
    Convierte una imagen a escala de grises.

    Parámetros:
    imagen (PIL.Image): Imagen en formato PIL.

    Retorna:
    PIL.Image: Imagen convertida a escala de grises (modo RGB).
    """
    return imagen.convert("L").convert("RGB")


# Función que aplica la marca de agua.
def aplicar_marca_agua(imagen, marca_agua, margen=10):
    """
    Aplica una marca de agua a una imagen en la esquina inferior derecha.

    La marca de agua se escala proporcionalmente al tamaño de la imagen base.

    Parámetros:
    imagen (PIL.Image): Imagen principal donde se aplicará la marca de agua.
    marca_agua (PIL.Image): Imagen de la marca de agua.
    margen (int, opcional): Espacio en píxeles desde los bordes. Default es 10.

    Retorna:
    PIL.Image: Imagen con la marca de agua aplicada.
    """
    
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
    """
    Genera un archivo Excel con el reporte de imágenes procesadas.

    El reporte incluye información como nombre del archivo, formato,
    dimensiones y estado del procesamiento.

    Parámetros:
    reporte_ruta (str): Ruta donde se guardará el archivo de Excel.
    reporte_final (list): Lista de listas con los datos del reporte.

    Retorna:
    None
    """
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


