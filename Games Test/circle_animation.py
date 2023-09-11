import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Animating a Circle in a Circular Path")

# Set up the circle
radius = 50
center_x = 320
center_y = 240
angle = 0
angular_speed = 0.03

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate the position of the circle on the circular path
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    # Increment the angle to move the circle along the circular path
    angle += angular_speed

    # Draw the circle
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)
    pygame.display.flip()