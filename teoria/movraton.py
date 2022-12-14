import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Movimiento Raton")
#Colores
colorFondo = (1, 150, 70)
colorFigura = (255, 255, 255)
#variables 
velocidad = 5
direccion = True
posX, posY = randint(1, 400), randint(1, 300)
lado = 40

while True:
    ventana.fill(colorFondo)
    pygame.draw.rect(ventana, colorFigura, (posX, posY, lado, lado))
    #detecta movimiento ratón
    posX, posY = pygame.mouse.get_pos()
    posX = posX - lado/2
    posY = posY - lado/2
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()