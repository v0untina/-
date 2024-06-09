from PyQt6.QtWidgets import QApplication,QGridLayout , QLabel, QWidget
from PyQt6.QtCore import Qt,QSize
import sys


class helpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 300, 600, 600)
        grid = QGridLayout()
        self.setFixedSize(500, 560)
        self.setLayout(grid)
        words=list()
        with open('help.txt', 'r', encoding="utf-8") as f:
            words = list(str(f.read()))
        self.setWindowTitle("Справка")
        label=QLabel(''.join(map(str,words)))
        label.setWordWrap(True)
        label.setStyleSheet("""
                font-family: 'Segoe UI', sans-serif; /* Задайте приятный шрифт */
                font-size: 16px; /* Укажите размер шрифта */
                color: #333333; /* Установите более темный цвет текста для лучшего контраста */
                line-height: 1.5; /* Увеличьте межстрочный интервал */
                padding: 8px; /* Добавьте отступы вокруг текста */
                background-color: #f5f5f5; /* Установите светлый фон для чтения */
                border: 1px solid #ccc; /* Добавьте границу вокруг QLabel */
                border-radius: 4px; /* Скруглите углы */
                """)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        grid.addWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = helpWindow()
    w.show()
    app.exec()