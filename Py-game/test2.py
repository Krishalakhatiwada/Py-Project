import pygame
import sys
import random
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
HOLE_MOVE_INTERVAL = 5000  # 5000 milliseconds (5 seconds)
OBSTACLE_RADIUS = 15  # Define obstacle radius

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Your Game Name")

# Create a circle for the hole
hole_radius = 20
hole_color = WHITE
hole_pos = [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]
hole_last_move_time = pygame.time.get_ticks()  # Track the last hole movement time

# Create a ball
ball_radius = 20
ball_color = RED
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = 5

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
score = 0
highest_score = 0
level = 1
game_over = False

def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def display_highest_score():
    highest_score_text = font.render(f"Highest Score: {highest_score}", True, WHITE)
    screen.blit(highest_score_text, (10, 50))

def display_level():
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(level_text, (10, 90))

def level_complete():
    global level, score
    if level == 1 and score >= 50:
        level = 2
        score = 0
    elif level == 2 and score >= 100:
        level = 3
        score = 0
    else:
        score += 10
    hole_pos[0] = random.randint(50, WIDTH - 50)
    hole_pos[1] = random.randint(50, HEIGHT - 50)
    ball_pos[0] = WIDTH // 2
    ball_pos[1] = HEIGHT // 2

def game_over_screen():
    screen.fill(BLACK)
    game_over_text = font.render("Game Over!", True, WHITE)
    restart_text = font.render("Press 'R' to Play Again or 'Q' to Quit", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(restart_text, (WIDTH // 2 - 200, HEIGHT // 2 + 20))

def check_collision_with_obstacles(obstacles):
    global game_over
    for obstacle in obstacles:
        distance = math.sqrt((obstacle[0] - ball_pos[0]) ** 2 + (obstacle[1] - ball_pos[1]) ** 2)
        if distance < OBSTACLE_RADIUS + ball_radius:
            game_over = True

def generate_obstacles(num_obstacles):
    obstacles = []
    for _ in range(num_obstacles):
        obstacle_x = random.randint(50, WIDTH - 50)
        obstacle_y = random.randint(50, HEIGHT - 50)
        obstacles.append((obstacle_x, obstacle_y))
    return obstacles

obstacles = generate_obstacles(5)  # Initial number of obstacles

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_over:
        if keys[pygame.K_r]:
            game_over = False
            level = 1
            score = 0
            ball_pos[0] = WIDTH // 2
            ball_pos[1] = HEIGHT // 2
            num_obstacles = 5 + (level - 1) * 3  # Reset obstacles for level 1
            obstacles = generate_obstacles(num_obstacles)
        elif keys[pygame.K_q]:
            running = False
    else:
        # Keyboard Controls
        if keys[pygame.K_LEFT] and ball_pos[0] != 20:
            ball_pos[0] -= ball_speed
        if keys[pygame.K_RIGHT] and ball_pos[0] != (WIDTH-20):
            ball_pos[0] += ball_speed
        if keys[pygame.K_UP] and ball_pos[1] != 20:
            ball_pos[1] -= ball_speed
        if keys[pygame.K_DOWN] and ball_pos[1] != (HEIGHT-20):
            ball_pos[1] += ball_speed

        # Check for collision with hole
        distance = math.sqrt((hole_pos[0] - ball_pos[0]) ** 2 + (hole_pos[1] - ball_pos[1]) ** 2)
        if distance < hole_radius + ball_radius:
            level_complete()

        # Check for collision with obstacles
        check_collision_with_obstacles(obstacles)

        # Check if it's time to move the hole
        current_time = pygame.time.get_ticks()
        if current_time - hole_last_move_time >= HOLE_MOVE_INTERVAL:
            hole_pos[0] = random.randint(50, WIDTH - 50)
            hole_pos[1] = random.randint(50, HEIGHT - 50)
            hole_last_move_time = current_time

        # Update display
        screen.fill(BLACK)
        pygame.draw.circle(screen, hole_color, (int(hole_pos[0]), int(hole_pos[1])), hole_radius)
        pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
        for obstacle in obstacles:
            pygame.draw.circle(screen, YELLOW, (obstacle[0], obstacle[1]), OBSTACLE_RADIUS)
        display_score()
        display_highest_score()
        display_level()

    if game_over:
        game_over_screen()

    pygame.display.flip()

    clock.tick(FPS)

    # Update highest score
    if score > highest_score:
        highest_score = score

    # Increase the number of obstacles with each level
    num_obstacles = 5 + (level - 1) * 3

pygame.quit()
sys.exit()
