import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

speed = 3

class Player:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.body = pygame.Rect((100, HEIGHT/2, size, size))

playerOne = Player("Daniel", 20)

while running:
    
    screen.fill('black')
    
    pygame.draw.rect(screen, "blue", playerOne.body)
    
    #KEY EVENT
    key = pygame.key.get_pressed()

    if key[pygame.K_UP] == True:
        playerOne.body.move_ip(0, -1*speed)
    elif key[pygame.K_DOWN] == True:
        playerOne.body.move_ip(0, 1*speed)
    elif key[pygame.K_LEFT] == True:
        playerOne.body.move_ip(-1*speed, 0)
    elif key[pygame.K_RIGHT] == True:
        playerOne.body.move_ip(1*speed, 0)
    
    #GAME EVENTS   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
