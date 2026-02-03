def cargar_ranking(nombre: str,
                   tiempo_final: float) -> None:

    with open("ranking.csv", "a") as archivo:
        archivo.write(f"{nombre}, {tiempo_final}s\n")


def leer_ranking() -> None:

    ranking = []
    with open("ranking.csv", "r") as archivo:
        ranking.append(archivo.readlines())

    lista = []
    for i in range(len(ranking)):
        for j in range(len(ranking[i])):
            lista.append(ranking[i][j].strip())

    print("Los mejores jugadores")
    for i in range(len(lista)):
        print(lista[i], end="\n")