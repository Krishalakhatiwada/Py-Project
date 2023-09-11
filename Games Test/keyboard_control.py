import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
DISPLAYSURF = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving a Circle with Keyboard Arrows")

#colors 
WHITE = (255,255,255)
RED = (255,0,0)


# Set up the circle
radius = 20
x = 320
y = 240
speed = 2

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the circle according to keyboard arrows
    keys = pygame.key.get_pressed()

   

    if keys[pygame.K_LEFT]:
        x -= speed*0.2
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Draw the circle
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF,RED, (int(x), int(y)), radius)
    pygame.display.update()
