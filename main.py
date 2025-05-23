import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("XCOPIA")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  #fill the screen with black
    pygame.display.flip()  #Update the display
    clock.tick(60)  #Limit to 60 frames per second

pygame.quit()
sys.exit()