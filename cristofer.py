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
matriz = [[0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0]]


#prueba matriz 2
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
    
    
#ficha
class ficha:
    x = 0 #x, y para meter en el metodo pygame.draw.rect
    y = 0
    figura = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]] #cuadrado
    ] 
    
    #Hasta aqui no sé como implementar las fichas
    def recorrerficha(): #este metodo ya es capaz de repintar sobre la primer cuadrícula
        test = ficha.figura
        for f in range(4):
            for ff in range(4):
                x = f * vBloqueTamano
                y = ff * vBloqueTamano
                pygame.draw.rect(vVentana, (100, 100, 100), (x, y, vBloqueTamano, vBloqueTamano), 1 )


    

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
    ficha.recorrerficha()

    pygame.display.update()


pygame.quit()
sys.exit()

#piezas
  #imagino que es crear un objeto 
#que necesito?, crear el objeto, que se dibuje, que se mueva


