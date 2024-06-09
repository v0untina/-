import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QStatusBar, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from help import helpWindow
import words4
import words5
import words6


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(50, 50, 620, 950)
        self.setWindowTitle("Игра Пять Букв")
        self.initUI()

        self.w = None
        self.setStyleSheet("""
                        MainWindow {
                            background-color: '#DCDCDC';
                        }
                        QPushButton {
                            font-size: 20px;
                            border: 2px solid #8f8f91;
                            border-radius: 6px;
                            background-color: #d3d7cf;
                            min-height: 40px;
                            padding: 5px;
                        }
                        QPushButton:hover {
                            background-color: #729fcf;
                            color: #ffffff;
                        }
                        QLabel {
                            font-size: 24px;
                            qproperty-alignment: 'AlignCenter';
                        }
                        QMenuBar {
                            background-color: #d3d7cf;
                            padding: 2px;
                            font-size:20px;

                            border: 1px solid #8f8f91;
                        }
                        QMenuBar::item {
                            spacing: 3px;
                            padding: 1px 4px;
                            background-color: #d3d7cf;
                            color: black;
                            border-radius: 4px;
                        }
                        QMenuBar::item:selected {
                            background-color: #729fcf;
                            color: white;
                            font-size:20px;

                        }
                        QMenuBar::item:pressed {
                            background: #729fcf;
                            
                        }
                        QMenu {
                            background-color: #d3d7cf;
                            border: 1px solid #8f8f91;
                        }
                        QMenu::item {
                            padding: 2px 20px 2px 20px;
                        }
                        QMenu::item:selected {
                            background-color: #729fcf;
                            color: white;
                        }
                        """)
        self.setStatusBar(QStatusBar(self))
        self.show()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        label = QLabel('Выберите количество букв ')
        label.setStyleSheet("""
        font-size:34px;
        font-family:Monserrat;
        """)
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)

        button4 = QPushButton('Четыре буквы')
        button4.clicked.connect(lambda: self.set_game_widget(words4.game, '4'))

        button5 = QPushButton('Пять букв')
        button5.clicked.connect(lambda: self.set_game_widget(words5.game5, '5'))

        button6 = QPushButton('Шесть букв')
        button6.clicked.connect(lambda: self.set_game_widget(words6.game6, '6'))

        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)

        menu_bar = self.menuBar()

        levels_menu = menu_bar.addMenu("Сложность")
        levels_menu4 = levels_menu.addAction(QIcon('4.png'), "Четыре буквы")
        levels_menu4.triggered.connect(self.onMyToolBarButtonClick4)

        levels_menu5 = levels_menu.addAction(QIcon('5.png'), "Пять букв")
        levels_menu5.triggered.connect(self.onMyToolBarButtonClick5)

        levels_menu6 = levels_menu.addAction(QIcon('6.png'), "Шесть букв")
        levels_menu6.triggered.connect(self.onMyToolBarButtonClick6)

        help_menu = menu_bar.addAction("Справка")
        help_menu.triggered.connect(self.onMyToolBarButtonClickHelp)

        self.setStatusBar(QStatusBar(self))

    def set_game_widget(self, game_widget_factory, level):
        if hasattr(self, 'current_level') and self.current_level == level:
            return

        self.current_level = level

        current_widget = self.centralWidget()
        if current_widget is not None:
            current_widget.deleteLater()

        new_widget = game_widget_factory()
        self.setCentralWidget(new_widget)

    def onMyToolBarButtonClick4(self):
        self.set_game_widget(words4.game, '4')

    def onMyToolBarButtonClick5(self):
        self.set_game_widget(words5.game5, '5')

    def onMyToolBarButtonClick6(self):
        self.set_game_widget(words6.game6, '6')

    def onMyToolBarButtonClickHelp(self):
        if self.w is None:
            self.w = helpWindow()
        self.w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()


цупршцприцуприцупришгцупишщцупшцуппотпотпотшотшупотцупотшуп