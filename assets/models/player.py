import pygame

class Player:
    def __init__(self, name, size, velocity, x, y):
        self.name = name
        self.size = size
        self.velocity = velocity
        self.body = pygame.Rect((x, y, size, size))
        self.points = 0
        self.hp = 100
