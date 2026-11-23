import pygame
import os
from datetime import datetime
from clock import draw_hand
import math

# Initialize Pygame
pygame.init()

# Window settings
WIDTH = 700
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")

# Colors
WHITE = (255, 255, 255)
BLACK = (25, 25, 25)
BEIGE = (230, 220, 190)
RED = (220, 30, 50)

# Clock settings
center = (WIDTH // 2, HEIGHT // 2)
radius = 280

# Load images
image_folder = os.path.join(os.path.dirname(__file__), "images")

left_hand = pygame.image.load(
    os.path.join(image_folder, "mickey_left_hand.png")
).convert_alpha()

right_hand = pygame.image.load(
    os.path.join(image_folder, "mickey_right_hand.png")
).convert_alpha()

# Resize images
left_hand = pygame.transform.smoothscale(left_hand, (65, 65))
right_hand = pygame.transform.smoothscale(right_hand, (55, 80))

# Font
font = pygame.font.SysFont("Arial", 36)

# Game loop
running = True
fps = pygame.time.Clock()

while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current system time
    now = datetime.now()

    minutes = now.minute
    seconds = now.second

    # Calculate angles
    minute_angle = (minutes + seconds / 60) * 6
    second_angle = seconds * 6

    # Draw background
    screen.fill(WHITE)

    # Draw clock face
    pygame.draw.circle(screen, BLACK, center, radius + 8)
    pygame.draw.circle(screen, BEIGE, center, radius)

    # Draw clock marks
    for i in range(60):
        angle = i * 6
        radians = math.radians(angle)

        outer_x = center[0] + math.sin(radians) * (radius - 10)
        outer_y = center[1] - math.cos(radians) * (radius - 10)

        if i % 5 == 0:
            inner_radius = radius - 35
            width = 5
        else:
            inner_radius = radius - 20
            width = 2

        inner_x = center[0] + math.sin(radians) * inner_radius
        inner_y = center[1] - math.cos(radians) * inner_radius

        pygame.draw.line(
            screen,
            BLACK,
            (int(inner_x), int(inner_y)),
            (int(outer_x), int(outer_y)),
            width
        )

    # Draw numbers
    for number in range(1, 13):
        angle = number * 30
        radians = math.radians(angle)

        x = center[0] + math.sin(radians) * 220
        y = center[1] - math.cos(radians) * 220

        text = font.render(str(number), True, BLACK)
        text_rect = text.get_rect(center=(int(x), int(y)))
        screen.blit(text, text_rect)

    # Draw Mickey's hands
    draw_hand(
        screen,
        right_hand,
        center,
        minute_angle,
        150,
        BLACK
    )

    draw_hand(
        screen,
        left_hand,
        center,
        second_angle,
        210,
        RED
    )

    # Display minutes and seconds
    time_text = f"{minutes:02d}:{seconds:02d}"
    digital_time = font.render(time_text, True, RED)

    screen.blit(
        digital_time,
        digital_time.get_rect(center=(center[0], 420))
    )

    # Update display
    pygame.display.flip()

    fps.tick(30)

# Close Pygame
pygame.quit()