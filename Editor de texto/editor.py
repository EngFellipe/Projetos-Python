from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog

def primeiraMaiuscula():
    texto = editor.textEdit.toPlainText()
    texto_modificado = texto.capitalize()
    
    editor.textEdit.clear()
    editor.textEdit.setText(texto_modificado)

def caixaBaixa():
    texto = editor.textEdit.toPlainText()
    texto_modificado = texto.lower()
    
    editor.textEdit.clear()
    editor.textEdit.setText(texto_modificado)

def caixaAlta():
    texto = editor.textEdit.toPlainText()
    texto_modificado = texto.upper()
    
    editor.textEdit.clear()
    editor.textEdit.setText(texto_modificado)

def textoAlternado():
    texto = editor.textEdit.toPlainText()

    texto_modificado = ""
    for i in range(len(texto)):
        if i % 2 == 0:  # Se o índice for par
            texto_modificado += texto[i].lower()
        else:  # Se o índice for ímpar
            texto_modificado += texto[i].upper()
    
    editor.textEdit.clear()
    editor.textEdit.setText(texto_modificado)

def removerEspaco():
    texto = editor.textEdit.toPlainText()
    texto_modificado = texto.strip()
    
    editor.textEdit.clear()
    editor.textEdit.setText(texto_modificado)

def tituloCase():
    texto = editor.textEdit.toPlainText()
    texto_modificado = texto.title()
    
    editor.textEdit.clear()
    editor.textEdit.setText(texto_modificado)

def inverseCase():
    texto = editor.textEdit.toPlainText()
    texto_modificado = texto[::-1]
    
    editor.textEdit.clear()
    editor.textEdit.setText(texto_modificado)

def baixar():
    texto = editor.textEdit.toPlainText()

    file_path, _ = QFileDialog.getSaveFileName(None, "Salvar Arquivo", "", "Arquivo de Texto (*.txt)")
    if file_path:
        with open(file_path, "w") as file:
            file.write(texto)

def limpar():
    editor.textEdit.clear()

def contagem():
    texto = editor.textEdit.toPlainText()

    letras = len(texto)
    editor.lbl_letras.setText(str(letras))

    palavras = texto.split()  # Divide o texto em uma lista de palavras
    contar_palavras = len(palavras)
    editor.lbl_palavras.setText(str(contar_palavras)) # Retorna o número de palavras na lista

    linhas = texto.splitlines()
    contar_linhas = len(linhas)
    editor.lbl_linhas.setText(str(contar_linhas))


app = QtWidgets.QApplication([])
editor = uic.loadUi("editor.ui")

editor.btn_frase.clicked.connect(primeiraMaiuscula)
editor.btn_caixaBaixa.clicked.connect(caixaBaixa)
editor.btn_caixaAlta.clicked.connect(caixaAlta)
editor.btn_alternado.clicked.connect(textoAlternado)
editor.btn_removerEspaco.clicked.connect(removerEspaco)
editor.btn_tituloCase.clicked.connect(tituloCase)
editor.btn_inverseCase.clicked.connect(inverseCase)
editor.btn_baixar.clicked.connect(baixar)
editor.btn_limpar.clicked.connect(limpar)

editor.textEdit.textChanged.connect(contagem)

editor.show()
app.exec()