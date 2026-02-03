from paquete.dibujos import *
from paquete.logica import *
from paquete.ranking import *
from paquete.complementarias import *
from paquete.graficos.config import *

import time
import pygame

jugando = True

pygame.init()
mostrar_boton = True

ventana.fill("lightblue")

crear_boton(botones[0], "Jugar")
crear_boton(botones[1], "Ver ranking")
crear_boton(botones[2], "Salir")

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = evento.pos
            for i in range(len(botones)):
                if botones[i].collidepoint(posicion_mouse) and mostrar_boton:
                    ventana.fill("lightblue")
                    mostrar_boton = False
                    match i:
                        case 0:
                            crear_boton(boton_aceptar, "Aceptar")
                            crear_boton(pygame.Rect((280, 140, 250, 0)), "Escribe tu nombre")
                            crear_boton(pygame.Rect((280, 180, 250, 50)), "")
                            pygame.display.update()
                        case 1:
                            print("Ver ranking")
                        case 2:
                            ejecutando = False
    if not mostrar_boton:
        if boton_aceptar.collidepoint(posicion_mouse):
            ventana.fill("lightblue")
            dibujar_celdas()
            pistas_filas = mostrar_pistas_por_fila()
            pistas_columnas = mostrar_pistas_por_columna()
            ventana.blit(pistas_filas, (270, 350))
            ventana.blit(pistas_columnas, (270, 300))
            pygame.display.update()

    pygame.display.update()

    pygame.quit
