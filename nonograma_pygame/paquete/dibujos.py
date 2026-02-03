import random
import pygame

pygame.init()
fuente = pygame.font.SysFont("Times New Roman", 30)

dibujo_uno = [
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1]
]

dibujo_dos = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1]
]

dibujo_tres = [
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]

dibujo_cuatro = [
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

dibujo_jugador = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

#dibujos = [dibujo_uno, dibujo_dos, dibujo_tres]
dibujos = [dibujo_cuatro]

dibujo = random.choice(dibujos)


def mostrar_dibujo(dibujo: list) -> None:
    for i in range(len(dibujo)):
        for j in range(len(dibujo[i])):
            print(dibujo[i][j], end=" ")
        print()


def calcular_pistas(linea: list) -> None:
    
    pistas = []
    contador = 0

    for celda in linea:
        if celda == 1:
            contador += 1
        else:
            if contador > 0:
                pistas.append(contador)
            contador = 0
        
    if contador > 0:
        pistas.append(contador)
            
    return pistas


def mostrar_pistas_por_fila() -> None:

    pistas_fila = []

    for i in range(len(dibujo)):
        pistas_fila.append(calcular_pistas(dibujo[i]))

    texto_superficie = fuente.render(f"Pistas por fila: {pistas_fila}", True, (0, 0, 0))

    return texto_superficie
    


def mostrar_pistas_por_columna() -> None:

    pistas_columnas = []

    for i in range(len(dibujo)):

        columna = []

        for j in range(len(dibujo[0])):
            columna.append(dibujo[j][i])

        pistas_columnas.append(calcular_pistas(columna))

    texto_superficie = fuente.render(f"Pistas por columnas: {pistas_columnas}", True, (0, 0, 0))

    return texto_superficie

