import pygame,sys
from pygame.locals import *

pygame.init()

#set up the window
DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Drawing')


#set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (255,128,0)

#draw on the surface object
DISPLAYSURF.fill(WHITE)

#Draw polygon
#pygame.draw.polygon(DISPLAYSURF,GREEN,[(146,0),(291,106),(236,277),(56,277),(0,106)],5)
#Drawing lines
#pygame.draw.line(DISPLAYSURF,BLUE,(60,60),(120,60),4)

#Drawing a circle
#pygame.draw.circle(DISPLAYSURF,RED,(30,50),20,0)

#Drawing another circle
#pygame.draw.circle(DISPLAYSURF,ORANGE,(100,200),50,10)

#Drawing ellipse
#pygame.draw.ellipse(DISPLAYSURF,GREEN,(20,20,200,200),1)
#pygame.draw.ellipse(DISPLAYSURF,GREEN,(220,10,250,30))

#Drawing rectangle
pygame.draw.rect(DISPLAYSURF,RED,(200,150,100,50))

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()