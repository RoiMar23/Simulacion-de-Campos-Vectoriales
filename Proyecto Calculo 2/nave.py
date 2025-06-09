import numpy as np
import pygame
from config import WIDTH, HEIGHT, WHITE

class Nave:
    def __init__(self, campo_func):
        self.pos = np.array([WIDTH // 2, HEIGHT // 2], dtype=float)
        self.vel = np.array([0, 0], dtype=float)
        self.angle = 0
        self.acceleration = 0.1
        self.rotation_speed = 5
        self.campo_func = campo_func  # <-- función del campo vectorial

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.vel[0] += self.acceleration * np.cos(np.radians(self.angle))
            self.vel[1] += self.acceleration * np.sin(np.radians(self.angle))
        
        if keys[pygame.K_SPACE] or keys[pygame.K_TAB]:
            fuerza = self.campo_func(self.pos)
            self.vel += fuerza
        
        if keys[pygame.K_LEFT]:
            self.angle -= self.rotation_speed
        
        if keys[pygame.K_RIGHT]:
            self.angle += self.rotation_speed
        
        self.vel *= 0.99
        self.pos += self.vel
        self.vel *= 0.99
        self.pos = np.clip(self.pos, [0, 0], [WIDTH, HEIGHT])
        
    def draw(self, screen):
        # Coordenadas del triángulo (nave) respecto al centro
        size = 20  # tamaño de la nave
        angle_rad = np.radians(self.angle)  # Convierte a radianes
        x, y = self.pos

        points = [
            (x + size * np.cos(angle_rad), y + size * np.sin(angle_rad)),  # punta
            (x + size * np.cos(angle_rad + 2.5), y + size * np.sin(angle_rad + 2.5)),  # ala izquierda
            (x + size * np.cos(angle_rad - 2.5), y + size * np.sin(angle_rad - 2.5)),  # ala derecha
        ]

        pygame.draw.polygon(screen, (200, 200, 255), points)
        
    def set_campo(self, campo_func):
        self.campo_func = campo_func