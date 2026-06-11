import pygame
from settings import *
import ball
import paddle

pygame.init()

pygame.display.set_caption("пинг? понг!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball.reset_ball()
font = pygame.font.SysFont(None, 52)

player_score = 0
ai_score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    ball.update_ball()
    paddle.update_player()
    paddle.update_ai(ball.ball_rect)
    

    hit_player = ball.ball_rect.colliderect(paddle.player_rect)
    hit_ai = ball.ball_rect.colliderect(paddle.ai_rect)
    if hit_player or hit_ai:
        ball.bounce_x()
        
        
        
    if ball.ball_rect.left > WIDTH:
        player_score += 1
        ball.reset_ball()
    if ball.ball_rect.left < 0:
        ai_score += 1
        ball.reset_ball()

    screen.fill((0, 0, 0))

    ball.draw_ball(screen)
    paddle.draw_paddle(screen)
    score_text = font.render(str(player_score) +" " + str(ai_score), True,"white")
    screen.blit(score_text, (WIDTH//2-score_text.get_width()//2,15))

    pygame.display.update()
    clock.tick(FPS)