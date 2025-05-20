import sys
import random
import time
import pygame

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
NUMBER_OF_LOGOS = 5  # (!) Try changing this to 1 or 100.
PAUSE_AMOUNT = 0.05  # (!) Try changing this to 1.0 or 0.0.
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
LOGO_TEXTS = ['DVD', '☺', '✨', '⚽', '💻', '🎵', '🌺', '🚀']  # Add more logo texts as desired

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'
TEXT = 'text'
TRAIL = 'trail'  # New key for trail

# Initialize Pygame
pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Bouncing Logos')
FONT = pygame.font.Font(None, 72)
CLOCK = pygame.time.Clock()

def main():
    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({
            COLOR: random.choice(COLORS),
            X: random.randint(50, WINDOW_WIDTH - 100),
            Y: random.randint(50, WINDOW_HEIGHT - 100),
            DIR: random.choice(DIRECTIONS),
            TEXT: random.choice(LOGO_TEXTS),
            TRAIL: []  # Initialize an empty list for the trail
        })

    cornerBounces = 0  # Count how many times a logo hits a corner.
    while True:  # Main program loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WINDOW.fill((0, 0, 0))  # Clear the window

        for logo in logos:  # Handle each logo in the logos list.
            originalDirection = logo[DIR]

            # See if the logo bounces off the corners:
            if logo[X] <= 50 and logo[Y] <= 50:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] <= 50 and logo[Y] >= WINDOW_HEIGHT - 100:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] >= WINDOW_WIDTH - 100 and logo[Y] <= 50:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] >= WINDOW_WIDTH - 100 and logo[Y] >= WINDOW_HEIGHT - 100:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # See if the logo bounces off the left edge:
            elif logo[X] <= 50 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] <= 50 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the right edge:
            elif logo[X] >= WINDOW_WIDTH - 100 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] >= WINDOW_WIDTH - 100 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # See if the logo bounces off the top edge:
            elif logo[Y] <= 50 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] <= 50 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the bottom edge:
            elif logo[Y] >= WINDOW_HEIGHT - 100 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] >= WINDOW_HEIGHT - 100 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # Change color and text when the logo bounces:
                logo[COLOR] = random.choice(COLORS)
                logo[TEXT] = random.choice(LOGO_TEXTS)

            # Move the logo. (X moves by 2 because the terminal
            # characters are twice as tall as they are wide.)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 2
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 2
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 2
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 2

            # Add the current position to the trail
            logo[TRAIL].append((logo[X], logo[Y]))

            # Limit the trail length to 20
            logo[TRAIL] = logo[TRAIL][-20:]

        # Draw the logos and trails
        for logo in logos:
            # Draw the logo
            text_surface = FONT.render(logo[TEXT], True, pygame.Color(logo[COLOR]))
            text_rect = text_surface.get_rect()
            text_rect.centerx = logo[X]
            text_rect.centery = logo[Y]
            WINDOW.blit(text_surface, text_rect)

            # Draw the trail
            for x, y in logo[TRAIL]:
                pygame.draw.circle(WINDOW, (128, 128, 128), (x, y), 5)

        # Display number of corner bounces
        text_surface = FONT.render(f'Corner bounces: {cornerBounces}', True, (255, 255, 255))
        WINDOW.blit(text_surface, (10, 10))

        pygame.display.update()
        CLOCK.tick(60)  # Cap the frame rate at 60 FPS

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        pygame.quit()
        sys.exit()  # When Ctrl-C is pressed, end the program.