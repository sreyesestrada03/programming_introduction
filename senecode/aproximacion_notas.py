def calcular_definitivas(estudiantes: list) -> list:
    for nota_estudiante in estudiantes:
        if nota_estudiante["nota"] >= 4.5:
            nota_estudiante["nota"] = 5.0
        elif nota_estudiante["nota"] >= 3.5:
            nota_estudiante["nota"] = 4.0
        elif nota_estudiante["nota"] >= 2.5:
            nota_estudiante["nota"] = 3.0
        else:
            nota_estudiante["nota"] = 1.5

    return estudiantes

# BLOQUE PRINCIPAL
estudiante_1 = {'nombre': 'Samuel Reyes', 'nota': 4.8}
estudiante_2 = {'nombre': 'Juan Marulanda', 'nota': 3.8}
estudiante_3 = {'nombre': 'Manuela Zapata', 'nota': 3.2}
estudiante_4 = {'nombre': 'Samantha Reyes', 'nota': 2.2}

estudiantes_lista = [estudiante_1,  estudiante_2, estudiante_3, estudiante_4]

calcular_definitivas(estudiantes_lista)

print(estudiantes_lista)
