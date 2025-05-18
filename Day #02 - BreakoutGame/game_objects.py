import pygame
import random
from config import *

class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 30
        self.speed = 7

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Ball:
    def __init__(self):
        self.radius = 10
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.choice([-4, 4])
        self.dy = -4

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)


def create_bricks(level):
    bricks = []
    rows = 5 + level
    cols = 10
    brick_width = WIDTH // cols
    brick_height = 20

    for row in range(rows):
        for col in range(cols):
            x = col * brick_width
            y = row * brick_height + 50
            brick = pygame.Rect(x, y, brick_width, brick_height)
            bricks.append(brick)
    return bricks


def draw_bricks(screen, bricks):
    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)
        pygame.draw.rect(screen, BLACK, brick, 2)  # contorno preto
