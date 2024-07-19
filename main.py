import pygame
import sys
import random

sys.path.append('./assets/models/')

from bullet import Bullet
from player import Player
from enemy import Enemy

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(),36)
running = True
debug = True
debugString = "Debug: "

text_surface = font.render(debugString, True, (255, 255, 255))

bullets = []
enemys = []
playerOne = Player("Daniel", 20, 3, 100, HEIGHT / 2)

def shoot():
    bullet = Bullet(2, 25, playerOne.body.x + playerOne.size, playerOne.body.y + playerOne.size / 2)
    bullets.append(bullet)

def handleKeyEvents(key):
    global debug, running
   
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
    elif key[pygame.K_q] == True:
        if debug == True:
            debug = False
        else:
            debug = True
    elif key[pygame.K_ESCAPE] == True:
        running = False

def draw():
    screen.fill('black')
     
    pygame.draw.rect(screen, "blue", playerOne.body)

    for enemy in enemys:
        pygame.draw.rect(screen, "red", enemy.body)
    
    for bullet in bullets:
        pygame.draw.rect(screen, "orange", bullet.body)

    if debug == True:
        debugString = "HP: " + str(playerOne.hp) + ",Points: " + str(playerOne.points) + " ,Bullets: " + str(len(bullets)) + ", Enemys: " + str(len(enemys))
        text_surface = font.render(debugString, True, (255, 255, 255))
        screen.blit(text_surface, dest=(20,40))

def handleEvents():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
def handleAI(): 
    for bullet in bullets:
        if bullet.body.x > WIDTH:
            bullets.remove(bullet)
        handleEnemyBulletCollission(bullet)
        bullet.body.move_ip(bullet.velocity, 0)
    
    for enemy in enemys:
        handleEnemyCollission(enemy)
        enemy.body.move_ip(enemy.velocity, 0)
        if enemy.body.x < 0:
            enemys.remove(enemy)
            spawnEnemy()

def handleEnemyCollission(enemy): #TODO delay function if hit
    global running
    x = abs(playerOne.body.x - enemy.body.x)
    y = abs(playerOne.body.y - enemy.body.y)

    if x < 10 and y < 10:
        playerOne.hp -= 25

def handleEnemyBulletCollission(bullet):
    for enemy in enemys:
        x = abs(enemy.body.x - bullet.body.x)
        y = abs(enemy.body.y - bullet.body.y)
        if x < 10 and y < 10:
            playerOne.points+=1
            enemys.remove(enemy)
            bullets.remove(bullet)
            spawnEnemy()


def spawnEnemy():
    enemy = Enemy(10, -2, random.randint(WIDTH, WIDTH + 50), random.randint(100, HEIGHT - 100))
    enemys.append(enemy)

def init():
    spawnEnemy()
    spawnEnemy()
    spawnEnemy()

init()

while running and playerOne.hp > 0:
    draw()
    handleKeyEvents(pygame.key.get_pressed())
    handleAI()
    handleEvents()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
