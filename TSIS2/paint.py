
import pygame
import sys
import os
from datetime import datetime

pygame.init()

# Window settings
WIDTH = 1100
HEIGHT = 750
TOOLBAR_HEIGHT = 200
CANVAS_HEIGHT = HEIGHT - TOOLBAR_HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Paint Application")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
BLUE = (0, 100, 255)

COLORS = [
    BLACK,
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (128, 0, 128),
    WHITE
]

# Canvas
canvas = pygame.Surface((WIDTH, CANVAS_HEIGHT))
canvas.fill(WHITE)

# Drawing settings
current_color = BLACK
brush_size = 5
current_tool = "pencil"

drawing = False
last_pos = None
start_pos = None

# Text settings
text_input = ""
typing_text = False
text_position = None

font = pygame.font.SysFont("Arial", 20)
toolbar_font = pygame.font.SysFont("Arial", 16)

# Tools
tools = [
    ("Pencil", "pencil"),
    ("Line", "line"),
    ("Rectangle", "rectangle"),
    ("Circle", "circle"),
    ("Square", "square"),
    ("Right Triangle", "right_triangle"),
    ("Equilateral Triangle", "equilateral_triangle"),
    ("Rhombus", "rhombus"),
    ("Eraser", "eraser"),
    ("Flood Fill", "fill"),
    ("Text", "text")
]

buttons = []

for i, (name, tool) in enumerate(tools):
    x = 15 + (i % 4) * 160
    y = 65 + (i // 4) * 40

    button = pygame.Rect(x, y, 145, 30)
    buttons.append((button, name, tool))

# Color buttons
color_buttons = []

for i, color in enumerate(COLORS):
    rect = pygame.Rect(700 + i * 40, 15, 30, 30)
    color_buttons.append((rect, color))


# Flood Fill
def flood_fill(surface, start_pos, fill_color):

    x, y = start_pos
    width, height = surface.get_size()

    if x < 0 or x >= width or y < 0 or y >= height:
        return

    target_color = surface.get_at((x, y))[:3]

    if target_color == fill_color:
        return

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        if surface.get_at((x, y))[:3] != target_color:
            continue

        surface.set_at((x, y), fill_color)

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))


# Save drawing
def save_drawing():

    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"painting_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    pygame.image.save(canvas, filepath)

    print(f"Drawing saved: {filepath}")


clock = pygame.time.Clock()

# Main loop
running = True

while running:

    mouse_pos = pygame.mouse.get_pos()

    canvas_mouse_pos = (
        mouse_pos[0],
        mouse_pos[1] - TOOLBAR_HEIGHT
    )

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:

            if typing_text:

                if event.key == pygame.K_RETURN:

                    if text_input:
                        text_surface = font.render(
                            text_input, True, current_color
                        )
                        canvas.blit(text_surface, text_position)

                    text_input = ""
                    typing_text = False
                    text_position = None

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                elif event.key == pygame.K_ESCAPE:
                    text_input = ""
                    typing_text = False
                    text_position = None

                elif event.unicode.isprintable():
                    text_input += event.unicode

            else:

                # Save with Ctrl + S
                if (event.key == pygame.K_s and
                        pygame.key.get_mods() & pygame.KMOD_CTRL):
                    save_drawing()

                elif event.key == pygame.K_1:
                    brush_size = 3

                elif event.key == pygame.K_2:
                    brush_size = 7

                elif event.key == pygame.K_3:
                    brush_size = 12

        # Mouse pressed
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1 and not typing_text:

                # Select tool
                for rect, name, tool in buttons:
                    if rect.collidepoint(mouse_pos):
                        current_tool = tool

                # Select color
                for rect, color in color_buttons:
                    if rect.collidepoint(mouse_pos):
                        current_color = color

                # Canvas actions
                if mouse_pos[1] >= TOOLBAR_HEIGHT:

                    if current_tool == "fill":

                        flood_fill(
                            canvas,
                            canvas_mouse_pos,
                            current_color
                        )

                    elif current_tool == "text":

                        text_position = canvas_mouse_pos
                        text_input = ""
                        typing_text = True

                    else:

                        drawing = True
                        last_pos = canvas_mouse_pos
                        start_pos = canvas_mouse_pos

        # Mouse released
        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1 and drawing:

                end_pos = canvas_mouse_pos

                if current_tool == "line":

                    pygame.draw.line(
                        canvas, current_color,
                        start_pos, end_pos, brush_size
                    )

                elif current_tool == "rectangle":

                    rect = pygame.Rect(
                        min(start_pos[0], end_pos[0]),
                        min(start_pos[1], end_pos[1]),
                        abs(end_pos[0] - start_pos[0]),
                        abs(end_pos[1] - start_pos[1])
                    )

                    pygame.draw.rect(
                        canvas, current_color, rect, brush_size
                    )

                elif current_tool == "circle":

                    radius = int(
                        ((end_pos[0] - start_pos[0]) ** 2 +
                         (end_pos[1] - start_pos[1]) ** 2) ** 0.5
                    )

                    pygame.draw.circle(
                        canvas, current_color,
                        start_pos, radius, brush_size
                    )

                elif current_tool == "square":

                    side = max(
                        abs(end_pos[0] - start_pos[0]),
                        abs(end_pos[1] - start_pos[1])
                    )

                    rect = pygame.Rect(
                        start_pos[0], start_pos[1], side, side
                    )

                    pygame.draw.rect(
                        canvas, current_color, rect, brush_size
                    )

                elif current_tool == "right_triangle":

                    points = [
                        start_pos,
                        (end_pos[0], start_pos[1]),
                        end_pos
                    ]

                    pygame.draw.polygon(
                        canvas, current_color, points, brush_size
                    )

                elif current_tool == "equilateral_triangle":

                    dx = end_pos[0] - start_pos[0]
                    height = int(abs(dx) * 0.866)

                    points = [
                        start_pos,
                        end_pos,
                        (start_pos[0] + dx // 2,
                         start_pos[1] - height)
                    ]

                    pygame.draw.polygon(
                        canvas, current_color, points, brush_size
                    )

                elif current_tool == "rhombus":

                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]

                    points = [
                        (start_pos[0] + dx // 2, start_pos[1]),
                        (end_pos[0], start_pos[1] + dy // 2),
                        (start_pos[0] + dx // 2, end_pos[1]),
                        (start_pos[0], start_pos[1] + dy // 2)
                    ]

                    pygame.draw.polygon(
                        canvas, current_color, points, brush_size
                    )

                drawing = False
                last_pos = None
                start_pos = None

    # Continuous drawing
    if drawing and pygame.mouse.get_pressed()[0]:

        if mouse_pos[1] >= TOOLBAR_HEIGHT:

            if current_tool == "pencil":

                pygame.draw.line(
                    canvas, current_color,
                    last_pos, canvas_mouse_pos, brush_size
                )

            elif current_tool == "eraser":

                pygame.draw.line(
                    canvas, WHITE,
                    last_pos, canvas_mouse_pos,
                    brush_size * 3
                )

            last_pos = canvas_mouse_pos

    # Draw toolbar
    screen.fill(LIGHT_GRAY)

    title = toolbar_font.render(
        "MY PAINT APPLICATION", True, BLACK
    )
    screen.blit(title, (15, 15))

    # Color palette
    for rect, color in color_buttons:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

    # Tool buttons
    for rect, name, tool in buttons:

        if current_tool == tool:
            button_color = BLUE
            text_color = WHITE
        else:
            button_color = GRAY
            text_color = BLACK

        pygame.draw.rect(screen, button_color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

        text = toolbar_font.render(name, True, text_color)
        screen.blit(text, (rect.x + 10, rect.y + 7))

    # Brush size
    size_text = toolbar_font.render(
        f"Brush size: {brush_size} (Press 1, 2, 3)",
        True, BLACK
    )
    screen.blit(size_text, (700, 65))

    # Selected tool
    tool_text = toolbar_font.render(
        f"Selected tool: {current_tool}",
        True, BLACK
    )
    screen.blit(tool_text, (700, 100))

    # Text instructions
    if typing_text:
        instruction = toolbar_font.render(
            "Type text and press ENTER (ESC to cancel)",
            True, BLUE
        )
        screen.blit(instruction, (700, 135))

    # Canvas
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    # Text preview
    if typing_text and text_input:

        preview = font.render(text_input, True, current_color)

        screen.blit(
            preview,
            (text_position[0],
             text_position[1] + TOOLBAR_HEIGHT)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
