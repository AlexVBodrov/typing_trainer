from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Тренажер печати")
        self.setGeometry(300, 250, 500, 500)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn_1 = QtWidgets.QPushButton(self)
        self.btn_1.move(70, 150)
        self.btn_1.setText("Нажми на меня")
        self.btn_1.setFixedWidth(200)
        self.btn_1.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText('Вторая надпись')
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


    
if __name__ == "__main__":
    application()
