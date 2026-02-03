import mostrar
import verificaciones
import random

def jugar_piedra_papel_o_tijera() -> str:

    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 0

    bandera = True

    while bandera:
        print("-------")
        print("Elige entre estas opciones")

        eleccion_jugador = int(input("[1] Piedra - "
        "[2] Papel - [3] Tijera: "))

        while eleccion_jugador != 1 and eleccion_jugador != 2 and eleccion_jugador != 3:
            eleccion_jugador = int(input("[1] Piedra - "
        "[2] Papel - [3] Tijera: "))

        eleccion_maquina = random.randint(1, 3)

        elemento_elegido_jugador = mostrar.mostrar_elemento(eleccion_jugador)
        elemento_elegido_maquina = mostrar.mostrar_elemento(eleccion_maquina)

        print(f"Tu jugada: {elemento_elegido_jugador}")
        print(f"Máquina: {elemento_elegido_maquina}")

        ganador_ronda = verificaciones.verificar_ganador_ronda(eleccion_jugador,
                                                               eleccion_maquina)

        if ganador_ronda == "Empate":
            print("Hubo empate")
        else:
            if ganador_ronda == "Jugador":
                aciertos_jugador += 1
            else:
                aciertos_maquina += 1
                
            print(f"El ganador de la ronda es: {ganador_ronda}")

        ronda_actual += 1

        partida = verificaciones.verificar_estado_partida(aciertos_jugador,
                                                aciertos_maquina,
                                                ronda_actual)
        
        print(f"El resultado de la partida es: Jugador {aciertos_jugador} - Máquina: {aciertos_maquina} / Ronda actual: {ronda_actual}")

        if partida == False:
            ganador_partida = verificaciones.verificar_ganador_partida(aciertos_jugador,
                                                     aciertos_maquina)
            bandera = False
            print(f"El ganador es: {ganador_partida}")
            return ganador_partida


jugar_piedra_papel_o_tijera()