import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRectF

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Random Circles")
        MainWindow.setGeometry(100, 100, 600, 400)
        self.centralwidget = QWidget(MainWindow)
        self.pushButton = QPushButton("Add Circle", self.centralwidget)
        self.pushButton.setGeometry(10, 10, 100, 30)
        MainWindow.setCentralWidget(self.centralwidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(50, self.width() - 100)
        y = random.randint(50, self.height() - 100)
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(QColor("black"))
            painter.drawEllipse(QRectF(x, y, diameter, diameter))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
