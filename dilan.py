#dilan c27059
print('Hola mundo')
print('Hola mundo')
print('Hola mundo')
print('Hola mundo')
print('Hola mundo')
print('Hola mundo')


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


############################################################
#  inicialización del juego
############################################################
global vPosicionX, vPosicionY, nuevo_x, nuevo_y
global bloqueActual

# Manejo de variables
pygame.init()

vColor = (255, 255, 255)


# Configuración de la ventana
vVentanaAncho = 400
vVentanaAlto = 700


# Configuración de la cuadrícula a dibujar
vCantidadFilas = 20
vCantidadColumnas = 10
vBloqueTamano = vVentanaAncho // vCantidadColumnas


############################################################
#  funciones
############################################################


def dibujaCuadricula():
            for x in range(0, vVentanaAncho, vBloqueTamano):
             for y in range(0, vVentanaAlto, vBloqueTamano):
                pygame.draw.rect(vVentana, vColor, (x, y, vBloqueTamano, vBloqueTamano), 1)
           
def dibujarCuadro():
    x=0
    y=0
    velocidad_x = 5
    if x <= 0 or x + vBloqueTamano >= vVentanaAlto:
        x= x-2
    pygame.draw.rect(vVentana,(0, 0, 255),(x, y, vBloqueTamano, vBloqueTamano), 0) 

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)  # 60 FPS

############################################################
#  inicia el juego
############################################################



# inicia el game loop
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
    dibujarCuadro()

    pygame.display.update()


pygame.quit()
sys.exit()


