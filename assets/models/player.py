import pygame
from bullet import Bullet 

class Player:
    def __init__(self, name, size, velocity, x, y, sprite):
        self.name = name
        self.size = size
        self.velocity = velocity
        self.body = pygame.Rect((x, y, size, size))
        self.points = 0
        self.hp = 100
        self.bullets = []
        self.sprite = sprite

    
    def shoot(self):
        bullet = Bullet(2, 25, self.body.x + self.size, self.body.y + self.size / 2)
        self.bullets.append(bullet)
