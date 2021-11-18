import sys

import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPaintEvent, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Yellow rounds")
        MainWindow.resize(427, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.round = QtWidgets.QPushButton(self.centralwidget)
        self.round.setGeometry(QtCore.QRect(350, 320, 75, 23))
        self.round.setObjectName("round")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Yellow rounds", "Yellow rounds"))
        self.round.setText(_translate("Yellow rounds", "Круги)"))


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.painting = False
        self.round.clicked.connect(self.startPaint)

    def startPaint(self):
        self.painting = True
        self.update()

    def paintEvent(self, event: QPaintEvent):
        if self.painting:
            paint = QPainter()
            paint.begin(self)
            self.draw(paint)
            paint.end()
            self.painting = False

    def draw(self, qp: QPainter):
        r = random.randint(5, 100)
        pen = QPen(random.choice([Qt.yellow, Qt.black, Qt.red, Qt.blue, Qt.gray, Qt.green, Qt.white]), 3, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawEllipse(random.randint(50, 350), random.randint(50, 350), r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wndw = Window()
    wndw.show()
    app.exec()