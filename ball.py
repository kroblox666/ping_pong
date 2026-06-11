import pygame
import random
from settings import *
ball_rect = pygame.Rect(WIDTH//2-BALL_SIZE//2, HEIGHT//2-BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

def reset_ball():
    global ball_dx, ball_dy
    ball_rect.center = (WIDTH//2, HEIGHT//2)
    ball_dx = BALL_SPEED * random.choice([-1, 1])
    ball_dy = BALL_SPEED * random.choice([-1, 1])

def update_ball():
    global ball_dy
    ball_rect.x += ball_dx
    ball_rect.y += ball_dy
    
    if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
        ball_dy = -ball_dy

def bounce_x():
    global ball_dx
    ball_dx = -ball_dx






def draw_ball(screen):
    pygame.draw.ellipse(screen, BALL_COLOR, ball_rect)
    
