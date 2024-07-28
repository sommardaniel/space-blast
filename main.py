import pygame
import sys
import random
from threading import Timer
sys.path.append('./assets/models/')

from player import Player
from enemy import Enemy
from spritesheet import Spritesheet

WIDTH = 800
HEIGHT = 600

tick = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(),36)
running = True
debug = True
debugString = "Debug: "
text_surface = font.render(debugString, True, (255, 255, 255))
space_spritesheet = Spritesheet('./assets/sprites/ships.png')

enemys = []
playerOne = Player("Daniel", 32, 3, 100, HEIGHT / 2, space_spritesheet.getSprite(68,62,16,16))
playerOne.sprite = pygame.transform.scale(playerOne.sprite, (32,32))

def handleKeyEvents(key):
    global debug, running
   
    if key[pygame.K_UP] == True:
        playerOne.body.move_ip(0, playerOne.velocity*(-1))
    if key[pygame.K_DOWN] == True:
        playerOne.body.move_ip(0, playerOne.velocity)
    if key[pygame.K_LEFT] == True:
        playerOne.body.move_ip(playerOne.velocity*(-1), 0)
    if key[pygame.K_RIGHT] == True:
        playerOne.body.move_ip(playerOne.velocity, 0)
    
    if key[pygame.K_SPACE] == True:
        playerOne.shoot()
    elif key[pygame.K_q] == True:
        if debug == True:
            debug = False
        else:
            debug = True
    elif key[pygame.K_ESCAPE] == True:
        running = False

def draw():
    screen.fill('black')
    
    screen.blit(playerOne.sprite, (playerOne.body.x, playerOne.body.y))

    for enemy in enemys:
        screen.blit(enemy.sprite, (enemy.body.x, enemy.body.y))
        for bullet in enemy.bullets:
            pygame.draw.rect(screen, "white", bullet.body)

    for bullet in playerOne.bullets:
        pygame.draw.rect(screen, "orange", bullet.body)
    
    if debug == True:
        debugString = "HP: " + str(playerOne.hp) + ",Points: " + str(playerOne.points)
        text_surface = font.render(debugString, True, (255, 255, 255))
        screen.blit(text_surface, dest=(20,40))

def handleEvents():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
def handleAI():
    global tick
    #update timer and fire every n seconds
    if tick < int(pygame.time.get_ticks()/1000):
        tick+=1
        if tick%2:
            enemyShoot()
    
    #handle player bullets
    for bullet in playerOne.bullets:
        if bullet.body.x > WIDTH:
            playerOne.bullets.remove(bullet)
        handleBulletCollission(bullet)
        bullet.body.move_ip(bullet.velocity, 0)
    
    #handle enemy bullets and collissons
    for enemy in enemys:
        for bullet in enemy.bullets:
            if bullet.body.x > WIDTH:
                enemy.bullets.remove(bullet)
            handleBulletCollission(bullet, enemy)
            bullet.body.move_ip(bullet.velocity, 0)
        
        handleEnemyCollission(enemy)
        enemy.body.move_ip(enemy.velocity, 0)
        if enemy.body.x < 0:
            enemys.remove(enemy)
            spawnEnemy()

def handleEnemyCollission(enemy): #TODO delay function if hit
    x = abs(playerOne.body.x - enemy.body.x)
    y = abs(playerOne.body.y - enemy.body.y)

    if x < 10 and y < 10:
        playerOne.hp -= 25

def handleBulletCollission(bullet, enemy = False):
    if enemy:
        x = abs(playerOne.body.x - bullet.body.x)
        y = abs(playerOne.body.y - bullet.body.y)
        if x < 10 and y < 10:
            playerOne.hp-=25
            try:
                enemy.bullets.remove(bullet)
            except:
                print('Error removing bullet')

    else:
        for enemy in enemys:
            x = abs(enemy.body.x - bullet.body.x)
            y = abs(enemy.body.y - bullet.body.y)
            if x < 10 and y < 10:
                playerOne.points+=1
                spawnEnemy()
                try:
                    enemys.remove(enemy)
                    playerOne.bullets.remove(bullet)
                except:
                    print('Error removing bullet')


def spawnEnemy():
    enemy = Enemy(20, -2, random.randint(WIDTH, WIDTH + 50), random.randint(100, HEIGHT - 100), space_spritesheet.getSprite(16*15+8,16*5+2,16,16))
    enemy.sprite = pygame.transform.scale(enemy.sprite, (20,20))
    enemys.append(enemy)

def enemyShoot():
    for enemy in enemys:
        enemy.shoot()
def init():
    for x in range(3):
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
