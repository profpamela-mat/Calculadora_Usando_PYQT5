import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, \
    QWidget, QGridLayout, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('MinhaCalculadora')
        self.setFixedSize(400,400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size:25px;}'
        )

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.addBotao(QPushButton('1'), 1, 0, 1, 1)
        self.addBotao(QPushButton('2'), 1, 1, 1, 1)
        self.addBotao(QPushButton('3'), 1, 2, 1, 1)
        self.addBotao(QPushButton('+'), 1, 3, 1, 1)
        self.addBotao(QPushButton('C'), 1, 4, 1, 1,
                      lambda: self.display.setText(''),
                      'background: #d5580d; color: #fff; font-weight: 700;'
                      )
        self.addBotao(QPushButton('4'), 2, 0, 1, 1)
        self.addBotao(QPushButton('5'), 2, 1, 1, 1)
        self.addBotao(QPushButton('6'), 2, 2, 1, 1)
        self.addBotao(QPushButton('-'), 2, 3, 1, 1)
        self.addBotao(QPushButton('<-'), 2, 4, 1, 1,
                      lambda: self.display.setText(
                          self.display.text()[:-1]
                      ),
                      'background: #13823a; color: #fff; font-weight: 700;'
                      )
        self.addBotao(QPushButton('7'), 3, 0, 1, 1)
        self.addBotao(QPushButton('8'), 3, 1, 1, 1)
        self.addBotao(QPushButton('9'), 3, 2, 1, 1)
        self.addBotao(QPushButton('/'), 3, 3, 1, 1)
        self.addBotao(QPushButton(' '), 3, 4, 1, 1)
        self.addBotao(QPushButton('.'), 3, 0, 1, 1)
        self.addBotao(QPushButton('0'), 3, 1, 1, 1)
        self.addBotao(QPushButton(' '), 3, 2, 1, 1)
        self.addBotao(QPushButton('*'), 3, 3, 1, 1)
        self.addBotao(QPushButton('='), 3, 4, 1, 1,
                      self.igual,
                      'background: #095177; color: #fff; font-weight: 700;'
                      )

        self.setCentralWidget(self.cw)

    def addBotao(self, bt, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(bt, row, col, rowspan, colspan)

        if not funcao:
            bt.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + bt.text()
                )
            )
        else:
            bt.clicked.connect(funcao)

        if style:
            bt.setStyleSheet(style)

        bt.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta Inválida!')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()