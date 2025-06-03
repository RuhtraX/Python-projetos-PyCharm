import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from qfluentwidgets import (PrimaryPushButton)

class ButtonView(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("ButtonView{background: rgb(255,255,255)}")

class PrimaryPushButtonDemo(ButtonView):
    def __init__(self):
        super().__init__()
        self.windowTitle = 'Estoque Car'

        # push button
        self.btnCadastrar = PrimaryPushButton('Cadastar Peça')
        self.btnProcurar = PrimaryPushButton('Procurar Peça')
        self.btnAlterar = PrimaryPushButton('Alterar Peça')
        self.btnDeletar = PrimaryPushButton('Deletar Peça')
        self.btnComprar = PrimaryPushButton('Comprar Peça')
        self.btnVender = PrimaryPushButton('Vender Peça')
        self.btnVisualizar = PrimaryPushButton('Visualizar Estoque')
        self.btnSair = PrimaryPushButton('Sair')

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.btnCadastrar, 0, 0)
        self.gridLayout.addWidget(self.btnProcurar, 1, 0)
        self.gridLayout.addWidget(self.btnAlterar, 2, 0)
        self.gridLayout.addWidget(self.btnDeletar, 3, 0)
        self.gridLayout.addWidget(self.btnComprar, 4, 0)
        self.gridLayout.addWidget(self.btnVender, 5, 0)
        self.gridLayout.addWidget(self.btnVisualizar, 6, 0)
        self.gridLayout.addWidget(self.btnSair, 7, 1)

        self.resize(320, 340)

if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)

    w1 = PrimaryPushButtonDemo()
    w1.show()
    app.exec_()