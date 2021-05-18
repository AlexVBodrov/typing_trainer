from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


def add_label():
    print('add label')


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Тренажер печати")
    window.setGeometry(300, 250, 500, 500)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Это базовая надпись")
    main_text.move(100, 100)
    main_text.adjustSize()
    # s_question_text = QtWidgets. TODO

    btn_1 = QtWidgets.QPushButton(window)
    btn_1.move(70, 150)
    btn_1.setText("Нажми на меня")
    btn_1.setFixedWidth(200)
    btn_1.clicked.connect(add_label)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    application()
