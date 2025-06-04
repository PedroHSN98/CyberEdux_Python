import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QWidget, QComboBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora") # Changed window title to "Calculadora"

        # Elements of the interface
        self.label_a = QLabel("Número A:")
        self.input_a = QLineEdit(self)

        self.label_b = QLabel("Número B:")
        self.input_b = QLineEdit(self)

        self.select = QComboBox()
        # Updated items to reflect all supported operations
        self.select.addItems(["Soma", "Subtração", "Multiplicação", "Divisão", "Potenciação"])

        self.button = QPushButton("Calcular")
        self.button.clicked.connect(self.__calcular)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label_a)
        layout.addWidget(self.input_a)
        layout.addWidget(self.label_b)
        layout.addWidget(self.input_b)
        layout.addWidget(self.select)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def __calcular(self):

        operacao = self.select.currentText() 
        try:
            a = float(self.input_a.text()) 
            b = float(self.input_b.text()) 
            resultado = None 

            if operacao == "Soma":
                resultado = a + b
                message_title = "Resultado da Soma"
                message_text = f"A soma de {a} + {b} é: {resultado}"
            elif operacao == "Subtração":
                resultado = a - b
                message_title = "Resultado da Subtração"
                message_text = f"A subtração de {a} - {b} é: {resultado}"
            elif operacao == "Multiplicação":
                resultado = a * b
                message_title = "Resultado da Multiplicação"
                message_text = f"A multiplicação de {a} * {b} é: {resultado}"
            elif operacao == "Divisão":
                if b == 0: 
                    QMessageBox.warning(self, "Erro de Divisão", "Não é possível dividir por zero.")
                    return 
                resultado = a / b
                message_title = "Resultado da Divisão"
                message_text = f"A divisão de {a} / {b} é: {resultado}"
            elif operacao == "Potenciação":
                resultado = a ** b 
                message_title = "Resultado da Potenciação"
                message_text = f"A potenciação de {a} elevado a {b} é: {resultado}"
            else:
                QMessageBox.warning(self, "Erro", "Operação inválida selecionada.")
                return

            QMessageBox.information(self, message_title, message_text)

        except ValueError:
            QMessageBox.warning(self, "Erro de Entrada", "Por favor, insira números válidos em ambos os campos.")
        except Exception as ex:
            QMessageBox.warning(self, "Erro Inesperado", f"Ocorreu um erro inesperado: {ex}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
