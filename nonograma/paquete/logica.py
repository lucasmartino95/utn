total_vidas = 3

def comprobar(dibujo: list,
              fila: int,
              columna: int) -> bool:

    if dibujo[fila][columna] == 1:
        return True
    else:
        return False
    

def restar_vida(total_vidas: int) -> None:

    total_vidas -= 1

    return total_vidas


def recorrer_matriz(matriz: list) -> None:

    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                contador += 1

    return contador            


def gano(dibujo: list,
         dibujo_jugador: list,
         mensaje: str) -> bool:
    
    contador = 0
    contador_jugador = 0
    

    contador = recorrer_matriz(dibujo)

    contador_jugador = recorrer_matriz(dibujo_jugador)
                
    if contador == contador_jugador:
        print(mensaje)
        return True
    else:
        return False


def limpiar_dibujo(dibujo_jugador: list) -> None:

    for i in range(len(dibujo_jugador)):
        for j in range(len(dibujo_jugador[i])):
            dibujo_jugador[i][j] = 0