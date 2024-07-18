import pygame
import sys
sys.path.append('./assets/models/')

from bullet import Bullet
from player import Player
from enemy import Enemy

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
bullets = []

def shoot():
    bullet = Bullet(2, 10, playerOne.body.x + playerOne.size, playerOne.body.y + playerOne.size / 2)
    bullets.append(bullet)

enemy = Enemy(10, -2, WIDTH, HEIGHT / 2)
playerOne = Player("Daniel", 20, 3, 100, HEIGHT / 2)

while running:
    
    screen.fill('black')
     
    pygame.draw.rect(screen, "blue", playerOne.body)
    pygame.draw.rect(screen, "red", enemy.body)
    enemy.body.move_ip(enemy.velocity, 0)

    for bullet in bullets:
        bullet.body.move_ip(bullet.velocity, 0)
        pygame.draw.rect(screen, "orange", bullet.body)

    #KEY EVENT
    key = pygame.key.get_pressed()
    
    if key[pygame.K_UP] == True:
        playerOne.body.move_ip(0, playerOne.velocity*(-1))
    elif key[pygame.K_DOWN] == True:
        playerOne.body.move_ip(0, playerOne.velocity)
    elif key[pygame.K_LEFT] == True:
        playerOne.body.move_ip(playerOne.velocity*(-1), 0)
    elif key[pygame.K_RIGHT] == True:
        playerOne.body.move_ip(playerOne.velocity, 0)
    
    if key[pygame.K_SPACE] == True:
        shoot()
    #GAME EVENTS   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
