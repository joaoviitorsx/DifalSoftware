from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

class TelaAliquota(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.empresa = None  # Dados da empresa selecionada
        
        # Layout principal
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        
        # Título da tela
        self.label_titulo = QLabel("Configuração da Alíquota Interna")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_titulo)
        
        # Informações da empresa selecionada
        self.label_empresa = QLabel("Empresa: ")
        self.layout.addWidget(self.label_empresa)
        
        # Campo para entrada da alíquota
        self.label_aliquota = QLabel("Alíquota Interna (%)")
        self.layout.addWidget(self.label_aliquota)
        self.input_aliquota = QLineEdit()
        self.input_aliquota.setPlaceholderText("Digite a alíquota (ex: 18.00)")
        self.layout.addWidget(self.input_aliquota)
        
        # Validação para aceitar apenas números com até duas casas decimais
        aliquota_regex = QRegularExpression("^[0-9]+(\\.[0-9]{1,2})?$")
        self.input_aliquota.setValidator(QRegularExpressionValidator(aliquota_regex))
        
        # Botão de continuar
        self.botao_continuar = QPushButton("Continuar")
        self.botao_continuar.clicked.connect(self.continuar)
        self.layout.addWidget(self.botao_continuar)
        
        # Botão de voltar
        self.botao_voltar = QPushButton("Voltar")
        self.botao_voltar.clicked.connect(self.voltar_para_tela_inicial)
        self.layout.addWidget(self.botao_voltar)
    
    def definir_empresa(self, empresa):
        """Define os dados da empresa selecionada"""
        self.empresa = empresa
        self.label_empresa.setText(f"Empresa: {empresa['razao_social']} - CNPJ: {empresa['cnpj']}")
    
    def continuar(self):
        """Valida e prossegue para a tela de upload de arquivos"""
        aliquota_texto = self.input_aliquota.text().strip()
        
        if not aliquota_texto:
            QMessageBox.warning(self, "Erro", "A alíquota não pode estar vazia.")
            return
        
        try:
            aliquota = float(aliquota_texto)
            if aliquota <= 0 or aliquota > 100:
                raise ValueError
            
            # Avançar para a tela de upload
            self.main_window.mostrar_tela_principal(self.empresa, aliquota)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Digite um valor válido para a alíquota.")
    
    def voltar_para_tela_inicial(self):
        """Retorna para a tela inicial"""
        self.main_window.mostrar_tela_inicial()