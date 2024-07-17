import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

class Player:
    def __init__(self, name, size, velocity):
        self.name = name
        self.size = size
        self.velocity = velocity
        self.body = pygame.Rect((100, HEIGHT/2, size, size))


class Enemy:
    def __init__(self, size, velocity):
        self.size = size
        self.velocity = velocity
        self.body = pygame.Rect((WIDTH, HEIGHT/2, size, size))

class Bullet:
    def __init__(self, size, velocity, x, y):
        self.size = size
        self.velocity = velocity
        self.body = pygame.Rect((x, y, size, size))

#def spawnEnemy():

bullets = []

def shoot():
    bullet = Bullet(2, 10, playerOne.body.x + playerOne.size, playerOne.body.y + playerOne.size / 2)
    bullets.append(bullet)

enemy = Enemy(10, -2)
playerOne = Player("Daniel", 20, 3)

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
