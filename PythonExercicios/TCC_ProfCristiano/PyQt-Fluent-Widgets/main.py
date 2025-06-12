import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtGui import QIntValidator
from qfluentwidgets import PrimaryPushButton, LineEdit, MessageBoxBase, SubtitleLabel, PushButton, ComboBox

listaPecas = []

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
            self.lineQtd.setValidator(QIntValidator(1, 99, self))
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

        for peca in listaPecas:
            self.comboBox.addItem(peca['nome'])

        self.comboBox.setCurrentIndex(-1)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.comboBox)
        if acao != 'Excluir':
            self.lineEdit = LineEdit(self)
            if acao == 'Alterar':
                self.lineEdit.setPlaceholderText('Informe o novo nome')
            else:
                self.lineEdit.setValidator(QIntValidator(1, 99, self))
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
        self.gridLayout.addWidget(self.btnAlterar, 1, 0)
        self.gridLayout.addWidget(self.btnDeletar, 2, 0)
        self.gridLayout.addWidget(self.btnComprar, 3, 0)
        self.gridLayout.addWidget(self.btnVender, 4, 0)
        self.gridLayout.addWidget(self.btnVisualizar, 5, 0)
        self.gridLayout.addWidget(self.btnSair, 6, 1)
        self.setFixedSize(360, 0)

    def showCadastrar(self):
        w = messageBoxPeca('Cadastrar', self)
        if w.exec():
            peca = w.linePeca.text().upper()
            qtd = int(w.lineQtd.text())
            listaPecas.append({'nome': peca, 'qtd': qtd})
    def showAlterar(self):
        w = comboBoxPeca('Alterar', self)
        if w.exec():
            indice = w.comboBox.currentIndex()
            novaPeca = w.lineEdit.text().upper()
            listaPecas[indice]['nome'] = novaPeca
    def showExcluir(self):
        w = comboBoxPeca('Excluir', self)
        if w.exec():
            indice = w.comboBox.currentIndex()
            print(f'Removido item {listaPecas.pop(indice)}')
    def showComprar(self):
        w = comboBoxPeca('Comprar', self)
        if w.exec():
            indice = w.comboBox.currentIndex()
            qtd = int(w.lineEdit.text())
            listaPecas[indice]['qtd'] += qtd
    def showVender(self):
        w = comboBoxPeca('Vender', self)
        if w.exec():
            indice = w.comboBox.currentIndex()
            qtd = int(w.lineEdit.text())
            listaPecas[indice]['qtd'] -= qtd

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w1 = EstoqueCar()
    w1.show()
    app.exec_()