import sys
import pygame


# The binary universe
black = 0, 0, 0
white = 255, 255, 255
UNIVERSE_SIZE = 64

# A window into the universe
size = width, height = UNIVERSE_SIZE*10, UNIVERSE_SIZE*10
screen = pygame.display.set_mode(size)

# Genesis
universe = [[0]*UNIVERSE_SIZE]*UNIVERSE_SIZE
print(universe)

#for i in range(0, UNIVERSE_SIZE):
#    for j in range(0, UNIVERSE_SIZE):
#        if ((i % 2) == 0):
#            universe[i][j] = 1
universe[2][2] = 1
print(universe)

    
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    for i in range(0, UNIVERSE_SIZE):
        for j in range(0, UNIVERSE_SIZE):
            if (universe[i][j] == 1):
                rectangle1 = pygame.Rect(i*10, j*10, 10, 10)
                pygame.draw.rect(screen, white, rectangle1)
    pygame.display.update() 
       
