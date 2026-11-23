
import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pink Music Player")

clock = pygame.time.Clock()

PINK_BG = (255, 225, 235)
PINK = (255, 105, 150)
DARK_PINK = (230, 70, 125)
WHITE = (255, 255, 255)
TEXT = (90, 55, 70)
LIGHT_PINK = (255, 190, 210)

title_font = pygame.font.SysFont("Arial", 34, bold=True)
font = pygame.font.SysFont("Arial", 21)
small_font = pygame.font.SysFont("Arial", 16)

player = MusicPlayer()

running = True
message = ""

def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def format_time(seconds):
    minutes = int(seconds) // 60
    seconds = int(seconds) % 60
    return f"{minutes:02}:{seconds:02}"


def draw_button(text, rect):
    pygame.draw.rect(
        screen, PINK, rect, border_radius=15
    )

    label = font.render(text, True, WHITE)

    screen.blit(
        label,
        (
            rect.centerx - label.get_width() // 2,
            rect.centery - label.get_height() // 2
        )
    )


buttons = {
    "PREVIOUS": pygame.Rect(105, 325, 140, 45),
    "PLAY": pygame.Rect(280, 325, 140, 45),
    "NEXT": pygame.Rect(455, 325, 140, 45),
    "STOP": pygame.Rect(280, 385, 140, 40)
}


while running:
    screen.fill(PINK_BG)

    pygame.draw.rect(
        screen,
        WHITE,
        (50, 35, 600, 475),
        border_radius=25
    )

    draw_text(
        "Pink Music Player",
        title_font,
        DARK_PINK,
        190,
        55
    )

    draw_text(
        "NOW PLAYING",
        small_font,
        PINK,
        285,
        120
    )

    draw_text(
        player.get_track_name(),
        font,
        TEXT,
        250,
        150
    )

    duration = player.get_duration()
    position = player.get_progress()

    # Playback progress bar
    bar_x = 110
    bar_y = 235
    bar_width = 480

    pygame.draw.rect(
        screen,
        LIGHT_PINK,
        (bar_x, bar_y, bar_width, 10),
        border_radius=5
    )

    if duration > 0:
        progress = min(position / duration, 1)

        pygame.draw.rect(
            screen,
            PINK,
            (bar_x, bar_y, int(bar_width * progress), 10),
            border_radius=5
        )

    draw_text(
        format_time(position),
        small_font,
        TEXT,
        110,
        255
    )

    draw_text(
        format_time(duration),
        small_font,
        TEXT,
        550,
        255
    )

    # Playlist
    draw_text(
        "PLAYLIST",
        font,
        DARK_PINK,
        110,
        290
    )

    if player.playlist:
        for i, track in enumerate(player.playlist[:3]):
            color = DARK_PINK if i == player.current_index else TEXT

            draw_text(
                track.name,
                small_font,
                color,
                230,
                290 + i * 20
            )
    else:
        draw_text(
            "No music files found",
            small_font,
            TEXT,
            230,
            290
        )

    for name, rect in buttons.items():
        draw_button(name, rect)

    draw_text(
        "P - Play | S - Stop | N - Next | B - Previous | Q - Quit",
        small_font,
        TEXT,
        85,
        455
    )

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.previous_track()

            elif event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if buttons["PLAY"].collidepoint(event.pos):
                player.play()

            elif buttons["STOP"].collidepoint(event.pos):
                player.stop()

            elif buttons["NEXT"].collidepoint(event.pos):
                player.next_track()

            elif buttons["PREVIOUS"].collidepoint(event.pos):
                player.previous_track()


    clock.tick(30)


pygame.mixer.music.stop()
pygame.quit()
