import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption("arshia_the_monkey")
icon = pygame.image.load('monkey.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 300
playerY = 300
playerX_change = 0


textX = 10
testY = 10

def player(x, y):
    screen.blit(playerImg, (x, y))



# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():

        direction = random.randint(1,4)
        step = random.randint(1,20)
        
        if event.type == pygame.QUIT:
            running = False
        if direction == 1:
            playerX = playerX + step
        elif direction == 2:
            playerX = playerX - step
        elif direction == 3:
            playerY = playerY + step
        elif direction == 4:
            playerY = playerY - step
    player(playerX, playerY)
   
    pygame.display.update()
