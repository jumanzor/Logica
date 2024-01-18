print("Hola, mundo")
print("Buenas, como están?")

print("Hola, mundo")
print("Hola, mundo")
print("Hola, mundo")

#Gabo
print("Todo bien mi estimado :) ")
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
#Color de la cuadricula
vColor = (255, 255, 255)
#Color del cubo
vColorBloque = (0, 255, 0)

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

# Sukuna el que me modifique o copie el codigo 

def dibujaCuadricula():
            """""
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
            """
def dibujaCuadricula():
     for fila in range (vCantidadFilas):
          for columnas in range (vCantidadColumnas):
               x=columnas*vBloqueTamano
               y=fila*vBloqueTamano
               pygame.draw.rect(vVentana, vColor, (x, y, vBloqueTamano, vBloqueTamano), 1 )
          
#Posicion del bloque 
vPosicionX=vVentanaAncho//2 - vBloqueTamano*2
vPosiciony=0
#Movimiento bloque 
velocidad_caida=1

#Movimiento Derecha y izquierda
velocidad_horizontal=5

#Selección de teclas para moverse
tecla_izquierda=pygame.K_LEFT
tecla_derecha=pygame.K_RIGHT
#Colisión con borde
def colision_con_borde(x,y,tamano):
        return (
            x < 0 or
            x + tamano > vVentanaAncho or
            y +tamano > vVentanaAlto
        )

#Movimientos
def movimiento(event):
    global vPosicionX, velocidad_horizontal
    if event.type == pygame.KEYDOWN:
        if event.key == tecla_izquierda:
            vPosicionX -= velocidad_horizontal
            if colision_con_borde(vPosicionX, vPosiciony, vBloqueTamano * 2):
                vPosicionX += velocidad_horizontal
        elif event.key == tecla_derecha:
            vPosicionX += velocidad_horizontal
            if colision_con_borde(vPosicionX, vPosiciony, vBloqueTamano * 2):
                vPosicionX -= velocidad_horizontal


# Lista de colores de bloques
colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Definir tipos de bloques
bloques = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
]

# Seleccionar un bloque aleatorio
bloqueActual = random.choice(bloques)
bloqueColor = random.choice(colores)

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
   #Caída
    vPosiciony+=velocidad_caida
    #Dibujar cuadricula
    dibujaCuadricula()
    movimiento(event)
    #Dibuja el cuadrado
    
    #pygame.draw.rect(vVentana, vColorBloque, (vPosicionX, vPosiciony, vBloqueTamano * 4, vBloqueTamano * 4), 1)

    #Dibuja diferentes bloques
     
    # Dibuja el bloque actual
    for fila in range(len(bloqueActual)):
        for columna in range(len(bloqueActual[0])):
            if bloqueActual[fila][columna] == 1:
                x = (columna * vBloqueTamano) + vPosicionX
                y = (fila * vBloqueTamano) + vPosiciony
                pygame.draw.rect(vVentana, bloqueColor, (x, y, vBloqueTamano, vBloqueTamano), 1)
                
    #Colisión con el suelo
    if vPosiciony + vBloqueTamano * 2 >= vVentanaAlto:
        vPosiciony = vVentanaAlto - vBloqueTamano * 2
    #Actualiza
    pygame.display.update()
    #Tiempo de caída
    pygame.time.Clock().tick(20)


pygame.quit()
sys.exit()