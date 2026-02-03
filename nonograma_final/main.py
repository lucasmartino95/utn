from paquete.dibujos import *
from paquete.logica import *
from paquete.ranking import *
from paquete.complementarias import *
import time

jugando = True

while jugando:

    print("[1] Jugar")
    print("[2] Ver ranking")
    print("[3] Salir")

    opcion = int(input("Elige una opción: "))

    match opcion:
        case 1:
            juego_activo = True
            nombre_jugador = input("Ingresa tu nombre: ")
            inicio = time.time()
            while juego_activo:
                mostrar_dibujo(dibujo_jugador)
                mostrar_pistas_por_fila()
                mostrar_pistas_por_columna()

                fila = int(input("Ingresa una fila: "))
                fila = validar_ingreso(fila, "Ingresa una fila: ")

                columna = int(input("Ingresa una columna: "))
                columna = validar_ingreso(columna, "Ingresa una columna: ")

                posicion_ingresada = comprobar(dibujo, fila, columna)

                if posicion_ingresada:
                    if dibujo_jugador[fila][columna] == 1:
                        print("Esta posición ya está pintada")
                    dibujo_jugador[fila][columna] = 1
                    if gano(dibujo, dibujo_jugador, "Felicidades! Ganaste.\n" \
                    "Se cargará al ranking tu puntaje"):
                        fin = time.time()
                        tiempo_final = fin - inicio
                        tiempo_final = round(tiempo_final, 2)
                        cargar_ranking(nombre_jugador, tiempo_final)
                        limpiar_dibujo(dibujo_jugador)
                        juego_activo = False
                else:
                    if total_vidas == 1:
                        print("Te quedaste sin vidas!")
                        limpiar_dibujo(dibujo_jugador)
                        juego_activo = False
                    else:
                        total_vidas = restar_vida(total_vidas)
                        print(f"Te quedan {total_vidas} vidas")
        case 2:
            leer_ranking()
        case 3:
            jugando = False