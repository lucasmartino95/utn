def verificar_ganador_ronda(jugador: int, maquina: int) -> str:

    if jugador == 1 and maquina == 3:
        return "Jugador"
    elif jugador == 2 and maquina == 1:
        return "Jugador"
    elif jugador == 3 and maquina == 2:
        return "Jugador"
    elif jugador == maquina:
        return "Empate"
    else:
        return "Máquina"
    

def verificar_estado_partida(aciertos_jugador: int,
                             aciertos_maquina: int,
                             ronda_actual: int) -> bool:
    
    # Si los dos tienen los mismos puntos, sigue la partida
    # Por ejemplo: 0 - 0, 1 - 1. Pero si sucede que uno de los dos
    # llega a 2 puntos, quiere decir que ganó, porque no pueden llegar los dos
    # a tener 2 puntos al mismo tiempo.
    
    if aciertos_jugador == aciertos_maquina:
        return True
    elif aciertos_jugador == 2 or aciertos_maquina == 2:
        return False


def verificar_ganador_partida(aciertos_jugador: int,
                              aciertos_maquina: int) -> str:
    
    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    else:
        return "Máquina"