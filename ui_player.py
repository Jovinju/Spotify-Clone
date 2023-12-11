# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(907, 606)
        icon = QIcon()
        icon.addFile(u":/resources/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0 , 0);\n"
"font-family: Arial Black;\n"
"font-size: 16px;\n"
"color: rgb(167, 167, 167);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.music_frame = QFrame(self.centralwidget)
        self.music_frame.setObjectName(u"music_frame")
        self.music_frame.setAutoFillBackground(False)
        self.music_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(18, 18, 18);\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.music_frame.setFrameShape(QFrame.StyledPanel)
        self.music_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.music_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.music_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.playlist_name = QLabel(self.frame)
        self.playlist_name.setObjectName(u"playlist_name")
        self.playlist_name.setStyleSheet(u"font-size: 32px;\n"
"color: rgb(245, 245, 245);\n"
"margin-left: 2px;")
        self.playlist_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.playlist_name)

        self.playlist_control_panel = QFrame(self.frame)
        self.playlist_control_panel.setObjectName(u"playlist_control_panel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.playlist_control_panel.sizePolicy().hasHeightForWidth())
        self.playlist_control_panel.setSizePolicy(sizePolicy1)
        self.playlist_control_panel.setStyleSheet(u"QPushButton {\n"
"	background: rgb(18, 18, 18);\n"
"	border-radius: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	background: rgb(32, 32, 32);\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.playlist_control_panel)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.play_playlist_button = QPushButton(self.playlist_control_panel)
        self.play_playlist_button.setObjectName(u"play_playlist_button")
        self.play_playlist_button.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.play_playlist_button.sizePolicy().hasHeightForWidth())
        self.play_playlist_button.setSizePolicy(sizePolicy2)
        self.play_playlist_button.setMinimumSize(QSize(48, 48))
        self.play_playlist_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_playlist_button.setStyleSheet(u"QPushButton {\n"
"	border-radius: 24px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/resources/play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/resources/pause.png", QSize(), QIcon.Normal, QIcon.On)
        icon1.addFile(u":/resources/play.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon1.addFile(u":/resources/play.png", QSize(), QIcon.Disabled, QIcon.On)
        self.play_playlist_button.setIcon(icon1)
        self.play_playlist_button.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.play_playlist_button)

        self.add_track_button = QPushButton(self.playlist_control_panel)
        self.add_track_button.setObjectName(u"add_track_button")
        self.add_track_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.add_track_button.sizePolicy().hasHeightForWidth())
        self.add_track_button.setSizePolicy(sizePolicy2)
        self.add_track_button.setMinimumSize(QSize(32, 32))
        self.add_track_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/resources/plus.png", QSize(), QIcon.Normal, QIcon.On)
        icon2.addFile(u":/resources/plus.png", QSize(), QIcon.Disabled, QIcon.On)
        self.add_track_button.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.add_track_button)

        self.remove_track_button = QPushButton(self.playlist_control_panel)
        self.remove_track_button.setObjectName(u"remove_track_button")
        self.remove_track_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.remove_track_button.sizePolicy().hasHeightForWidth())
        self.remove_track_button.setSizePolicy(sizePolicy2)
        self.remove_track_button.setMinimumSize(QSize(32, 32))
        self.remove_track_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/resources/minus.png", QSize(), QIcon.Normal, QIcon.On)
        icon3.addFile(u":/resources/minus.png", QSize(), QIcon.Disabled, QIcon.On)
        self.remove_track_button.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.remove_track_button)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addWidget(self.playlist_control_panel)


        self.verticalLayout_4.addWidget(self.frame)

        self.music_list_widget = QListWidget(self.music_frame)
        self.music_list_widget.setObjectName(u"music_list_widget")
        self.music_list_widget.setStyleSheet(u"QListView {\n"
"	margin-left: 10px;\n"
"}\n"
"QListView:focus {\n"
"	outline: none;\n"
"}\n"
"QListView::item {\n"
"	color: rgb(230, 230 , 230);\n"
"	border-radius: 5px;\n"
"	padding: 4px, 4px;\n"
"	margin: 2px, 2px;\n"
"}\n"
"QListView::item:selected:!active {\n"
"	color: rgb(230, 230 , 230);\n"
"}\n"
"QListView::item:hover {\n"
"	background: rgb(26, 26, 26);\n"
"	color: rgb(230, 230 , 230);\n"
"}\n"
"QListView::item:selected {\n"
"	background: rgb(34, 34, 34);\n"
"	border:none;\n"
"}\n"
"QListView:focus {\n"
"	outline: none;\n"
"}\n"
"QListView::item {\n"
"	border-radius: 5px;\n"
"	padding: 4px, 4px;\n"
"	margin: 2px, 2px;\n"
"}\n"
"QListView::item:selected:!active {\n"
"	color: rgb(230, 230 , 230);\n"
"}\n"
"QListView::item:hover {\n"
"	background: rgb(26, 26, 26);\n"
"	color: rgb(230, 230 , 230);\n"
"}\n"
"QListView::item:selected {\n"
"	background: rgb(34, 34, 34);\n"
"	border:none;\n"
"}\n"
"QListView::item:selected:hover {\n"
"	background: rgb(34, 34, 34);\n"
"	border:none;\n"
"}")
        self.music_list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_4.addWidget(self.music_list_widget)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 6)

        self.gridLayout.addWidget(self.music_frame, 0, 1, 1, 1)

        self.playlist_frame = QFrame(self.centralwidget)
        self.playlist_frame.setObjectName(u"playlist_frame")
        self.playlist_frame.setStyleSheet(u"background-color: rgb(18, 18, 18);\n"
"border-radius: 8px;\n"
"color: rgb(167, 167, 167);")
        self.playlist_frame.setFrameShape(QFrame.StyledPanel)
        self.playlist_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.playlist_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, -1, -1)
        self.label = QLabel(self.playlist_frame)
        self.label.setObjectName(u"label")
        self.label.setContextMenuPolicy(Qt.NoContextMenu)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setMargin(6)
        self.label.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.label)

        self.add_playlist_button = QPushButton(self.playlist_frame)
        self.add_playlist_button.setObjectName(u"add_playlist_button")
        sizePolicy2.setHeightForWidth(self.add_playlist_button.sizePolicy().hasHeightForWidth())
        self.add_playlist_button.setSizePolicy(sizePolicy2)
        self.add_playlist_button.setMinimumSize(QSize(32, 32))
        self.add_playlist_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_playlist_button.setLayoutDirection(Qt.LeftToRight)
        self.add_playlist_button.setStyleSheet(u"QPushButton {\n"
"	border-radius: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(32, 32, 32);\n"
"	color: rgb(230, 230, 230);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/resources/plus.png", QSize(), QIcon.Normal, QIcon.On)
        self.add_playlist_button.setIcon(icon4)

        self.horizontalLayout.addWidget(self.add_playlist_button)

        self.remove_playlist_button = QPushButton(self.playlist_frame)
        self.remove_playlist_button.setObjectName(u"remove_playlist_button")
        self.remove_playlist_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.remove_playlist_button.sizePolicy().hasHeightForWidth())
        self.remove_playlist_button.setSizePolicy(sizePolicy2)
        self.remove_playlist_button.setMinimumSize(QSize(32, 32))
        self.remove_playlist_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_playlist_button.setStyleSheet(u"QPushButton {\n"
"	border-radius: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(32, 32, 32);\n"
"	color: rgb(230, 230, 230);\n"
"}")
        self.remove_playlist_button.setIcon(icon3)

        self.horizontalLayout.addWidget(self.remove_playlist_button)

        self.horizontalLayout.setStretch(0, 10)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.playlist_widget = QListWidget(self.playlist_frame)
        self.playlist_widget.setObjectName(u"playlist_widget")
        self.playlist_widget.setStyleSheet(u"QListView {\n"
"	margin-left: 2px;\n"
"}\n"
"QListView:focus {\n"
"	outline: none;\n"
"}\n"
"QListView::item {\n"
"	color: rgb(230, 230 , 230);\n"
"	border-radius: 5px;\n"
"	padding: 4px, 4px;\n"
"	margin: 2px, 2px;\n"
"}\n"
"QListView::item:selected:!active {\n"
"	color: rgb(230, 230 , 230);\n"
"}\n"
"QListView::item:hover {\n"
"	background: rgb(26, 26, 26);\n"
"}\n"
"QListView::item:selected {\n"
"	background: rgb(34, 34, 34);\n"
"	border:none;\n"
"}\n"
"QListView:focus {\n"
"	outline: none;\n"
"}\n"
"QListView::item {\n"
"	border-radius: 5px;\n"
"	padding: 4px, 4px;\n"
"	margin: 2px, 2px;\n"
"}\n"
"QListView::item:selected:!active {\n"
"	color: rgb(230, 230 , 230);\n"
"}\n"
"QListView::item:hover {\n"
"	background: rgb(26, 26, 26);\n"
"	color: rgb(230, 230 , 230);\n"
"}\n"
"QListView::item:selected {\n"
"	background: rgb(34, 34, 34);\n"
"	border:none;\n"
"}\n"
"QListView::item:selected:hover {\n"
"	background: rgb(34, 34, 34);\n"
"	border:none;\n"
"}")
        self.playlist_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.playlist_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.playlist_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.playlist_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.playlist_widget.setFlow(QListView.TopToBottom)
        self.playlist_widget.setResizeMode(QListView.Fixed)
        self.playlist_widget.setLayoutMode(QListView.SinglePass)
        self.playlist_widget.setViewMode(QListView.ListMode)
        self.playlist_widget.setUniformItemSizes(False)
        self.playlist_widget.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.playlist_widget)


        self.gridLayout.addWidget(self.playlist_frame, 0, 0, 1, 1)

        self.music_info_frame = QFrame(self.centralwidget)
        self.music_info_frame.setObjectName(u"music_info_frame")
        self.music_info_frame.setFrameShape(QFrame.StyledPanel)
        self.music_info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.music_info_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.current_photo = QLabel(self.music_info_frame)
        self.current_photo.setObjectName(u"current_photo")
        sizePolicy2.setHeightForWidth(self.current_photo.sizePolicy().hasHeightForWidth())
        self.current_photo.setSizePolicy(sizePolicy2)
        self.current_photo.setMinimumSize(QSize(72, 72))
        self.current_photo.setMaximumSize(QSize(72, 72))
        self.current_photo.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.current_photo)

        self.info_frame = QFrame(self.music_info_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setStyleSheet(u"margin: 0px")
        self.verticalLayout_2 = QVBoxLayout(self.info_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.current_title_info = QLabel(self.info_frame)
        self.current_title_info.setObjectName(u"current_title_info")
        sizePolicy2.setHeightForWidth(self.current_title_info.sizePolicy().hasHeightForWidth())
        self.current_title_info.setSizePolicy(sizePolicy2)
        self.current_title_info.setMaximumSize(QSize(200, 16777215))
        self.current_title_info.setStyleSheet(u"")
        self.current_title_info.setTextFormat(Qt.AutoText)
        self.current_title_info.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.current_title_info)

        self.current_artist_info = QLabel(self.info_frame)
        self.current_artist_info.setObjectName(u"current_artist_info")
        self.current_artist_info.setStyleSheet(u"font-size: 10px;\n"
"color: rgb(130, 130 , 130);")

        self.verticalLayout_2.addWidget(self.current_artist_info)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.info_frame)

        self.horizontalLayout_5.setStretch(1, 1)

        self.gridLayout.addWidget(self.music_info_frame, 1, 0, 1, 1)

        self.control_panel_frame = QFrame(self.centralwidget)
        self.control_panel_frame.setObjectName(u"control_panel_frame")
        self.control_panel_frame.setEnabled(True)
        self.control_panel_frame.setStyleSheet(u"QPushButton {\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: rgb(26, 26, 26);\n"
"	border: none;\n"
"	border-radius: 16px;\n"
"}")
        self.control_panel_frame.setFrameShape(QFrame.StyledPanel)
        self.control_panel_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.control_panel_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.music_cotrol_panel = QVBoxLayout()
        self.music_cotrol_panel.setSpacing(0)
        self.music_cotrol_panel.setObjectName(u"music_cotrol_panel")
        self.control_buttons = QFrame(self.control_panel_frame)
        self.control_buttons.setObjectName(u"control_buttons")
        self.control_buttons.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.control_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.previous_button = QPushButton(self.control_buttons)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy2)
        self.previous_button.setMinimumSize(QSize(32, 32))
        icon5 = QIcon()
        iconThemeName = u"previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u":/resources/previous.png", QSize(), QIcon.Normal, QIcon.On)
            icon5.addFile(u":/resources/previous.png", QSize(), QIcon.Disabled, QIcon.On)

        self.previous_button.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.previous_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.play_pause_button = QPushButton(self.control_buttons)
        self.play_pause_button.setObjectName(u"play_pause_button")
        self.play_pause_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.play_pause_button.sizePolicy().hasHeightForWidth())
        self.play_pause_button.setSizePolicy(sizePolicy2)
        self.play_pause_button.setMinimumSize(QSize(36, 36))
        self.play_pause_button.setStyleSheet(u"QPushButton {\n"
"	background: rgb(250, 250, 250);\n"
"	border-radius: 18px;\n"
"}\n"
"QPushButton:hover {\n"
"	background: rgb(200, 200 ,200);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/resources/play-black.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/resources/pause-black.png", QSize(), QIcon.Normal, QIcon.On)
        icon6.addFile(u":/resources/play-black.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon6.addFile(u":/resources/pause-black.png", QSize(), QIcon.Disabled, QIcon.On)
        self.play_pause_button.setIcon(icon6)
        self.play_pause_button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.play_pause_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.next_button = QPushButton(self.control_buttons)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy2)
        self.next_button.setMinimumSize(QSize(32, 32))
        icon7 = QIcon()
        iconThemeName = u"next"
        if QIcon.hasThemeIcon(iconThemeName):
            icon7 = QIcon.fromTheme(iconThemeName)
        else:
            icon7.addFile(u":/resources/next.png", QSize(), QIcon.Normal, QIcon.On)
            icon7.addFile(u":/resources/next.png", QSize(), QIcon.Disabled, QIcon.On)

        self.next_button.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.next_button)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.music_cotrol_panel.addWidget(self.control_buttons)

        self.slider_music_frame = QFrame(self.control_panel_frame)
        self.slider_music_frame.setObjectName(u"slider_music_frame")
        self.slider_music_frame.setStyleSheet(u"font-size: 12px;")
        self.control_slider = QHBoxLayout(self.slider_music_frame)
        self.control_slider.setObjectName(u"control_slider")
        self.current_time_label = QLabel(self.slider_music_frame)
        self.current_time_label.setObjectName(u"current_time_label")

        self.control_slider.addWidget(self.current_time_label)

        self.main_slider = QSlider(self.slider_music_frame)
        self.main_slider.setObjectName(u"main_slider")
        self.main_slider.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_slider.sizePolicy().hasHeightForWidth())
        self.main_slider.setSizePolicy(sizePolicy3)
        self.main_slider.setFocusPolicy(Qt.StrongFocus)
        self.main_slider.setAutoFillBackground(False)
        self.main_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 4px;\n"
"    background: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background: white;\n"
"	width: 12px;\n"
"	margin: -4px 0;\n"
"	border-radius: 6px;\n"
" }\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"	background: rgb(77, 77, 77);\n"
"}")
        self.main_slider.setMaximum(100)
        self.main_slider.setPageStep(0)
        self.main_slider.setValue(0)
        self.main_slider.setTracking(True)
        self.main_slider.setOrientation(Qt.Horizontal)
        self.main_slider.setInvertedAppearance(False)
        self.main_slider.setInvertedControls(False)
        self.main_slider.setTickPosition(QSlider.NoTicks)

        self.control_slider.addWidget(self.main_slider)

        self.track_time_label = QLabel(self.slider_music_frame)
        self.track_time_label.setObjectName(u"track_time_label")

        self.control_slider.addWidget(self.track_time_label)


        self.music_cotrol_panel.addWidget(self.slider_music_frame)


        self.horizontalLayout_3.addLayout(self.music_cotrol_panel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, -1, 10, -1)
        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.volume_button = QPushButton(self.control_panel_frame)
        self.volume_button.setObjectName(u"volume_button")
        self.volume_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.volume_button.sizePolicy().hasHeightForWidth())
        self.volume_button.setSizePolicy(sizePolicy2)
        self.volume_button.setMinimumSize(QSize(32, 32))
        self.volume_button.setLayoutDirection(Qt.LeftToRight)
        self.volume_button.setStyleSheet(u"")
        icon8 = QIcon()
        iconThemeName = u"volume"
        if QIcon.hasThemeIcon(iconThemeName):
            icon8 = QIcon.fromTheme(iconThemeName)
        else:
            icon8.addFile(u":/resources/volume-max.png", QSize(), QIcon.Normal, QIcon.On)
            icon8.addFile(u":/resources/volume-max.png", QSize(), QIcon.Disabled, QIcon.On)

        self.volume_button.setIcon(icon8)
        self.volume_button.setIconSize(QSize(20, 20))
        self.volume_button.setCheckable(True)
        self.volume_button.setChecked(True)
        self.volume_button.setFlat(False)

        self.horizontalLayout_4.addWidget(self.volume_button)

        self.volume_slider = QSlider(self.control_panel_frame)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.volume_slider.sizePolicy().hasHeightForWidth())
        self.volume_slider.setSizePolicy(sizePolicy2)
        self.volume_slider.setContextMenuPolicy(Qt.NoContextMenu)
        self.volume_slider.setLayoutDirection(Qt.LeftToRight)
        self.volume_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 4px;\n"
"    background: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background: white;\n"
"	width: 12px;\n"
"	margin: -4px 0;\n"
"	border-radius: 6px;\n"
" }\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"	background: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"	background: rgb(77, 77, 77);\n"
"}")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setSingleStep(1)
        self.volume_slider.setPageStep(25)
        self.volume_slider.setValue(100)
        self.volume_slider.setTracking(True)
        self.volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.volume_slider)

        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 10)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.gridLayout.addWidget(self.control_panel_frame, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 8)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 907, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.playlist_widget.setCurrentRow(-1)
        self.volume_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music Player", None))
        self.playlist_name.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u043f\u043b\u0435\u0439\u043b\u0438\u0441\u0442", None))
        self.play_playlist_button.setText("")
        self.add_track_button.setText("")
        self.remove_track_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u044f \u043c\u0435\u0434\u0438\u0430\u0442\u0435\u043a\u0430", None))
        self.add_playlist_button.setText("")
        self.remove_playlist_button.setText("")
        self.current_photo.setText("")
        self.current_title_info.setText("")
        self.current_artist_info.setText("")
        self.previous_button.setText("")
        self.play_pause_button.setText("")
        self.next_button.setText("")
        self.current_time_label.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.track_time_label.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.volume_button.setText("")
    # retranslateUi

