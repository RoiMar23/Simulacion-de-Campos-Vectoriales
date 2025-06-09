import pygame
import numpy as np
from config import WIDTH, HEIGHT, BLACK, FPS
from nave import Nave
from asteroide import Asteroide
from particula import crear_explosion
from particula import Particula
from campo_vectorial import draw_campo_vectorial
from campos import campo_circular, campo_radial


def detectar_colision(nave, asteroide):
    distancia = np.linalg.norm(nave.pos - asteroide.pos)
    return distancia < asteroide.size

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Asteroides en Campo Vectorial")
    clock = pygame.time.Clock()

    centro = np.array([WIDTH // 2, HEIGHT // 2])
    
    campo_func = lambda pos: campo_circular(pos)
    nave = Nave(campo_func)
    asteroides = [Asteroide() for _ in range(5)]
    particulas = [] 
    running = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                nave = Nave(campo_func=campo_func)
                particulas = []
                pygame.time.set_timer(pygame.USEREVENT, 0)
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    campo_func = lambda pos: campo_circular(pos)
                    if nave is not None:
                        nave.set_campo(campo_func)
                    else:
                        nave = Nave(campo_func=campo_func)
                elif event.key == pygame.K_TAB:
                    campo_func = lambda pos: campo_radial(pos, centro)
                    if nave is not None:
                        nave.set_campo(campo_func)
                    else:
                        nave = Nave(campo_func=campo_func)

        if nave is not None:
            nave.update()

        for asteroide in asteroides:
            asteroide.update()
            if nave is not None and detectar_colision(nave, asteroide):
                particulas = crear_explosion(nave.pos.copy())
                nave = None
                pygame.time.set_timer(pygame.USEREVENT, 2000)

        draw_campo_vectorial(screen, campo_func)
        if nave is not None:
            nave.draw(screen)
            
        for asteroide in asteroides:
            asteroide.draw(screen)
            
        for p in particulas:
            p.update()
            p.draw(screen)
        particulas = [p for p in particulas if p.lifetime > 0]
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()