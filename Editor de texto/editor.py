# # Texto em caixa alta
# texto = input("Digite um texto: ")
# texto_em_caixa_alta = texto.upper()
# print("Texto em caixa alta:", texto_em_caixa_alta)

# # Texto em caixa baixa
# texto = input("Digite um texto: ")
# texto_em_caixa_alta = texto.lower()
# print("Texto em caixa baixa:", texto_em_caixa_alta)

# # Texto em formato de título
# texto = input("Digite um texto: ")
# texto_em_caixa_alta = texto.title()
# print("Texto em caixa alta:", texto_em_caixa_alta)

# # Converter o texto upcase para lowercase e vise e versa
# texto = input("Digite um texto: ")
# texto_em_caixa_alta = texto.swapcase()
# print("Texto em caixa alta:", texto_em_caixa_alta)

from PyQt5 import uic, QtWidgets

def caixaAlta():
    texto = editor.lineEdit.text()
    texto_em_caixa_alta = texto.upper()
    
    editor.lineEdit.clear()
    
    editor.lineEdit.setText(texto_em_caixa_alta)

def caixaBaixa():
    texto = editor.lineEdit.text()
    texto_em_caixa_alta = texto.lower()
    
    editor.lineEdit.clear()
    
    editor.lineEdit.setText(texto_em_caixa_alta)

def limpar():
    editor.lineEdit.clear()


app = QtWidgets.QApplication([])
editor = uic.loadUi("editor.ui")
editor.btn_caixaAlta.clicked.connect(caixaAlta)
editor.btn_caixaBaixa.clicked.connect(caixaAlta)
editor.btn_limpar.clicked.connect(limpar)

editor.show()
app.exec()