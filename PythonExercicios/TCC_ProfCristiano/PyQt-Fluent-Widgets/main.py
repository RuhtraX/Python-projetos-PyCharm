import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from qfluentwidgets import PrimaryPushButton, LineEdit, MessageBoxBase, SubtitleLabel, PushButton, ComboBox

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

class comboBoxPeca(MessageBoxBase):
    def __init__(self, acao, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel(f'{acao} Peça', self)
        self.comboBox = ComboBox(self)

        self.comboBox.setPlaceholderText('Selecione a peça')

        items = ['A', 'B', 'C']
        self.comboBox.addItems(items)
        self.comboBox.setCurrentIndex(-1)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.comboBox)
        if acao != 'Excluir':
            self.lineEdit = LineEdit(self)
            if acao == 'Alterar':
                self.lineEdit.setPlaceholderText('Informe o novo nome')
            else:
                self.lineEdit.setPlaceholderText('Informe a quantidade')
            self.viewLayout.addWidget(self.lineEdit)
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
        self.btnAlterar.clicked.connect(self.showAlterar)
        self.btnDeletar = PrimaryPushButton('Excluir Peça')
        self.btnDeletar.clicked.connect(self.showExcluir)
        self.btnComprar = PrimaryPushButton('Comprar Peça')
        self.btnComprar.clicked.connect(self.showComprar)
        self.btnVender = PrimaryPushButton('Vender Peça')
        self.btnVender.clicked.connect(self.showVender)
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
    def showAlterar(self):
        w = comboBoxPeca('Alterar', self)
        if w.exec():
            peca = w.comboBox.currentIndex()
            novaPeca = w.lineEdit.text()
            print(f'Alteração peça índice {peca} para {novaPeca}')
    def showExcluir(self):
        w = comboBoxPeca('Excluir', self)
        if w.exec():
            peca = w.comboBox.currentIndex()
            print(f'Exclusão da peça {peca}')
    def showComprar(self):
        w = comboBoxPeca('Comprar', self)
        if w.exec():
            peca = w.comboBox.currentIndex()
            qtd = w.lineEdit.text()
            print(f'Compra de {qtd} unidades da peça {peca}')
    def showVender(self):
        w = comboBoxPeca('Vender', self)
        if w.exec():
            peca = w.comboBox.currentIndex()
            qtd = w.lineEdit.text()
            print(f'Venda de {qtd} unidades da peça {peca}')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w1 = EstoqueCar()
    w1.show()
    app.exec_()