import pygame
import sys
from config import *
from utils import draw_text, draw_background
from game_objects import Paddle, Ball
from bricks import create_bricks, draw_bricks

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

# Objetos
paddle = Paddle()
ball = Ball()
score = 0
lives = 3
level = 1
bricks = create_bricks(level)

# Menu inicial
def show_menu():
    draw_background(screen)
    draw_text(screen, "Breakout", 50, WIDTH//2 - 100, HEIGHT//2 - 60)
    draw_text(screen, "Pressione qualquer tecla para começar", 24, WIDTH//2 - 180, HEIGHT//2)
    pygame.display.flip()
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                wait = False

show_menu()

# Loop do jogo
running = True
while running:
    clock.tick(FPS)
    draw_background(screen)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input
    keys = pygame.key.get_pressed()
    paddle.move(keys)

    # Atualização da bola
    ball.update()

    # Colisão com paredes
    if ball.x <= 0 or ball.x >= WIDTH:
        ball.dx *= -1
    if ball.y <= 0:
        ball.dy *= -1
    if ball.y >= HEIGHT:
        lives -= 1
        if lives == 0:
            draw_background(screen)
            draw_text(screen, "Game Over", 50, WIDTH//2 - 100, HEIGHT//2 - 30, RED)
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False
        else:
            ball.reset()

    # Colisão com paddle
    if paddle.rect().collidepoint(ball.x, ball.y + ball.radius):
        ball.dy *= -1

    # Colisão com blocos
    hit_index = ball.rect().collidelist(bricks)
    if hit_index != -1:
        del bricks[hit_index]
        ball.dy *= -1
        score += 10

    # Verifica vitória do nível
    if not bricks:
        level += 1
        paddle.width = max(60, paddle.width - 10)
        bricks = create_bricks(level)
        ball.reset()
        pygame.time.delay(1000)

    # Desenho
    paddle.draw(screen)
    ball.draw(screen)
    draw_bricks(screen, bricks)

    draw_text(screen, f"Pontos: {score}", 24, 10, 10)
    draw_text(screen, f"Vidas: {lives}", 24, WIDTH - 120, 10)
    draw_text(screen, f"Nível: {level}", 24, WIDTH//2 - 40, 10)

    pygame.display.flip()

pygame.quit()
