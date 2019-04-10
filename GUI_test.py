#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt5.QtCore import QDateTime, Qt, QTimer, QDir
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QFileDialog)
import sys
import AudioToTest
import os

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.createTopRightGroupBox()
        self.createBottomRightGroupBox()

        styleComboBox.activated[str].connect(self.changeStyle)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topRightGroupBox,1, 1)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Styles")
        self.changeStyle('Windows')

        self.A = AudioToTest.AudioToTest()

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        QApplication.setPalette(QApplication.style().standardPalette())

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Recording")

        self.recordingButton = QPushButton("Start Recording")
        self.recordingButton.setCheckable(True)
        self.recordingButton.setDefault(True)
        self.recordingButton.clicked.connect(self.recording_button_clicked)


        self.lineEdit = QLineEdit('wav file saving name')

        self.savingButton = QPushButton("Save wav")
        self.savingButton.setDefault(True)

        layout = QVBoxLayout()
        layout.addWidget(self.recordingButton)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.savingButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Speech to Text")

        self.lineEdit = QLineEdit('')

        self.chooseButton = QPushButton("Choose File")
        self.chooseButton.setDefault(True)
        self.chooseButton.clicked.connect(self.choose_button_clicked)

        self.transferButton = QPushButton("Transfer")
        self.transferButton.setDefault(True)
        self.transferButton.clicked.connect(self.transfer_button)

        self.filetransferButton = QPushButton("File Transfer")


        layout = QGridLayout()
        layout.addWidget(self.lineEdit, 0, 0, 1, 2)
        layout.addWidget(self.chooseButton, 1, 0, 1, 2)
        layout.addWidget(self.transferButton, 2, 0, 1, 2)
        layout.addWidget(self.filetransferButton,3,0,1,2)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)

    def recording_button_clicked(self):
        if self.recordingButton.isChecked():
            self.recordingButton.setText("Stop Recording")
        else:
            self.recordingButton.setText("Start Recording")

    def choose_button_clicked(self):
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '.', "wav files (*.wav)")
        self.lineEdit.setText(absolute_path[0])

    def transfer_button(self):
        self.A.recognize(self.lineEdit.text())

    def File_Trans(self):
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '.', "wav files (*.wav)")
        if absolute_path:
            os.system("ffmpeg -i "+absolute_path+"output.wav")



if __name__ == '__main__':

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
