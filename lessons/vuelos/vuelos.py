def cargar_aerolineas(ruta_archivo: str)->dict:
    aerolineas = {}
    archivo = open(ruta_archivo)
    titulos = archivo.readline().split(",")
    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        codigo_aerolinea = datos[0]
        if codigo_aerolinea not in aerolineas:
            aerolineas[codigo_aerolinea] = []
        vuelo={}
        vuelo["codigo_vuelo"] = datos[1]
        vuelo["origen"] = datos[2]
        vuelo["destino"] = datos[3]
        vuelo["distancia"] = datos[4]
        vuelo["salida"] = datos[5]
        vuelo["duracion"] = datos[6]
        vuelo["retraso"] = datos[7]
        aerolineas[codigo_aerolinea].append(vuelo)
        linea = archivo.readline()
    archivo.close()
    return aerolineas


def aerolinea_con_mas_vuelos(aerolineas: dict) -> dict:
    aerolinea_con_mas_vuelos = None

    for cada_aerolinea in aerolineas.keys():
        if len(aerolineas[cada_aerolinea]) > len(aerolinea_con_mas_vuelos):
            aerolinea_con_mas_vuelos[cada_aerolinea] = len(aerolineas[cada_aerolinea])

    return aerolinea_con_mas_vuelos


def buscar_vuelo(aerolineas: dict, vuelo: str) -> dict:
    aerolinea_codigos_vuelos = {}
    aerolinea_resultado = {}


# Prueba
aerolineas = cargar_aerolineas("vuelos.csv")
print(aerolinea_con_mas_vuelos(aerolineas))
