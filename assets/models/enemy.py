import pygame
from bullet import Bullet 

class Enemy:
    def __init__(self, size, velocity, x, y, sprite):
        self.size = size
        self.velocity = velocity
        self.body = pygame.Rect((x, y, size, size))
        self.bullets = []
        self.sprite = sprite

    def shoot(self):
        bullet = Bullet(2, -5, self.body.x + self.size, self.body.y + self.size / 2)
        self.bullets.append(bullet)
