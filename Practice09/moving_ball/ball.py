
import pygame


class Ball:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.radius = 25
        self.speed = 20

    def move(self, direction, width, height):
        new_x = self.x
        new_y = self.y

        if direction == "UP":
            new_y -= self.speed
        elif direction == "DOWN":
            new_y += self.speed
        elif direction == "LEFT":
            new_x -= self.speed
        elif direction == "RIGHT":
            new_x += self.speed

        # Check screen boundaries
        if self.radius <= new_x <= width - self.radius:
            if self.radius <= new_y <= height - self.radius:
                self.x = new_x
                self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (self.x, self.y),
            self.radius
        )
