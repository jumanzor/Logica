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

#vColor para el fondo
vColor = (255, 255, 255)

#Colores es una lista de colores el cual agarra un valor al azar (0,1,2,3,4,5,6,7...) 
#y le da el "valor completo" al metodo
colores = [
    (255, 0, 0),     # Rojo
    (0, 255, 0),     # Verde
    (0, 0, 255),     # Azul
    (255, 255, 0),   # Amarillo
    (255, 0, 255),   # Magenta
    (0, 255, 255),   # Cian
    (255, 165, 0),   # Naranja
    (128, 0, 128),   # Púrpura
    (255, 140, 0),   # Naranja oscuro
    (0, 128, 0)      # Verde oscuro
]

colorActual=random.choice(colores)

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
    filas = len(matrix)
    columnas = len(matrix[0])
    for f in range(filas):
        for c in range(columnas):
                x= f * vBloqueTamano
                y= c * vBloqueTamano
                pygame.draw.rect(vVentana, vColor, 
                                 (x, y, vBloqueTamano, vBloqueTamano), 1 )
    
    #Este metodo recorre el tamaño de bloqueactual y para poder pintarlo lo suma por vPosicionX y vPosicionY 
    # y lo multiplica por el tamaño del bloque
def dibujaBloqueActual():
            #el primer len agarra la cantidad de filas
    for i in range(len(bloqueActual)):
            #y el bloqueactual[i] las columnas
        for j in range(len(bloqueActual[i])):
            if bloqueActual[i][j] != 0:
                x = (j + vPosicionX) * vBloqueTamano
                y = (i + vPosicionY) * vBloqueTamano
                pygame.draw.rect(vVentana, colorActual, 
                                 (x, y, vBloqueTamano, vBloqueTamano))
                #seteo el tick aquí para cuando la caida pase esta no sea super rápida
                pygame.time.Clock().tick(25)
       
                
    #para que caiga la pieza necesito recorrer el bloque actual y quitarle en Y hasta que.... 
    #anteriormente definí una varible global vPosicionY la cual ya estaba en 0 
    # y usándose para crear la pieza, ahora solo necestito restarle   
def caidaPieza():
    global vPosicionY
    if vPosicionY < vCantidadFilas - len(bloqueActual):
       vPosicionY +=1
    #tengo un problema que va rapidísimo  
    
    #sacado mediente internet
def rotaBloque():
    global bloqueActual
    bloqueActual = [list(row) for row in zip(*reversed(bloqueActual))] 
             
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

pygame.display.set_caption("Tetris")
ejecutando = True

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
            #este event.type recibe señales del teclado entonces
            # meti que cuando la tecla sea felcha izqui o derecha
            # le sume o le reste a la posicion que ya se está usando al crear los bloques
            # además de bloquear los numeros para el movimiento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ejecutando = False
            if event.key ==pygame.K_LEFT and vPosicionX > 0:
                vPosicionX -= 1
            if event.key == pygame.K_RIGHT and vPosicionX < 7:
                vPosicionX +=1
            if event.key == pygame.K_DOWN and vPosicionY > 19:
                vPosicionY +=1
            if event.key == pygame.K_UP:
                rotaBloque()
            
    vVentana.fill((0, 0, 0))

    dibujaBloqueActual()
    caidaPieza()
    dibujaCuadricula()

    pygame.display.update()

pygame.quit()
sys.exit()


