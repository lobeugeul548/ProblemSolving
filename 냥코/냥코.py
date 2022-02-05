import pygame
import sys

height = 1300
weight = 650
size = height, weight
screen = pygame.display.set_mode(size)
background = pygame.image.load("Battle_cats_background(원본).png")
title = "냥코대전쟁"
pygame.display.set_caption(title)
pygame.init()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()
sys.exit()
