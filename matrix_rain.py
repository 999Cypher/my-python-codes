import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Get screen info and set fullscreen
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Matrix Rain Effect")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Font setup
font_size = 20
font = pygame.font.SysFont('monospace', font_size)

# Rain drops: each drop is a tuple (x, y, speed, char)
drops = []
for i in range(WIDTH // font_size):
    x = i * font_size
    y = random.randint(-HEIGHT, 0)
    speed = random.randint(1, 5)
    char = chr(random.randint(33, 126))  # printable ASCII characters
    drops.append((x, y, speed, char))

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Update and draw each drop
    for i, (x, y, speed, char) in enumerate(drops):
        # Update drop position
        y += speed
        if y > HEIGHT:
            y = random.randint(-HEIGHT, 0)
            char = chr(random.randint(33, 126))
        drops[i] = (x, y, speed, char)

        # 3D effect: scale x-coordinate based on y-coordinate
        scale = 1 + (y / HEIGHT) * 0.5
        x_3d = x * scale

        # Draw the character
        text = font.render(char, True, GREEN)
        screen.blit(text, (x_3d, y))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit() 