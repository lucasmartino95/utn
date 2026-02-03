import pygame
from paquete.dibujos import *
from paquete.logica import *

ANCHO = 800
ALTO = 600

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

FILAS = len(dibujo)
COLUMNAS = len(dibujo[0])
TAMAÑO_CELDA = 30

pygame.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Nonograma")

fuente = pygame.font.SysFont("Times New Roman", 30)

boton_jugar = pygame.Rect((280, 140, 250, 50))
boton_ranking = pygame.Rect((280, 240, 250, 50))
boton_salir = pygame.Rect((280, 340, 250, 50))
boton_aceptar = pygame.Rect(280, 280, 250, 50)

botones = [boton_jugar, boton_ranking, boton_salir]

def dibujar_celdas() -> None:

    for i in range(FILAS):
        for j in range(COLUMNAS):
            x = j * TAMAÑO_CELDA
            y = i * TAMAÑO_CELDA
            rectangulo_celda = pygame.Rect(x + 300, y + 150, TAMAÑO_CELDA, TAMAÑO_CELDA)
            pygame.draw.rect(ventana, NEGRO, rectangulo_celda, 1)


matriz_rects = []
for i in range(FILAS):
    fila_rects = []
    for j in range(COLUMNAS):
        x = i * TAMAÑO_CELDA
        y = j * TAMAÑO_CELDA
        rect = pygame.Rect(x, y, TAMAÑO_CELDA, TAMAÑO_CELDA)
        fila_rects.append(rect)
    matriz_rects.append(fila_rects)


def detectar_clic_mouse(posicion_mouse: tuple) -> None:
        for i in range(FILAS):
            for j in range(COLUMNAS):
                    
                if matriz_rects[i][j].collidepoint(posicion_mouse):
                    if comprobar(dibujo, i, j):
                        pygame.draw.rect(ventana, NEGRO, matriz_rects[i][j])
                        pygame.display.update()
                        print("Cuadrado correcto")
                    else:
                        print("Cuadrado incorrecto")

                    print(f"Clic en celda {i},{j}")

def crear_boton(tipo_boton: any,
                texto: str) -> None:
    '''
    Toma un objeto de la clase Rect con su respectiva posición y tamaño,
    luego escribe un texto dentro del rectángulo y lo centra

    Args:
        tipo_boton (any): objeto de la clase Rect
        texto (str): texto dentro del rectángulo
    
    Returns:
        None
    '''

    pygame.draw.rect(ventana, (0, 0, 0), tipo_boton, 5)

    texto_superficie = fuente.render(texto, True, (0, 0, 0))
    text_rect = texto_superficie.get_rect(center=tipo_boton.center)

    ventana.blit(texto_superficie, text_rect)