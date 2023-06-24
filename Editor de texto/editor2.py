from PyQt5 import uic, QtWidgets

def primeiraMaiuscula():
    texto = editor2.textEdit.toPlainText()
    texto_modificado = texto.capitalize()
    
    editor2.textEdit.clear()
    editor2.textEdit.setText(texto_modificado)

def caixaAlta():
    texto = editor2.textEdit.toPlainText()
    texto_modificado = texto.upper()
    
    editor2.textEdit.clear()
    editor2.textEdit.setText(texto_modificado)

def caixaBaixa():
    texto = editor2.textEdit.toPlainText()
    texto_modificado = texto.lower()
    
    editor2.textEdit.clear()
    editor2.textEdit.setText(texto_modificado)

def removerEspaco():
    texto = editor2.textEdit.toPlainText()
    texto_modificado = texto.strip()
    
    editor2.textEdit.clear()
    editor2.textEdit.setText(texto_modificado)

def limpar():
    editor2.textEdit.clear()


app = QtWidgets.QApplication([])
editor2 = uic.loadUi("editor.ui")
editor2.btn_frase.clicked.connect(primeiraMaiuscula)
editor2.btn_caixaAlta.clicked.connect(caixaAlta)
editor2.btn_caixaBaixa.clicked.connect(caixaBaixa)
editor2.btn_removerEspaco.clicked.connect(removerEspaco)
editor2.btn_limpar.clicked.connect(limpar)

editor2.show()
app.exec()