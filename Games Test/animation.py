import pygame,sys
from pygame.locals import *

pygame.init()

#set up the window
DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Animating a Circle')


#set up the circle
radius = 50
x = 50
y = 200

speed = .5

#Set up the colors
WHITE = (255,255,255)
RED = (255,0,0)

#The game loop
while True:
    #handle the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Move the circle
    x += speed

    #Bounce the circle off the sides of the screen
    if x+radius > 640 or x-radius < 0:
        speed = - speed

    #Draw the circle
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF,RED,(x,y),radius)
    pygame.display.update()