import pygame
from bullet import Bullet 

class Enemy:
    def __init__(self, size, velocity, x, y):
        self.size = size
        self.velocity = velocity
        self.body = pygame.Rect((x, y, size, size))
        self.bullets = []

    def shoot(self):
        bullet = Bullet(2, 25, self.body.x + self.size, self.body.y + self.size / 2)
        self.bullets.append(bullet)
