import pygame
from config import WHITE, WIDTH, HEIGHT, DARK_BLUE

def draw_text(screen, text, size, x, y, color=WHITE):
    font_obj = pygame.font.SysFont("Arial", size)
    render = font_obj.render(text, True, color)
    screen.blit(render, (x, y))

def draw_background(screen):
    screen.fill(DARK_BLUE)
    for i in range(0, HEIGHT, 40):
        pygame.draw.line(screen, (20, 20, 50), (0, i), (WIDTH, i), 1)
