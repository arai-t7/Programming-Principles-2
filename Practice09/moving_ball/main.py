
import pygame
from ball import Ball

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

# Create ball
ball = Ball()

# FPS controller
clock = pygame.time.Clock()

running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move("UP", WIDTH, HEIGHT)
            elif event.key == pygame.K_DOWN:
                ball.move("DOWN", WIDTH, HEIGHT)
            elif event.key == pygame.K_LEFT:
                ball.move("LEFT", WIDTH, HEIGHT)
            elif event.key == pygame.K_RIGHT:
                ball.move("RIGHT", WIDTH, HEIGHT)

    # White background
    screen.fill((255, 255, 255))

    # Draw ball
    ball.draw(screen)

    # Update display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
