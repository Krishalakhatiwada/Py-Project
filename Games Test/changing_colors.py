import pygame,sys,random
from pygame.locals import *

pygame.init()

#set up the window
DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Channging colors randomly')


#set up the circle
RED = 0
GREEN = 0
BLUE = 0

#The game loop
while True:
    #handle the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    RED = random.randint(0, 255)
    GREEN = random.randint(0, 255)
    BLUE = random.randint(0, 255)
 
    DISPLAYSURF.fill((RED,GREEN,BLUE))
    pygame.time.wait(100)
    pygame.display.update()