from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class CustomTableWidget(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        
        # Set the table properties
        self.setShowGrid(False)  # Hide the default grid lines
        self.verticalHeader().setVisible(False)  # Hide vertical header
        
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Optional: Hide horizontal scrollbar

    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QPainter(self.viewport())
        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))

        for row in range(self.rowCount()):
            painter.drawLine(0, self.rowHeight(row) - 1, self.viewport().width(), self.rowHeight(row) - 1)

app = QApplication([])

tableWidget = CustomTableWidget(3, 3)

# Add some data to the table
tableWidget.setItem(0, 0, QTableWidgetItem("Item 1"))
tableWidget.setItem(0, 1, QTableWidgetItem("Item 2"))
tableWidget.setItem(0, 2, QTableWidgetItem("Item 3"))

tableWidget.show()

app.exec()
