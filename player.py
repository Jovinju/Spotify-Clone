"""Player logic"""

from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QFileDialog

from ui_player import Ui_MainWindow
from playlist import PlayList, Composition

class Player(QMainWindow, Ui_MainWindow):
    """Implementaion of player logic"""

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.current_playlist = None
        self.current_playing_playlist = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_slider)
        self.start_slider_position = 0

        self.add_playlist_button.clicked.connect(self.add_playlist)
        self.remove_playlist_button.clicked.connect(self.remove_playlist)

        update_music_frame = self.update_music_frame
        self.playlist_widget.currentItemChanged.connect(update_music_frame)

        self.add_track_button.clicked.connect(self.add_track)
        self.remove_track_button.clicked.connect(self.remove_track)

        self.play_playlist_button.clicked.connect(self.play_playlist_music)
        self.play_pause_button.clicked.connect(self.play_pause)

        self.next_button.clicked.connect(self.play_next)
        self.previous_button.clicked.connect(self.play_previous)

        self.main_slider.sliderReleased.connect(self.set_position)
        self.main_slider.sliderPressed.connect(self.timer.stop)

        self.volume_slider.valueChanged.connect(self.set_volume)

    def add_playlist(self):
        """
        Adds new item to playlist_widget
        and assigns Playlist object to this item
        """

        if self.playlist_widget.count() == 8:
            return
        if self.playlist_widget.count() == 0:
            self.remove_playlist_button.setEnabled(True)

        name = f"Мой плейлист №{self.playlist_widget.count() + 1}"
        new_item = QListWidgetItem(name)
        new_item.playlist = PlayList()
        self.playlist_widget.addItem(new_item)
        self.playlist_widget.setCurrentItem(new_item)

    def remove_playlist(self):
        """Removes playlist from playlist_widget"""

        if self.current_playlist == self.current_playing_playlist:
            self.current_playing_playlist.stop()
            self.timer.stop()

        current_row = self.playlist_widget.currentRow()
        self.playlist_widget.takeItem(current_row)

        if self.playlist_widget.count() == 0:
            self.remove_playlist_button.setEnabled(False)
            self.playlist_name.setText("Добавьте плейлист")
            self.current_playlist = None

    def add_track(self):
        """Adds track(s) to Playlist object"""

        file_paths = QFileDialog.getOpenFileNames(filter="*.mp3")[0]
        for file_path in file_paths:
            track = Composition(file_path)
            self.current_playlist.append(track)
        self.update_music_frame()

    def remove_track(self):
        """Removes selected track from Playlist object"""

        index = self.music_list_widget.currentRow()
        self.current_playlist.remove(self.current_playlist[index].data)
        self.update_music_frame()

    def update_music_frame(self):
        """Updates info about current playlist in music_frame"""

        self.music_list_widget.clear()

        if self.playlist_widget.currentItem() is None:
            self.play_playlist_button.setEnabled(False)
            self.remove_track_button.setEnabled(False)

            self.previous_button.setEnabled(False)
            self.play_pause_button.setEnabled(False)
            self.next_button.setEnabled(False)
            self.main_slider.setEnabled(False)

            self.add_track_button.setEnabled(False)
            self.current_playlist = None
            self.current_playing_playlist = None
            return

        self.current_playlist = self.playlist_widget.currentItem().playlist
        self.playlist_name.setText(self.playlist_widget.currentItem().text())

        if self.current_playlist.size == 0:
            self.add_track_button.setEnabled(True)
            self.remove_track_button.setEnabled(False)
            self.play_playlist_button.setEnabled(False)
            return

        if self.music_list_widget.count() == 0:
            self.play_playlist_button.setEnabled(True)
            self.remove_track_button.setEnabled(True)

        if self.current_playlist == self.current_playing_playlist:
            if self.current_playlist.is_paused:
                self.play_playlist_button.setChecked(False)
            else:
                self.play_playlist_button.setChecked(True)
        else:
            self.play_playlist_button.setChecked(False)


        for track_item in self.current_playlist:
            text = f"{track_item.data.metadata['artist']} - "\
                  + f"{track_item.data.metadata['title']}"
            music_item = QListWidgetItem(text)
            self.music_list_widget.addItem(music_item)

            if self.current_playlist == self.current_playing_playlist:
                if track_item == self.current_playlist.current_playing_item:
                    self.music_list_widget.setCurrentItem(music_item)
            else:
                if self.music_list_widget.currentItem() is None:
                    self.music_list_widget.setCurrentItem(music_item)

    def play_playlist_music(self):
        """Starts play music from selected track, can pause and play track"""

        if self.current_playing_playlist is not None\
            and self.current_playing_playlist != self.current_playlist:

            self.current_playing_playlist.current_playing_item = None
            self.current_playing_playlist = None

        if self.current_playing_playlist is None:
            self.current_playing_playlist = self.current_playlist
            self.play_pause_button.setChecked(True)

            self.previous_button.setEnabled(True)
            self.play_pause_button.setEnabled(True)
            self.next_button.setEnabled(True)
            self.main_slider.setEnabled(True)

        if self.current_playlist.current_playing_item is None:
            playlist = self.current_playlist
            index = self.music_list_widget.currentRow()
            playlist.set_volume(self.volume_slider.value() / 100)
            playlist.play_all(playlist[index])

            playing_item = playlist.current_playing_item
            track_length = playing_item.data.metadata["length"]
            self.main_slider.setMaximum(track_length)

            track_time = self.get_formatted_time(track_length)
            self.track_time_label.setText(track_time)

            self.timer.start(1000)

            self.update_music_info_frame()
            return

        if self.play_playlist_button.isChecked():
            self.play_pause_button.setChecked(True)
            self.current_playlist.unpause()
            self.timer.start(1000)
        else:
            self.play_pause_button.setChecked(False)
            self.current_playlist.pause()
            self.timer.stop()

    def play_pause(self):
        """Pauses and plays the track"""

        is_checked = self.play_pause_button.isChecked()
        if is_checked:
            self.current_playing_playlist.unpause()
            self.timer.start(1000)
        else:
            self.current_playing_playlist.pause()
            self.timer.stop()

        if self.current_playing_playlist == self.current_playlist:
            if is_checked:
                self.play_playlist_button.setChecked(True)
            else:
                self.play_playlist_button.setChecked(False)

    def play_next(self):
        """Plays the next track"""

        if self.current_playing_playlist.is_paused:
            self.current_playing_playlist.next_track()
            self.current_playing_playlist.pause()
            self.timer.stop()
        else:
            self.current_playing_playlist.next_track()

        playlist = self.current_playing_playlist
        track_length = playlist.current_playing_item.data.metadata["length"]

        self.current_time_label.setText(self.get_formatted_time(0))
        track_time = self.get_formatted_time(track_length)
        self.track_time_label.setText(track_time)

        self.main_slider.setMaximum(track_length)
        self.main_slider.setValue(0)
        self.start_slider_position = 0
        self.update_slider()

        self.update_music_frame()
        self.update_music_info_frame()

    def play_previous(self):
        """Plays the previous track"""

        if self.current_playing_playlist.is_paused:
            self.current_playing_playlist.previous_track()
            self.current_playing_playlist.pause()
            self.timer.stop()
        else:
            self.current_playing_playlist.previous_track()

        playlist = self.current_playing_playlist
        track_length = playlist.current_playing_item.data.metadata["length"]

        self.current_time_label.setText(self.get_formatted_time(0))
        track_time = self.get_formatted_time(track_length)
        self.track_time_label.setText(track_time)


        self.main_slider.setMaximum(track_length)
        self.main_slider.setValue(0)
        self.start_slider_position = 0
        self.update_slider()

        self.update_music_frame()
        self.update_music_info_frame()

    def update_slider(self):
        """
        Called by QTimer every 1 sec 
        Update value of slider and current time text
        """

        if self.current_playing_playlist.is_paused:
            return

        track_position = self.current_playing_playlist.get_pos()
        value = self.start_slider_position + track_position
        self.main_slider.setValue(value)


        if not self.current_playing_playlist.get_busy():
            self.play_next()
            return

        self.current_time_label.setText(self.get_formatted_time(value))

    def set_position(self):
        """
        Called when track slider is realised
        Plays the track from the position of slider
        """

        compensation = self.current_playing_playlist.get_pos()
        self.start_slider_position = self.main_slider.value() - compensation
        self.current_playing_playlist.set_pos(self.main_slider.value())

        track_position = self.get_formatted_time(self.main_slider.value())
        self.current_time_label.setText(track_position)

        self.update_slider()
        self.timer.start(1000)

    def update_music_info_frame(self):
        """Updates music info frame when current playing track is changed"""

        current_playlist = self.current_playing_playlist
        current_playlist_item = current_playlist.current_playing_item

        title_info = current_playlist_item.data.metadata["title"]
        self.current_title_info.setText(title_info)

        artist_info = current_playlist_item.data.metadata["artist"]
        self.current_artist_info.setText(artist_info)

        if current_playlist_item.data.metadata["picture"] is None:
            pixmap = QPixmap(":/resources/music.png")
        else:
            image = current_playlist_item.data.metadata["picture"]
            qimage = QImage(image.tobytes(), image.size[0], image.size[1],
                            QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(72, 72)
        self.current_photo.setPixmap(pixmap)

    def set_volume(self, value: int) -> None:
        """
        Called when volume slider value is changed
        Sets a new volume value

        Args:
            value (int): new volume value (0 - 100)
        """

        if 70 < value <= 100:
            self.volume_button.setIcon(QIcon(":/resources/volume-max.png"))
        elif 30 < value <= 70:
            self.volume_button.setIcon(QIcon(":/resources/volume-medium.png"))
        elif 0 < value <= 30:
            self.volume_button.setIcon(QIcon(":/resources/volume-low.png"))
        else:
            self.volume_button.setIcon(QIcon(":/resources/volume-zero.png"))

        if self.current_playing_playlist is None:
            return
        self.current_playing_playlist.set_volume(value / 100)

    def get_formatted_time(self, seconds: int) -> str:
        """ Converts seconds time to a formatted time like 0:00

        Args:
            seconds (int): seconds time

        Returns:
            str: formatted time
        """

        if seconds % 60 < 10:
            return f"{seconds // 60}:0{seconds % 60}"
        return f"{seconds // 60}:{seconds % 60}"
