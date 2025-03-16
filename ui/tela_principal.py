from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QProgressBar, QMessageBox
from PySide6.QtCore import Qt
from utils.ler_arquivos import processar_nfes

class TelaPrincipal(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.empresa = None
        self.aliquota = None
        self.arquivo_xmls = None
        self.arquivo_ncm = None
        
        # Layout principal
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        
        # Título da tela
        self.label_titulo = QLabel("Upload de Arquivos para Processamento")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_titulo)
        
        # Informações da empresa selecionada
        self.label_empresa = QLabel("Empresa: ")
        self.layout.addWidget(self.label_empresa)
        
        # Alíquota informada
        self.label_aliquota = QLabel("Alíquota Interna: ")
        self.layout.addWidget(self.label_aliquota)
        
        # Botões para seleção de arquivos
        self.botao_selecionar_xmls = QPushButton("Selecionar Planilha de XMLs")
        self.botao_selecionar_xmls.clicked.connect(self.selecionar_arquivo_xmls)
        self.layout.addWidget(self.botao_selecionar_xmls)
        
        self.botao_selecionar_ncm = QPushButton("Selecionar Planilha de NCMs")
        self.botao_selecionar_ncm.clicked.connect(self.selecionar_arquivo_ncm)
        self.layout.addWidget(self.botao_selecionar_ncm)
        
        # Barra de progresso
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)
        
        # Botão de processamento
        self.botao_processar = QPushButton("Processar NF-e")
        self.botao_processar.clicked.connect(self.processar_dados)
        self.layout.addWidget(self.botao_processar)
        
        # Botão de voltar
        self.botao_voltar = QPushButton("Voltar")
        self.botao_voltar.clicked.connect(self.voltar_para_tela_aliquota)
        self.layout.addWidget(self.botao_voltar)
    
    def definir_dados(self, empresa, aliquota):
        """Define os dados da empresa e alíquota selecionada"""
        self.empresa = empresa
        self.aliquota = aliquota
        self.label_empresa.setText(f"Empresa: {empresa['razao_social']} - CNPJ: {empresa['cnpj']}")
        self.label_aliquota.setText(f"Alíquota Interna: {aliquota}%")
    
    def selecionar_arquivo_xmls(self):
        """Abre o diálogo para selecionar a planilha de XMLs"""
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar Planilha de XMLs", "", "Planilhas Excel (*.xlsx)")
        if arquivo:
            self.arquivo_xmls = arquivo
            QMessageBox.information(self, "Arquivo Selecionado", f"Planilha de XMLs carregada: {arquivo}")
    
    def selecionar_arquivo_ncm(self):
        """Abre o diálogo para selecionar a planilha de NCMs"""
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar Planilha de NCMs", "", "Planilhas Excel (*.xlsx)")
        if arquivo:
            self.arquivo_ncm = arquivo
            QMessageBox.information(self, "Arquivo Selecionado", f"Planilha de NCMs carregada: {arquivo}")
    
    def processar_dados(self):
        """Valida os arquivos e inicia o processamento"""
        if not self.arquivo_xmls or not self.arquivo_ncm:
            QMessageBox.warning(self, "Erro", "Selecione ambos os arquivos antes de processar.")
            return
        
        # Chama a função de processamento
        processar_nfes(self.arquivo_xmls, self.arquivo_ncm, self.progress_bar, self)
    
    def voltar_para_tela_aliquota(self):
        """Retorna para a tela de alíquota"""
        self.main_window.mostrar_tela_aliquota(self.empresa)

