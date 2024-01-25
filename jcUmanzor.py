


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
import sys
import random


############################################################
#  inicialización del juego
############################################################
global vPosicionX, vPosicionY, nuevo_x, nuevo_y
global bloqueActual

# Manejo de variables
pygame.init()
pygame.mixer.init()
vSonidoColision = pygame.mixer.Sound('choque.mp3')
vSonidoColision.set_volume(0.3)

# Posibles colores a pintar
vColores = [(255, 255, 255), (255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0),(255, 0, 255), (0, 255, 255)]

# Configuración de la ventana de inicio
ventana_inicio_ancho = 500
ventana_inicio_alto = 500
imagenInicio = pygame.image.load('tetris.jpg')
imagen = pygame.transform.scale(imagenInicio, (300, 200))

# Configuración de la ventana
vVentanaAncho = 401
vVentanaAlto = 601



# Configuración de la cuadrícula a dibujar
vCantidadFilas = 15
vCantidadColumnas = 10
vBloqueTamano = vVentanaAncho // vCantidadColumnas

# Inicialización de la cuadrícula de juego
vCuadricula = []

for _ in range(vCantidadFilas):
    fila = [0] * vCantidadColumnas
    vCuadricula.append(fila)


# Velocidad de caída y tiempo de caída
vTiempoCaida = 600  # Tiempo en milisegundos
vTiempoEvento = pygame.USEREVENT + 1
pygame.time.set_timer(vTiempoEvento, vTiempoCaida)



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
    [5, 5, 0, 0],
    [0, 0, 5, 5]
]

BloqueS2 = [
    [0, 0, 6, 6],
    [6, 6, 0, 0]
]

bloques = [BloqueT, BloqueL, BloqueI, BloqueO, BloqueS, BloqueS2]


############################################################
#  funciones
############################################################

def dibujaCuadriculaCompleta():
    for y in range(vCantidadFilas):
        for x in range(vCantidadColumnas):
            pygame.draw.rect(vVentana, 
                             vColores[vCuadricula[y][x]], 
                             (x * vBloqueTamano, y * vBloqueTamano, vBloqueTamano, vBloqueTamano),
                                1 if vCuadricula[y][x] == 0 else 0)

def dibujaBloqueActual(bloque):
    for y in range(len(bloque)):
        for x in range(len(bloque[0])):
            if bloque[y][x] != 0:
                pygame.draw.rect(vVentana, 
                                 vColores[bloque[y][x]], 
                                 (vPosicionX * vBloqueTamano + x * vBloqueTamano,
                                                                 vPosicionY * vBloqueTamano + y * vBloqueTamano,
                                                                 vBloqueTamano, vBloqueTamano))

def moverBloque(x_offset, y_offset, bloque):
    global bloqueActual, vPosicionX, vPosicionY
    if colisionBloque(bloque):
        vSonidoColision.play()
        nuevo_bloque = False
        anclarBloque(bloque, vPosicionX, vPosicionY)
        bloqueActual = random.choice(bloques)
        vPosicionX = 4
        vPosicionY = 0            
        limpiarFila()
    else:
        nuevo_x = vPosicionX + x_offset
        nuevo_y = vPosicionY + y_offset
        if all(0 <= nuevo_x + x < vCantidadColumnas and 0 <= nuevo_y + y < vCantidadFilas
                for x in range(len(bloque[0])) for y in range(len(bloque)) if bloque[y][x] != 0):
            vPosicionX = nuevo_x
            vPosicionY = nuevo_y

def limpiarFila():
    for i, fila in enumerate(vCuadricula):
        if all(fila):
            vCuadricula.pop(i)
            vCuadricula.insert(0, [0 for _ in range(vCantidadColumnas)])


def colisionBloque(bloque):
    for y, fila in enumerate(bloque):
        for x, valor in enumerate(fila):
            if valor != 0:
                fila_actual = vPosicionY + y + 1
                columna_actual = vPosicionX + x
                if fila_actual >= vCantidadFilas or vCuadricula[fila_actual][columna_actual] != 0:
                    return True
    return False


def anclarBloque(bloque, vPosicionX, vPosicionY):
    for y, fila in enumerate(bloque):
        for x, valor in enumerate(fila):
            if valor != 0:
                vCuadricula[vPosicionY + y][vPosicionX + x] = valor


def rotarBloque(bloque):
    global bloqueActual
    bloqueActual = list(zip(*bloque[::-1]))


############################################################
#  inicia el juego
############################################################


# se define bloque inicial y posición inicial del bloque
bloqueActual = random.choice(bloques)
vPosicionX = 4
vPosicionY = 0

ventana_inicio = pygame.display.set_mode((ventana_inicio_ancho, ventana_inicio_alto))
pygame.display.set_caption("Pantalla de Inicio")
pantalla_inicio = True

# Bucle pantalla inicio 
while pantalla_inicio:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pantalla_inicio = False  

    ventana_inicio.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    texto_grande = font.render("TETRIS", True, (255, 255, 255))
    texto_pequeno = font.render("Presione una tecla para comenzar", True, (255, 255, 255))
    ventana_inicio.blit(texto_grande, (ventana_inicio_ancho // 2 - texto_grande.get_width() // 2, 50))
    ventana_inicio.blit(texto_pequeno, (ventana_inicio_ancho // 2 - texto_pequeno.get_width() // 2, 120))
    ventana_inicio.blit(imagen, (110, 200)) 
    pygame.display.update()


# inicia el game loop
vVentana = pygame.display.set_mode((vVentanaAncho, vVentanaAlto))
pygame.display.set_caption("Juego del Tetris")
ejecutando = True

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rotarBloque(bloqueActual)
            if event.key == pygame.K_ESCAPE:
                ejecutando = False
            if event.key == pygame.K_LEFT:
                moverBloque(-1, 0, bloqueActual)
            if event.key == pygame.K_RIGHT:
                moverBloque(1, 0,bloqueActual)
        elif event.type == vTiempoEvento:
                moverBloque(0,1,bloqueActual)


    vVentana.fill((0, 0, 0))

    dibujaBloqueActual(bloqueActual)
    dibujaCuadriculaCompleta()

    pygame.display.update()


pygame.quit()
sys.exit()