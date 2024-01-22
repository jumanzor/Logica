#Cristofer C26901

print('hola mundo...')

import pygame
import sys, time
import random


############################################################
#  inicialización del juego
############################################################
global vPosicionX, vPosicionY, nuevo_x, nuevo_y
global bloqueActual

#prueba matriz 
filas = 10
columnas = 20
matrix = [[0 for c in range(columnas)] for f in range(filas)]


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

# Configuración de bloques
BloqueT = [
    [0, 1, 0],
    [1, 1, 1]
]

BloqueL = [
    [0, 0, 2],
    [2, 2, 2]
]

BloqueI = [
    [3, 3, 3, 3]
]

BloqueO = [
    [4, 4],
    [4, 4]
]

BloqueS = [
    [5, 5, 0],
    [0, 5, 5]
]

BloqueS2 = [
    [0, 6, 6],
    [6, 6, 0]
]

#bloques es una lista que almacena las listas con las formas de los bloques
bloques = [BloqueT, BloqueL, BloqueI, BloqueO, BloqueS, BloqueS2]
    
#bloqueActual usa bloques para generar un numero random y imprimirlo en la matriz
bloqueActual = random.choice(bloques)

############################################################
#  funciones
############################################################


    #el metodo dibujar cuadricula usa el len(matriz) para no salirse de los limites,
    #recorre filas y columnas multiplicados por el tamaño del bloque para dar tamaño a las celdas
    #y pinta el rectangulo
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
    
    
    #Este metodo recorre el tamaño de bloqueactual y para poder pintarlo lo suma por vPosicionX y vPosicionY 
    # y lo multiplica por el tamaño del bloque
def dibujaBloqueActual():
    for i in range(len(bloqueActual)):
        for j in range(len(bloqueActual[i])):
            if bloqueActual[i][j] != 0:
                x = (j + vPosicionX) * vBloqueTamano
                y = (i + vPosicionY) * vBloqueTamano
                pygame.draw.rect(vVentana, vColor, (x, y, vBloqueTamano, vBloqueTamano))
                
                
#def caidaPieza():

#def colision():
                
                
############################################################
#  inicia el juego
############################################################

# inicia el game loop
    #establece la posición inicial en el eje X para el bloque
    #vCantidadColumnas // 2 agarra la mitad de la cuadrícula para que la pieza salga centrada
    #len(bloqueActual[0]) // 2 mitad del ancho del bloque actual en el eje X
#ejemplo, si se pone en 0 la figura se formará en la esquina izquierda y Y si es 0 porque las queremos arriba
vPosicionX = vCantidadColumnas // 2 - len(bloqueActual[0]) // 2
vPosicionY = 0

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

    dibujaBloqueActual()
    dibujaCuadricula()
    

    pygame.display.update()


pygame.quit()
sys.exit()


