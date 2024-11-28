import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi

class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.load_data()
        self.refreshButton.clicked.connect(self.load_data)

    def load_data(self):
        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()
        query = "SELECT * FROM coffee"
        results = cursor.execute(query).fetchall()
        connection.close()

        self.tableWidget.setRowCount(len(results))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Название", "Степень обжарки", "Молотый/в зернах",
            "Описание вкуса", "Цена", "Объем"
        ])

        for row_index, row_data in enumerate(results):
            for column_index, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
