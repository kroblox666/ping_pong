import pygame
from settings import *
import ball

pygame.init()

pygame.display.set_caption("пинг? понг!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()




    screen.fill((0, 0, 0))

    ball.draw_ball(screen)

    pygame.display.update()
    clock.tick(FPS)