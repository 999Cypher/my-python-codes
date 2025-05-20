import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Objects")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define player and object dimensions
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20
OBJECT_SIZE = 30

# Set up the player
player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = WINDOW_HEIGHT - PLAYER_HEIGHT - 10

# Set up the object
object_x = random.randint(OBJECT_SIZE, WINDOW_WIDTH - OBJECT_SIZE)
object_y = -OBJECT_SIZE
object_speed = 2

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - PLAYER_WIDTH:
        player_x += 5

    # Move the object
    object_y += object_speed

    # Check for object collision
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    object_rect = pygame.Rect(object_x, object_y, OBJECT_SIZE, OBJECT_SIZE)
    if player_rect.colliderect(object_rect):
        # Reset the object position
        object_x = random.randint(OBJECT_SIZE, WINDOW_WIDTH - OBJECT_SIZE)
        object_y = -OBJECT_SIZE

    # Clear the window
    window.fill(BLACK)

    # Draw the player
    pygame.draw.rect(window, WHITE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Draw the object
    pygame.draw.rect(window, GREEN, (object_x, object_y, OBJECT_SIZE, OBJECT_SIZE))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()