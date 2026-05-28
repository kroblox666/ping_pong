import pygame
from settings import *
ball_rect = pygame.Rect(WIDTH//2-BALL_SIZE//2, HEIGHT//2-BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

def draw_ball(screen):
    pygame.draw.ellipse(screen, BALL_COLOR, ball_rect)
    
    