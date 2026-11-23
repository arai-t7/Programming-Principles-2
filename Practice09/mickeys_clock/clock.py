import pygame
import math


def draw_hand(screen, image, center, angle, length, hand_color):
    """
    Draw a clock hand with a Mickey glove.

    angle: rotation angle in degrees
    length: distance from clock center to glove
    """

    # Convert angle to radians
    radians = math.radians(angle)

    # Calculate the end position of the hand
    x = center[0] + math.sin(radians) * length
    y = center[1] - math.cos(radians) * length

    # Draw the arm
    pygame.draw.line(
        screen,
        hand_color,
        center,
        (int(x), int(y)),
        8
    )

    # Rotate the glove
    rotated_image = pygame.transform.rotate(image, -angle)

    # Place the glove at the end of the arm
    image_rect = rotated_image.get_rect(
        center=(int(x), int(y))
    )

    screen.blit(rotated_image, image_rect)

    # Draw the center of the clock
    pygame.draw.circle(screen, (30, 30, 30), center, 12)
    pygame.draw.circle(screen, (220, 30, 50), center, 6)