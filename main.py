import sys
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from random import randrange, randint
from UI import Ui_MainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.draw)
        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
            x = randrange(1, 300)
            y = randrange(1, 300)
            r = randrange(1, 300)
            rect = QRect(x, y, x + r, y + r)
            qp.drawEllipse(rect)
            qp.end()
            self.flag = False

    def draw(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())


