import numpy as np
import pygame
from config import WIDTH, HEIGHT, RED

class Asteroide:
    def __init__(self):
        self.pos = np.array([np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT)], dtype=float)
        self.vel = np.array([np.random.uniform(-2, 2), np.random.uniform(-2, 2)], dtype=float)
        self.size = np.random.randint(10, 30)

    def update(self):
        self.pos += self.vel
        if self.pos[0] < 0: self.pos[0] = WIDTH
        if self.pos[0] > WIDTH: self.pos[0] = 0
        if self.pos[1] < 0: self.pos[1] = HEIGHT
        if self.pos[1] > HEIGHT: self.pos[1] = 0

    def draw(self, screen):
        # Color plomo para el asteroide principal
        plomo = (120, 120, 120)
        pygame.draw.circle(screen, plomo, (int(self.pos[0]), int(self.pos[1])), self.size)
        # Dibuja cráteres aleatorios
        for _ in range(3):
            angle = np.random.uniform(0, 2 * np.pi)
            dist = np.random.uniform(0.2, 0.7) * self.size
            crater_x = self.pos[0] + dist * np.cos(angle)
            crater_y = self.pos[1] + dist * np.sin(angle)
            pygame.draw.circle(screen, (80, 80, 80), (int(crater_x), int(crater_y)), int(self.size * 0.15))