import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from audio import Recorder
import multiprocessing


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(300, 300))
        self.setWindowTitle('CCMS')
        self.recording = False

        self.button = QPushButton('Start Recording', self)
        self.button.move(10, 200)
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        if not self.recording:
            self.recording = True
            self.button.setText('Stop Recording')
            re = Recorder()
            P = multiprocessing.Process(target=re.recorder())
            P.start()
        else:
            self.re.savewav("test.wav")
            self.re.Stop_record()
            self.recording = False
            self.button.setText('Start Recording')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qb = GUI()
    qb.show()
    sys.exit(app.exec_())



