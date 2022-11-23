import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from gui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        for i in range(randint(1, 10)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255),
                               randint(0, 255)))
            a = randint(1, 101)
            qp.drawEllipse(randint(1, 601), randint(1, 601), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())