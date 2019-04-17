import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from audio import Recorder


class GUI(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setMinimumSize(QSize(300, 300))
        self.setWindowTitle('CCMS')
        self.recording = False
        self.re = Recorder()
        self.button = QPushButton('Start Recording', self)
        self.button.move(10, 200)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        if not self.recording:
            self.recording = True
            self.button.setText('Stop Recording')
            self.re.recorder()
        else:
            self.re.savewav("test.wav")
            self.recording = False
            self.button.setText('Start Recording')


if __name__ == '__main__':
    GUI.GO()



