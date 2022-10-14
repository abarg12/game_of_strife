import sys
import pygame

pygame.init()
pygame.font.init()

# The binary universe
black = 0, 0, 0
white = 255, 255, 255
green = 40, 255, 80
UNIVERSE_SIZE = 64

# A window into the universe
size = width, height = UNIVERSE_SIZE*10, UNIVERSE_SIZE*10
screen = pygame.display.set_mode(size)

# Initial game message
screen.fill(white)
pygame.display.set_caption('Game of Strife')
font = pygame.font.SysFont("Arial", 24)
text = font.render('Click on screen to spawn life, then press enter to begin the simulation', True, white, black)
textRect = text.get_rect()
textRect.center = (size[0] // 2, size[1] // 3)
screen.blit(text, textRect)
pygame.display.update()


# Universal laws
def update_universe():
    calculate_neighbors()
    for i in range(UNIVERSE_SIZE):
        for j in range(UNIVERSE_SIZE):
            if (universe_popgrid[i][j] < 2):
                # underpopulation death
                universe[i][j] = 0
            elif (universe_popgrid[i][j] > 3):
                # overpopulation death
                universe[i][j] = 0
            elif (universe_popgrid[i][j] == 3):
                universe[i][j] = 1
            
def calculate_neighbors():
    for k in range(UNIVERSE_SIZE): 
        for l in range(UNIVERSE_SIZE):
            universe_popgrid[k][l] = 0
    
    for i in range(UNIVERSE_SIZE):
        for j in range(UNIVERSE_SIZE):
            if universe[i][j] == 1:
                increment_neighbors_normal(i, j)
            if universe[i][j] == 2:
                increment_neighbors_swarm(i, j)
                
def increment_neighbors_normal(i, j):
   for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if (i == k and j == l):
                continue 
            elif (k < 0 or k >= universe_size):
                continue 
            elif (l < 0 or l >= universe_size):
                continue 
            else:
                universe_popgrid[k][l] += 1

def increment_neighbors_swarm(i, j):
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if (i == k and j == l):
                continue 
            elif (k < 0 or k >= universe_size):
                continue 
            elif (l < 0 or l >= universe_size):
                continue 
            else:
                universe_popgrid_swarm[k][l] += 1




BC = True  # before click
while BC:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: BC = False
        if event.type == pygame.MOUSEBUTTONDOWN: BC = False


# Genesis
universe = [[0]*UNIVERSE_SIZE for i in range(UNIVERSE_SIZE)]
universe_popgrid = [[0]*UNIVERSE_SIZE for i in range(UNIVERSE_SIZE)]
universe_swarm_popgrid = [[0]*UNIVERSE_SIZE for i in range(UNIVERSE_SIZE)]
screen.fill(black)

BC = True 
while BC:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                # the power to create life
                universe[int(pos[0] / 10)][int(pos[1] / 10)] = 1
            if event.button == 2:
                # the power to create chaos
                universe[int(pos[0] / 10)][int(pos[1] / 10)] = 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                BC = False
    
    for i in range(UNIVERSE_SIZE):
        for j in range(UNIVERSE_SIZE):
            if (universe[i][j] == 1):
                rectangle1 = pygame.Rect(i*10, j*10, 10, 10)
                pygame.draw.rect(screen, white, rectangle1)
            if (universe[i][j] == 2):
                rectangle2 = pygame.Rect(i*10, j*10, 10, 10)
                pygame.draw.rect(screen, green, rectangle2)
    pygame.display.update() 
       

# update universe every half-second
UNIVERSE_TICK = pygame.USEREVENT + 1
pygame.time.set_timer(UNIVERSE_TICK, 500)


E = True  # while universe exists
while E:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                sys.exit()
        if event.type == UNIVERSE_TICK:
            update_universe()
            screen.fill(black)
            for i in range(UNIVERSE_SIZE):
                for j in range(UNIVERSE_SIZE):
                    if (universe[i][j] == 1):
                        rectangle1 = pygame.Rect(i*10, j*10, 10, 10)
                        pygame.draw.rect(screen, white, rectangle1)
            pygame.display.update()

