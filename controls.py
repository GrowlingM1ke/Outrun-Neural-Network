import pygame
from pygame.locals import *

class Controls:

    def inputs(self, event, keys):
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                event.type = pygame.QUIT
            elif event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    def output(self, event):
        if event.type == pygame.QUIT:
            exit(0)