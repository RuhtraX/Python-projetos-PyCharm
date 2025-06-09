import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from qfluentwidgets import (PrimaryPushButton, LineEdit, MessageBoxBase, SubtitleLabel, PushButton)

class messageBoxPeca(MessageBoxBase):
    def __init__(self, acao, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel(f'{acao} Peça', self)
        self.linePeca = LineEdit(self)

        self.linePeca.setPlaceholderText('Informe a peça')

        # Adicionar os widgets
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.linePeca)
        if acao == 'Cadastrar':
            self.lineQtd = LineEdit(self)
            self.lineQtd.setPlaceholderText('Informe a quantidade')
            self.viewLayout.addWidget(self.lineQtd)

        self.yesButton.setText(acao)
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
        self.btnProcurar.clicked.connect(self.showProcurar)
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
        w = messageBoxPeca('Cadastrar', self)
        if w.exec():
            peca = w.linePeca.text()
            qtd = w.lineQtd.text()
            print(f'{peca.upper()}: {qtd}')
    def showProcurar(self):
        w = messageBoxPeca('Procurar', self)
        if w.exec():
            peca = w.lineEdit.text()
            print(peca.upper())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w1 = EstoqueCar()
    w1.show()
    app.exec_()