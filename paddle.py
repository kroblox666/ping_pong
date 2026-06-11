import pygame
from settings import *

player_rect = pygame.Rect(30, HEIGHT//2-PADDLE_WIDTH//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_rect = pygame.Rect(WIDTH-30, HEIGHT//2-PADDLE_WIDTH//2, PADDLE_WIDTH, PADDLE_HEIGHT)


def update_player():
    keys = pygame.key.get_pressed()
    if keys  [pygame.K_UP] and player_rect.top >0:
        player_rect.y -= PADDLE_SPEED
    
    if keys  [pygame.K_DOWN] and player_rect.bottom <HEIGHT:
        player_rect.y += PADDLE_SPEED
        
def update_ai(ball_rect):
    if ai_rect.centery < ball_rect.centery:
        if ai_rect.bottom < HEIGHT:
            ai_rect.y += AI_SPEED
    if ai_rect.centery > ball_rect.centery:
        if ai_rect.bottom > 0:
            ai_rect.y -= AI_SPEED
    
    
    
def draw_paddle(screen):
    pygame.draw.rect(screen, PADDLE_COLOR, player_rect)
    pygame.draw.rect(screen, PADDLE_COLOR, ai_rect)
    
    
