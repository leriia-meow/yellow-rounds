import sys

import random
from PyQt5.QtGui import QPainter, QPaintEvent, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog
from UI import Ui_MainWindow


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
        pen = QPen(Qt.yellow, 3, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawEllipse(random.randint(50, 350), random.randint(50, 350), r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wndw = Window()
    wndw.show()
    app.exec()