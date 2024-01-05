#Cristofer C26901

print('hola mundo...')

#problema: Juego de tetris
    #Pintar el fondo            listo
    #crear una pieza
    #que la pieza caiga
    #mover la pieza (der/izq)
    #detectar colisiones
    #eliminar la linea completa
    #rotar piezas
    #diferentes tipos de pieza


import pygame
import sys, time
import random


############################################################
#  inicialización del juego
############################################################
global vPosicionX, vPosicionY, nuevo_x, nuevo_y
global bloqueActual

#prueba matriz 1
matriz = [[1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10],
          [1,2,3,4,5,6,7,8,9,10]]


#prueba matriz 2
rows = 10
cols = 20
matrix = [[0] * cols for _ in range(rows)]


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
    
    #intento de recorrer matriz y meter los valores en el x, y.
    prueba = matrix
    filas = len(prueba)
    columnas = len(prueba[0])
    for f in range(filas):
        for c in range(columnas):
                x= f * vBloqueTamano
                y= c * vBloqueTamano
                pygame.draw.rect(vVentana, vColor, (x, y, vBloqueTamano, vBloqueTamano), 1 )
    print()
    

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

    pygame.display.update()


pygame.quit()
sys.exit()

