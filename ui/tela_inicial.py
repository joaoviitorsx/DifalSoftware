from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from database.db_conexao import conectar_banco, listar_empresas

class TelaInicial(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.conexao = conectar_banco()
        
        # Layout principal
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        
        # Título da tela
        self.label_titulo = QLabel("Selecione ou cadastre uma empresa")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_titulo)
        
        # ComboBox para selecionar empresas cadastradas
        self.combo_empresas = QComboBox()
        self.layout.addWidget(self.combo_empresas)
        
        # Botão para cadastrar nova empresa
        self.botao_cadastrar = QPushButton("Cadastrar Nova Empresa")
        self.botao_cadastrar.clicked.connect(self.ir_para_cadastro)
        self.layout.addWidget(self.botao_cadastrar)
        
        # Botão para continuar com a empresa selecionada
        self.botao_continuar = QPushButton("Continuar")
        self.botao_continuar.clicked.connect(self.selecionar_empresa)
        self.layout.addWidget(self.botao_continuar)
        
        # Carregar empresas do banco
        self.carregar_empresas()
    
    def carregar_empresas(self):
        """Carrega as empresas do banco de dados e preenche o ComboBox"""
        empresas = listar_empresas(self.conexao)
        self.combo_empresas.clear()
        self.combo_empresas.addItem("Selecione uma empresa", None)
        
        for empresa in empresas:
            self.combo_empresas.addItem(f"{empresa['razao_social']} - {empresa['cnpj']}", empresa)
    
    def selecionar_empresa(self):
        """Obtém a empresa selecionada e avança para a próxima tela."""
        index = self.combo_empresas.currentIndex()
        if index == 0:
            QMessageBox.warning(self, "Aviso", "Selecione uma empresa antes de continuar.")
            return
        
        empresa = self.combo_empresas.currentData()
        self.main_window.mostrar_tela_aliquota(empresa)
    
    def ir_para_cadastro(self):
        """Redireciona para a tela de cadastro de empresas."""
        self.main_window.mostrar_tela_cadastro()
