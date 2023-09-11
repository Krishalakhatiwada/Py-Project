import pygame
import sys,math

# Initialize Pygame
pygame.init()

# Set up the window
DISPLAYSURF = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving a Circle with Mouse Cursor")

# Set up the circle
radius = 50
x = 320
y = 240
speed = 5

#Set up colors
#colors 
WHITE = (255,255,255)
RED = (255,0,0)



# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the circle according to the mouse cursor
    mouse_pos = pygame.mouse.get_pos()
    target_x, target_y = mouse_pos
    dx = target_x - x
    dy = target_y - y
    distance = math.sqrt(dx**2 + dy**2)
    if distance != 0:
        x += dx / distance * speed
        y += dy / distance * speed

    # Draw the circle
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF,RED, (int(x), int(y)), radius)
    pygame.time.wait(100)
    pygame.display.flip()