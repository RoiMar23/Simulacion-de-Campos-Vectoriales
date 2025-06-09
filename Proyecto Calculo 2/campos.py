import numpy as np

def campo_circular(pos):
    """Campo en forma de espiral: F = (y, -x)"""
    fuerza_x = pos[1] * 0.0005
    fuerza_y = -pos[0] * 0.0005
    return np.array([fuerza_x, fuerza_y])

def campo_radial(pos, centro):
    """Campo que apunta hacia afuera desde un centro dado"""
    delta = centro - pos
    fuerza = delta * 0.0005
    return fuerza

def campo_nulo(pos):
    """Sin campo (para desactivarlo)"""
    return np.array([0.0, 0.0])

def campo_random(pos):
    """Campo aleatorio"""
    return np.random.uniform(-0.1, 0.1, size=2)
