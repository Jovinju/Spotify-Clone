"""Implements playing tracks"""

import io
import pygame

from mutagen.mp3 import MP3
from PIL import Image
from linked_list import LinkedList, LinkedListItem



class Composition:
    """Class of keeping info about song"""

    def __init__(self, path) -> None:
        self.path = path
        self.metadata = self.__get_metadata()

    def __get_metadata(self) -> dict:
        metadata = {
            "title": 'Unknown',
            "artist": 'Unknown',
            "length": None,
            "picture": None,
        }

        audio = MP3(self.path)

        if "TIT2" in audio:
            metadata["title"] = str(audio.get("TIT2"))
        if "TPE1" in audio:
            metadata["artist"] = str(audio.get("TPE1"))
        metadata["length"] = round(audio.info.length)

        for key in audio.keys():
            if key.startswith("APIC:"):
                b_picture = audio.get(key).data
                picture = Image.open(io.BytesIO(b_picture))
                metadata["picture"] = picture
        return metadata

class PlayList(LinkedList):
    """
    Implements song playback using a data structure - ring double linked list

    Args:
        LinkedList (_type_): Ring double linked list
    """

    def __init__(self) -> None:
        super().__init__()
        pygame.mixer.init()
        self.current_playing_item = None
        self.is_paused = None

    def play_all(self, playlist_item: LinkedListItem) -> None:
        """ Starts playing all track from playlist_item

        Args:
            playlist_item (LinkedListItem): an LinkedListItem object
        """

        pygame.mixer.music.load(playlist_item.data.path)
        pygame.mixer.music.play()
        self.current_playing_item = playlist_item
        self.is_paused = False

    def pause(self) -> None:
        """Pauses current playing track"""

        pygame.mixer.music.pause()
        self.is_paused = True

    def unpause(self) -> None:
        """Unpauses current playing track"""

        pygame.mixer.music.unpause()
        self.is_paused = False

    def stop(self) -> None:
        """Stops playing track"""

        pygame.mixer.music.stop()
        self.current_playing_item = None
        self.is_paused = None

    def next_track(self) -> None:
        """Starts playing a next track"""

        pygame.mixer.music.stop()
        self.play_all(self.current_playing_item.next_item)

    def previous_track(self) -> None:
        """Starts playing a previous track"""

        pygame.mixer.music.stop()
        self.play_all(self.current_playing_item.prev_item)

    def set_volume(self, value: float) -> None:
        """ Sets a new value of music volume"""

        pygame.mixer.music.set_volume(value)

    def get_pos(self) -> int:
        """Returns time of playing current track in sec"""

        return pygame.mixer.music.get_pos() // 1000

    def set_pos(self, value: int):
        """ Sets a new time from which the track continues to play"""

        pygame.mixer.music.set_pos(value)

    def get_busy(self) -> bool:
        """
        Returns a boolean value whether the music is currently playing or not
        """

        return pygame.mixer.music.get_busy()
