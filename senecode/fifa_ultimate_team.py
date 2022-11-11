def comprar_jugador(jugadores: list, monedas: int) -> str:

    i = 0
    encontrado = False
    jugador_preseleccionado = None

    while i < len(jugadores) and encontrado == False:
        if jugadores[i]["precio"] <= monedas:
            jugador_preseleccionado = jugadores[i]
            encontrado = True
        i += 1

    if jugador_preseleccionado != None:
        for jugador in jugadores:
            if jugador["precio"] <= jugador_preseleccionado["precio"] and jugador["media"] >=jugador_preseleccionado["media"]:
                jugador_preseleccionado = jugador

        jugador_preseleccionado = jugador_preseleccionado["nombre"]

    return jugador_preseleccionado


jugadores = [{'nombre': 'Messi', 'precio': 12000, 'media': 94}, {'nombre': 'Ronaldo', 'precio': 15000, 'media': 93}, {'nombre': 'James', 'precio': 5000, 'media': 86}, {'nombre': 'Salazar', 'precio': 2000, 'media': 78}]

resultado = comprar_jugador(jugadores, 19000)
print(resultado)
