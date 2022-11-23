import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.draw.clicked.connect(self.run)
        self.can_draw = False

    def paintEvent(self, event):
        if self.can_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_elipses(qp)
            qp.end()

    def run(self):
        self.can_draw = True
        self.repaint()

    def draw_elipses(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(randint(1, 10)):
            a = randint(1, 101)
            qp.drawEllipse(randint(1, 601), randint(1, 601), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())