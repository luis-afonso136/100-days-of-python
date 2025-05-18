# bricks.py
import pygame
from config import BRICK_WIDTH, BRICK_HEIGHT, BRICK_ROWS, BRICK_COLUMNS, PADDING, BLACK

# Cores diferentes para cada linha
BRICK_COLORS = [
    (255, 0, 0),     # Vermelho
    (255, 165, 0),   # Laranja
    (255, 255, 0),   # Amarelo
    (0, 128, 0),     # Verde
    (0, 255, 255),   # Ciano
    (0, 0, 255),     # Azul
    (128, 0, 128),   # Roxo
]

class Brick:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)
        pygame.draw.rect(screen, (0, 0, 0), self, 2)  # contorno preto

def create_bricks(level):
    bricks = []
    for row in range(BRICK_ROWS):
        color = BRICK_COLORS[row % len(BRICK_COLORS)]
        for col in range(BRICK_COLUMNS):
            x = col * (BRICK_WIDTH + PADDING) + PADDING
            y = row * (BRICK_HEIGHT + PADDING) + PADDING
            bricks.append(Brick(x, y, color))
    return bricks


def draw_bricks(screen, bricks):
    for brick in bricks:
        pygame.draw.rect(screen, brick.color, brick.rect)            # Bloco colorido
        pygame.draw.rect(screen, (0, 0, 0), brick.rect, 2)            # Contorno preto



