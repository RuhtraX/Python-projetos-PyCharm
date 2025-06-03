import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from qfluentwidgets import (PrimaryPushButton, LineEdit, MessageBoxBase, SubtitleLabel, PushButton)

class messageBoxCadastrar(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('Cadastrar Peça', self)
        self.lineEdit = LineEdit(self)

        self.lineEdit.setPlaceholderText('Informe a peça')
        self.lineEdit.setClearButtonEnabled(True)

        # Adicionar os widgets
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.lineEdit)

        self.yesButton.setText('Cadastrar')
        self.cancelButton.setText('Cancelar')

        self.widget.setMinimumWidth(350)

class ButtonView(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("ButtonView{background: rgb(255,255,255)}")

class EstoqueCar(ButtonView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Estoque Car')

        # push button
        self.btnCadastrar = PrimaryPushButton('Cadastar Peça')
        self.btnCadastrar.clicked.connect(self.showCadastrar)
        self.btnProcurar = PrimaryPushButton('Procurar Peça')
        self.btnAlterar = PrimaryPushButton('Alterar Peça')
        self.btnDeletar = PrimaryPushButton('Deletar Peça')
        self.btnComprar = PrimaryPushButton('Comprar Peça')
        self.btnVender = PrimaryPushButton('Vender Peça')
        self.btnVisualizar = PrimaryPushButton('Visualizar Estoque')
        self.btnSair = PushButton('Sair')
        self.btnSair.clicked.connect(self.close)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.btnCadastrar, 0, 0)
        self.gridLayout.addWidget(self.btnProcurar, 1, 0)
        self.gridLayout.addWidget(self.btnAlterar, 2, 0)
        self.gridLayout.addWidget(self.btnDeletar, 3, 0)
        self.gridLayout.addWidget(self.btnComprar, 4, 0)
        self.gridLayout.addWidget(self.btnVender, 5, 0)
        self.gridLayout.addWidget(self.btnVisualizar, 6, 0)
        self.gridLayout.addWidget(self.btnSair, 7, 1)
        self.setFixedSize(360, 0)

    def showCadastrar(self):
        w = messageBoxCadastrar(self)
        if w.exec():
            peca = w.lineEdit.text()
            print(peca.upper())


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)

    w1 = EstoqueCar()
    w1.show()
    app.exec_()