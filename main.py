import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRectF
from UI import Ui_MainWindow  # Импортируем сгенерированный класс интерфейса

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Кнопка для добавления окружностей
        self.ui.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(50, self.width() - 100)
        y = random.randint(50, self.height() - 100)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("yellow"))
        painter.setPen(QColor("black"))
        for x, y, diameter in self.circles:
            painter.drawEllipse(QRectF(x, y, diameter, diameter))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())