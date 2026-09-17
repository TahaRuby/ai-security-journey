# import

import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6.QtCore import QTimer


# create application

app = QApplication(sys.argv)


# create window

window = QWidget()

window.setWindowTitle("Countdown")
window.resize(400, 300)


# variables

remaining_seconds = 60


# timer

timer = QTimer()


# functions

def update_display():
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    time_label.setText(f"{minutes:02d}:{seconds:02d}")


def countdown():
    global remaining_seconds

    if remaining_seconds > 0:
        remaining_seconds -= 1
        update_display()

    else:
        timer.stop()
        time_label.setText("Time's up!")


def start_countdown():
    timer.start(1000)


def pause_countdown():
    timer.stop()


def reset_countdown():
    global remaining_seconds

    timer.stop()

    remaining_seconds = 60

    update_display()


# connect timer

timer.timeout.connect(countdown)


# display

time_label = QLabel("01:00")

time_label.setStyleSheet(
    "font-size: 50px; font-weight: bold;"
)

time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


# buttons

start_button = QPushButton("Start")
pause_button = QPushButton("Pause")
reset_button = QPushButton("Reset")


# button commands

start_button.clicked.connect(start_countdown)
pause_button.clicked.connect(pause_countdown)
reset_button.clicked.connect(reset_countdown)


# button layout

button_layout = QHBoxLayout()

button_layout.addWidget(start_button)
button_layout.addWidget(pause_button)
button_layout.addWidget(reset_button)


# main layout

main_layout = QVBoxLayout()

main_layout.addWidget(time_label)

main_layout.addLayout(button_layout)


# set layout

window.setLayout(main_layout)


# show window

window.show()


# start application

sys.exit(app.exec())
