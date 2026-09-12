# import and global variable
import sys
import json

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QListWidget
)

from PySide6.QtCore import Qt


app = QApplication(sys.argv)

window = QWidget()

notes = []


window.setWindowTitle("Note App")
window.setFixedSize(600, 500)


# function for loading notes

def load_notes():
    global notes

    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)

    except FileNotFoundError:
        notes = []


# function for saving notes

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


# function for adding note

def add_note():
    title = title_entry.text()
    text = note_text.toPlainText()

    if title == "" or text == "":
        status_label.setText("Please enter title and note!")
        return

    note = {
        "title": title,
        "text": text
    }

    notes.append(note)

    save_notes()

    notes_list.addItem(title)

    title_entry.clear()
    note_text.clear()

    status_label.setText("Note added!")


# function for showing selected note

def show_note():
    selected_item = notes_list.currentRow()

    if selected_item < 0:
        return

    note = notes[selected_item]

    title_entry.setText(note["title"])
    note_text.setPlainText(note["text"])


# function for deleting note

def delete_note():
    selected_item = notes_list.currentRow()

    if selected_item < 0:
        status_label.setText("Please select a note!")
        return

    notes.pop(selected_item)

    notes_list.takeItem(selected_item)

    save_notes()

    title_entry.clear()
    note_text.clear()

    status_label.setText("Note deleted!")


# UI design


# title

title_label = QLabel(
    "Note App",
    window
)

title_label.setGeometry(
    20, 15, 560, 40
)

title_label.setAlignment(
    Qt.AlignmentFlag.AlignCenter
)

title_label.setStyleSheet(
    "font-size: 25px;"
)


# notes list

notes_list = QListWidget(
    window
)

notes_list.setGeometry(
    20, 70, 180, 300
)

notes_list.itemClicked.connect(
    show_note
)


# title input

title_label = QLabel(
    "Title",
    window
)

title_label.setGeometry(
    230, 70, 300, 25
)


title_entry = QLineEdit(
    window
)

title_entry.setGeometry(
    230, 95, 340, 35
)


# note text

note_label = QLabel(
    "Note",
    window
)

note_label.setGeometry(
    230, 140, 300, 25
)


note_text = QTextEdit(
    window
)

note_text.setGeometry(
    230, 165, 340, 205
)


# add button

add_button = QPushButton(
    "Add Note",
    window
)

add_button.setGeometry(
    20, 390, 170, 40
)

add_button.clicked.connect(
    add_note
)


# delete button

delete_button = QPushButton(
    "Delete Note",
    window
)

delete_button.setGeometry(
    210, 390, 170, 40
)

delete_button.clicked.connect(
    delete_note
)


# status label

status_label = QLabel(
    "Ready",
    window
)

status_label.setGeometry(
    20, 440, 550, 30
)

status_label.setAlignment(
    Qt.AlignmentFlag.AlignCenter
)


# load saved notes

load_notes()

for note in notes:
    notes_list.addItem(
        note["title"]
    )


# running application

window.show()

sys.exit(app.exec())
