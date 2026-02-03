def cargar_planilla(linea,
                    coche,
                    coches,
                    recaudacion: int,
                    recaudaciones: list
                    ) -> None:
    
    match linea:
        case 150:
            indice_linea = 0
        case 155:
            indice_linea = 1
        case 158:
            indice_linea = 2

    for i in range(len(coches)):
        if coche == coches[i]:
            indice_coche = i

    recaudaciones[indice_linea][indice_coche] += recaudacion


def mostrar_recaudacion(recaudaciones: list) -> None:
    print("Planilla de recaudaciones: ")

    for i in range(len(recaudaciones)):
        if i == 0:
            idx = 150
        elif i == 1:
            idx = 155
        elif i == 2:
            idx = 158 
        print(f"Línea {idx}")
        for j in range(len(recaudaciones[i])):
            print(recaudaciones[i][j], end=" ")
        print()


def mostrar_recaudacion_por_linea(recaudaciones: list) -> None:

    numero_lineas = ["Línea 150", "Línea 155", "Línea 158"]

    lineas = [0, 0, 0]

    for i in range(len(recaudaciones[0])):
        lineas[0] += recaudaciones[0][i]

    for i in range(len(recaudaciones[1])):
        lineas[1] += recaudaciones[1][i]
    
    for i in range(len(recaudaciones[0])):
        lineas[2] += recaudaciones[2][i]


    print("Recaudación por líneas: ")
    for i in range(len(lineas)):
        print(numero_lineas[i])
        print(lineas[i], end=" ")


def mostrar_recaudacion_por_coche(coche: str, coches: list, recaudaciones: list) -> None:

    for i in range(len(coches)):
        if coche == coches[i]:
            indice_coche = i
    
    recaudacion_por_coche = 0

    for i in range(len(recaudaciones)):
        recaudacion_por_coche += recaudaciones[i][indice_coche]

    print(f"La recaudación del coche {coche} es ${recaudacion_por_coche}")


def mostrar_recaudacion_total(recaudaciones: list) -> None:

    recaudacion_total = 0

    for i in range(len(recaudaciones)):
        for j in range(len(recaudaciones[i])):
            recaudacion_total += recaudaciones[i][j]
    
    print(f"La recaudación total es: ${recaudacion_total}")


