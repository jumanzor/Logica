

print("hola mundo")
print("hola mundo")
print("hola mundo")















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
            #fila 1
            pygame.draw.rect(vVentana, vColor, (0, 0, vBloqueTamano, vBloqueTamano), 1 )
            pygame.draw.rect(vVentana, vColor, (40,0 , vBloqueTamano, vBloqueTamano), 1 )
            pygame.draw.rect(vVentana, vColor, (80,0 , vBloqueTamano, vBloqueTamano), 1 )
            pygame.draw.rect(vVentana, vColor, (120,0 , vBloqueTamano, vBloqueTamano), 1 )
            #fila 2
            pygame.draw.rect(vVentana, vColor, (0, 40, vBloqueTamano, vBloqueTamano), 1 )
            pygame.draw.rect(vVentana, vColor, (40,40 , vBloqueTamano, vBloqueTamano), 1 )
            pygame.draw.rect(vVentana, vColor, (80,40 , vBloqueTamano, vBloqueTamano), 1 )
            pygame.draw.rect(vVentana, vColor, (120,40 , vBloqueTamano, vBloqueTamano), 1 )
            #fila 3
            pygame.draw.rect(vVentana, vColor, (0, 80, vBloqueTamano, vBloqueTamano), 1 )
            pygame.draw.rect(vVentana, vColor, (40,80 , vBloqueTamano, vBloqueTamano), 1 )
            pygame.draw.rect(vVentana, vColor, (80,80 , vBloqueTamano, vBloqueTamano), 1 )
            pygame.draw.rect(vVentana, vColor, (120,80 , vBloqueTamano, vBloqueTamano), 1 )


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


'''