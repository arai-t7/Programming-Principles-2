
import pygame
from pathlib import Path
from mutagen import File


class MusicPlayer:
    def __init__(self):
        self.music_folder = Path(__file__).parent / "music"
        self.playlist = []
        self.current_index = 0
        self.load_playlist()

    def load_playlist(self):
        self.playlist = sorted(
            [
                file for file in self.music_folder.rglob("*")
                if file.suffix.lower() in [".mp3", ".wav", ".ogg"]
            ],
            key=lambda file: file.name.lower()
        )

    def get_current_track(self):
        if not self.playlist:
            return None
        return self.playlist[self.current_index]

    def get_track_name(self):
        track = self.get_current_track()
        return track.stem if track else "No music found"

    def get_duration(self):
        track = self.get_current_track()

        if track is None:
            return 0

        try:
            audio = File(track)
            if audio is not None and audio.info:
                return audio.info.length
        except Exception:
            pass

        return 0

    def play(self):
        track = self.get_current_track()

        if track is None:
            return

        pygame.mixer.music.load(str(track))
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if not self.playlist:
            return

        self.current_index = (
            self.current_index + 1
        ) % len(self.playlist)

        self.play()

    def previous_track(self):
        if not self.playlist:
            return

        self.current_index = (
            self.current_index - 1
        ) % len(self.playlist)

        self.play()

    def get_progress(self):
        if not pygame.mixer.music.get_busy():
            return 0

        position = pygame.mixer.music.get_pos()

        if position < 0:
            return 0

        return position / 1000

    def update(self):
        if self.playlist and not pygame.mixer.music.get_busy():
            # Do not automatically restart after stopping.
            return
