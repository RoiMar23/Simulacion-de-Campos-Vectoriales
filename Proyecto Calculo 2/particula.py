import numpy as np
import pygame
from config import WHITE

class Particula:
    def __init__(self, pos):
        self.pos = np.array(pos, dtype=float)
        self.vel = np.random.uniform(-2, 2, size=2)
        self.lifetime = 30

    def update(self):
        self.pos += self.vel
        self.lifetime -= 1

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, WHITE, self.pos.astype(int), 3)

def crear_explosion(pos):
    return [Particula(pos) for _ in range(20)]