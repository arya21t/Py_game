import pygame
import time
import sys

pygame.init()

pygame.display.set_caption("Ninja game")
screen = pygame.display.set_mode((320,568))

clock = pygame.time.Clock()

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   