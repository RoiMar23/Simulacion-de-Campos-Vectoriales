import pygame
import numpy as np
from config import WIDTH, HEIGHT, GREEN, AMARILLO, AZUL_CLARO

def draw_campo_vectorial(screen, campo_func):
    escala = 30  # Tamaño de las flechas
    for x in range(0, WIDTH, 50):
        for y in range(0, HEIGHT, 50):
            pos = np.array([x, y], dtype=float)
            fuerza = campo_func(pos)
            norma = np.linalg.norm(fuerza)
            if norma > 0:
                dir_flecha = (fuerza / norma) * escala
            else:
                dir_flecha = np.zeros(2)
            end = pos + dir_flecha
            pygame.draw.line(screen, AZUL_CLARO, pos, end, 2)
            # Dibujar cabeza de flecha
            ang = np.arctan2(dir_flecha[1], dir_flecha[0])
            punta = end
            lado1 = punta - 7 * np.array([np.cos(ang - np.pi/6), np.sin(ang - np.pi/6)])
            lado2 = punta - 7 * np.array([np.cos(ang + np.pi/6), np.sin(ang + np.pi/6)])
            pygame.draw.polygon(screen, AZUL_CLARO, [punta, lado1, lado2])