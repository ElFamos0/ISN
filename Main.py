# -*- coding : utf8 -*-

import pygame
pygame.init()
res = (1920, 1080)
screen = pygame.display.set_mode(res, pygame.RESIZABLE)

lance = True

while lance:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lance = False
