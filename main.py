import sys

from PySide6.QtWidgets import QApplication
from player import Player

app = QApplication(sys.argv)
music_player = Player()
music_player.show()
app.exec()
