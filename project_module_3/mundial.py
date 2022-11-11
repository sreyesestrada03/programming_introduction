def carga_de_datos(nombre_archivo: str) -> dict:
    clubes = {}
    archivo = open(nombre_archivo, encoding='utf-8')
    titulos = archivo.readline().split(",")

    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        club = datos[0]
        jugador = {
            "name": datos[1],
            "wage": datos[2],
            "age": datos[3],
            "pace": datos[4],
            "shooting": datos[5],
            "passing": datos[6],
            "dribbling": datos[7],
            "position": datos[8],
            "joined": datos[9],
            "contract": datos[10],
            "nationality": datos[11],
            "preferred_foot": datos[12],
            "international_reputation": int(datos[13].replace("\n", ""))
        }

        if club in clubes:
            clubes[club] += [jugador]
        else:
            clubes[club] = [jugador]
        linea = archivo.readline()

    archivo.close()
    return clubes


def equipos_con_cadena_nombre(clubes: dict, cadena: str) -> dict:
    clubes_filtrados = {}

    for club in clubes.keys():
        if cadena.lower() in club.lower():
            clubes_filtrados[club] = clubes[club]

    return clubes_filtrados


def calcular_promedio_salario(clubes: dict, nombre_club: str) -> int:
    promedio = 0
    i = 0

    club_a_promediar = equipos_con_cadena_nombre(clubes, nombre_club)

    if nombre_club in clubes:
        while i < len(club_a_promediar[nombre_club]):
            promedio += int(club_a_promediar[nombre_club][i]["wage"])
            i += 1

        promedio /= len(club_a_promediar[nombre_club])

    return round(promedio, 2)


def buscar_jugador(clubes: dict, nombre_jugador: str) -> dict:
    diccionario_jugador = None
    contador = 0

    for club in clubes.keys():
        for jugador in clubes[club]:
            if nombre_jugador.lower() == jugador["name"].lower():
                diccionario_jugador = clubes[club][contador]

            contador += 1

        contador = 0

    return diccionario_jugador


def calcular_puntaje_jugador(jugador: dict) -> int:
    delanteros = ["LF", "CF", "RF", "ST", "RS", "LS"]
    pace = 0
    shooting = 0
    passing = 0
    dribbling = 0
    bono = 0

    if jugador["position"] == "SUB" or jugador["position"] == "RES":
        puntaje = 0

    elif jugador["position"] in delanteros:
        pace = int(jugador["pace"]) * 0.10
        shooting = int(jugador["shooting"]) * 0.45
        passing = int(jugador["passing"]) * 0.05
        dribbling = int(jugador["dribbling"]) * 0.40

        if "L" in jugador["position"] and jugador["preferred_foot"] == "Left" or "R" in jugador["position"] and jugador["preferred_foot"] == "Right":
            bono = 0.05

    else:
        pace = int(jugador["pace"]) * 0.30
        shooting = int(jugador["shooting"]) * 0.10
        passing = int(jugador["passing"]) * 0.40
        dribbling = int(jugador["dribbling"]) * 0.20

        if "L" in jugador["position"] and jugador["preferred_foot"] == "Left" or "R" in jugador["position"] and jugador["preferred_foot"] == "Right":
            bono = 0.05

    puntaje = pace + shooting + passing + dribbling + bono

    return puntaje


def mejores_y_peores_jugadores(clubes: dict) -> dict:
    diccionario_mejor_peor = {}

    for club in clubes.keys():
        mejor_jugador = clubes[club][0]
        peor_jugador = clubes[club][0]

        for jugador in clubes[club]:
            if calcular_puntaje_jugador(mejor_jugador) < calcular_puntaje_jugador(jugador):
                mejor_jugador = jugador

            if calcular_puntaje_jugador(peor_jugador) > calcular_puntaje_jugador(jugador):
                peor_jugador = jugador

        diccionario_mejor_peor[club] = {"mejor": None, "peor": None}
        diccionario_mejor_peor[club]["mejor"] = mejor_jugador["name"]
        diccionario_mejor_peor[club]["peor"] = peor_jugador["name"]


    return diccionario_mejor_peor


def cantidad_jugadores_posicion(clubes: dict, posicion: str) -> int:
    resultado = 0

    for club in clubes:
        for jugador in clubes[club]:
            if jugador["position"] == posicion.upper():
                resultado += 1

    return resultado


def jugadores_por_pais(clubes: dict) -> dict:
    diccionario_paises = {}

    for club in clubes:
        for jugador in clubes[club]:
            if jugador["nationality"] in diccionario_paises:
                diccionario_paises[jugador["nationality"]] += [jugador]
            else:
                diccionario_paises[jugador["nationality"]] = [jugador]

    return diccionario_paises


def top10_paises_reputacion_internacional(clubes: dict) -> dict:
    diccionario_paises = jugadores_por_pais(clubes)
    diccionario_paises_promedio = {}
    pais_mejor_promedio_nombre = ""
    pais_mejor_promedio = -1
    top10 = []

    for pais in diccionario_paises.keys():
        diccionario_paises_promedio[pais] = 0

        for jugador in diccionario_paises[pais]:
            diccionario_paises_promedio[pais] = jugador["international_reputation"] + diccionario_paises_promedio[pais]

        diccionario_paises_promedio[pais] = diccionario_paises_promedio[pais] / len(diccionario_paises[pais])

    for i in range(0, 10):
        for cada_pais_promedio in diccionario_paises_promedio:
            if diccionario_paises_promedio[cada_pais_promedio] > pais_mejor_promedio:
                pais_mejor_promedio = diccionario_paises_promedio[cada_pais_promedio]
                pais_mejor_promedio_nombre = cada_pais_promedio

        top10 += [pais_mejor_promedio_nombre]
        del diccionario_paises_promedio[pais_mejor_promedio_nombre]
        pais_mejor_promedio = 0
        pais_mejor_promedio_nombre = ""

    return top10[::-1]
