from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PIL import Image
import os

# Classe para representar a janela principal
class ConversorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("conversor.ui", self)

        # Conectar botões
        self.bt_ad_origem.clicked.connect(self.selecionar_arquivo)
        self.bt_converter.clicked.connect(self.converter_arquivo)

        self.show()

    def selecionar_arquivo(self):
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar arquivo", "", "Images (*.png *.ico)")
        if arquivo:
            self.txt_origem.setText(arquivo)
            extensao = os.path.splitext(arquivo)[1][1:].upper()
            self.lb_status.setText(f'Arquivo {extensao} selecionado.')

    def converter_arquivo(self):
        arquivo_origem = self.txt_origem.text()
        if not arquivo_origem:
            self.lb_status.setText("Favor selecionar um arquivo ICO ou PNG.")
            return

        if arquivo_origem.endswith('.png'):
            arquivo_destino = arquivo_origem[:-4] + '.ico'
        elif arquivo_origem.endswith('.ico'):
            arquivo_destino = arquivo_origem[:-4] + '.png'
        else:
            self.lb_status.setText("Formato não suportado.")
            return

        imagem = Image.open(arquivo_origem)
        imagem.save(arquivo_destino)

        self.lb_status.setText(f"Arquivo convertido e salvo como {arquivo_destino}")

# Função para iniciar a aplicação
def iniciar_aplicacao():
    app = QApplication([])
    janela = ConversorUI()
    app.exec_()

# Iniciar a aplicação
if __name__ == "__main__":
    iniciar_aplicacao()
