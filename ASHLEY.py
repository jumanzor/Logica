print ("HOLA MUNDO")
print ("HOLA MUNDO")
print ("HOLA MUNDO")


'''
#  programar un juego de TETRIS

1. pintar el GRID (la cuadrícula)  area de juego
2. pintemos un cuadro
3. hagamos que ese cuadro caiga solo
4. mover el cuadro (derecha/izquierda)
5. detectar colision (con otreas piezas y el fondo)
6. eliminar linea completada
7. rotar piezas
8. tener varios tipos de piezas
'''






# ya pinta los diferentes bloques
# falta mejorarlo

import pygame
import sys, time
import random
import numpy as np


############################################################
#  inicialización del juego
############################################################
global vPosicionX, vPosicionY, nuevo_x, nuevo_y
global bloqueActual

# Manejo de variables
pygame.init()

vColor = (255, 255, 255)


# Configuración de la ventana
vVentanaAncho = 401
vVentanaAlto = 801


# Configuración de la cuadrícula a dibujar
vCantidadFilas = 20
vCantidadColumnas = 10
vBloqueTamano = vVentanaAncho // vCantidadColumnas



############################################################
#  funciones
############################################################

def dibujaCuadricula():
    for fila in range(20):

        for col in range(10):
          x = col * vBloqueTamano
          y = fila * vBloqueTamano
          pygame.draw.rect(vVentana, vColor, (x, y, vBloqueTamano, vBloqueTamano), 1)



class Figura:
    x = 0
    y = 0

    figuras = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]




#cuadro de prueba 
#Color y velocidad de movimiento
VELOCIDAD_X = 5
cColor = (255, 255, 255)
cTamano= vVentanaAncho // vCantidadColumnas
def dibujaCuadro():
    pygame.draw.rect(cCuadro, cColor, (40,0, cTamano, cTamano), 100)

############################################################
#  inicia el juego
############################################################
    
##MATRIZ 
matriz = [[0] * 20 for _ in range(10)]

# Imprimir la matriz
for fila in matriz:
    print(fila)

# inicia el game loop
cCuadro = pygame.display.set_mode((vVentanaAncho, vVentanaAlto))
vVentana = pygame.display.set_mode((vVentanaAncho, vVentanaAlto))
pygame.display.set_caption("Juego del Tetris")
ejecutando = True

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ejecutando = False

    vVentana.fill((0, 0, 0))

    dibujaCuadricula()
    dibujaCuadro()

    pygame.display.update()


pygame.quit()
sys.exit()

