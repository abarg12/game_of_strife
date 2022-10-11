import sys
import pygame


size = width, height = 360, 360
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

    
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    rectangle1 = pygame.Rect(120, 120, 20, 20)
    pygame.draw.rect(screen, white, rectangle1)
    pygame.display.update() 
       
