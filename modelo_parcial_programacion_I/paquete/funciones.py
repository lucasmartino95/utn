def mostrar_menu_opciones() -> int:
    
    print("MENÚ DE OPCIONES")
    print("[1] Cargar evento")
    print("[2] Calcular por cada salón la cantidad total de fiestas realizadas")
    print("[3] Consultar el nombre del evento más realizado en cada salón")
    print("[4] Calcular recaudación de cada salón")
    print("[5] Calcular la cantidad de salones que hayan recaudado más de $5.000.000")
    print("[6] Calcular el porcentaje de bodas de oro realizadas en cada salón")
    print("[7] Generar un informe con la recaudación de cada salón")
    print("[8] Salir del programa")
    opcion_elegida = int(input("Elige lo que quieres hacer: "))

    return opcion_elegida


def cargar_evento(puerto_madero: list,
                  palermo: list,
                  san_telmo: list,
                  salones: list, 
                  evento: str, 
                  salon: str) -> list:

    if evento == "Cumpleaños" or \
    evento == "Casamientos" or \
    evento == "Fiestas de 15" or \
    evento == "Bodas de oro":
        if salon == "Puerto madero":
            salones[0] += 1
        elif salon == "Palermo":
            salones[1] += 1
        elif salon == "San telmo":
            salones[2] += 1
    else:
        print("El evento que ingresaste no es válido")
    
    print(puerto_madero)
    print(palermo)
    print(san_telmo)


def calcular_total_fiestas_por_salon(salones: list) -> None:

    print(f"Puerto madero tiene {salones[0]} fiestas en total")
    print(f"Palermo tiene {salones[1]} fiestas en total")
    print(f"San telmo tiene {salones[2]} fiestas en total")


def consultar_evento_mas_realizado_por_salon(puerto_madero: list,
                                             palermo: list,
                                             san_telmo: list) -> None:
    pass


def mostrar_lista(mi_lista: list) -> None:

    for i in range(len(mi_lista)):
        for j in range(len(mi_lista[i])):
            print(mi_lista[i][j], end=" ")
        print()
