import pygame

class Player:
    def __init__(self, name, size, velocity, x, y):
        self.name = name
        self.size = size
        self.velocity = velocity
        #self.body = pygame.Rect((100, HEIGHT/2, size, size))
        self.body = pygame.Rect((x, y, size, size))
