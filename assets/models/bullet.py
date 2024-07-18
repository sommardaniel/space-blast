import pygame

class Bullet:
    def __init__(self, size, velocity, x, y):
        self.size = size
        self.velocity = velocity
        self.body = pygame.Rect((x, y, size, size))

