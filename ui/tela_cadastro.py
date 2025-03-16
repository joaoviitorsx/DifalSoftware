from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from database.db_conexao import conectar_banco, cadastrar_empresa

class TelaCadastro(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.conexao = conectar_banco()
        
        # Layout principal
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        
        # Título da tela
        self.label_titulo = QLabel("Cadastro de Empresa")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_titulo)
        
        # Campo para CNPJ
        self.label_cnpj = QLabel("CNPJ")
        self.layout.addWidget(self.label_cnpj)
        self.input_cnpj = QLineEdit()
        self.input_cnpj.setPlaceholderText("00.000.000/0000-00")
        self.layout.addWidget(self.input_cnpj)
        
        # Validação do CNPJ
        cnpj_regex = QRegularExpression("[0-9]{2}\\.[0-9]{3}\\.[0-9]{3}/[0-9]{4}-[0-9]{2}")
        self.input_cnpj.setValidator(QRegularExpressionValidator(cnpj_regex))
        
        # Campo para Razão Social
        self.label_razao_social = QLabel("Razão Social")
        self.layout.addWidget(self.label_razao_social)
        self.input_razao_social = QLineEdit()
        self.input_razao_social.setPlaceholderText("Nome da Empresa")
        self.layout.addWidget(self.input_razao_social)
        
        # Botão de salvar empresa
        self.botao_salvar = QPushButton("Salvar")
        self.botao_salvar.clicked.connect(self.salvar_empresa)
        self.layout.addWidget(self.botao_salvar)
        
        # Botão de voltar
        self.botao_voltar = QPushButton("Voltar")
        self.botao_voltar.clicked.connect(self.voltar_para_tela_inicial)
        self.layout.addWidget(self.botao_voltar)
    
    def salvar_empresa(self):
        """Cadastra a empresa no banco de dados"""
        cnpj = self.input_cnpj.text().strip()
        razao_social = self.input_razao_social.text().strip()
        
        if not cnpj or not razao_social:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos corretamente.")
            return
        
        cadastrar_empresa(self.conexao, cnpj, razao_social)
        QMessageBox.information(self, "Sucesso", "Empresa cadastrada com sucesso!")
        self.voltar_para_tela_inicial()
    
    def voltar_para_tela_inicial(self):
        """Retorna para a tela inicial após o cadastro"""
        self.main_window.mostrar_tela_inicial()
