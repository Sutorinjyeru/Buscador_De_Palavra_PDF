# "Faça um programa em python que leia em uma pasta arquivos pdfs diversos
# procurando uma palavara especifica.
# No final, mostre em quais arquivos estão estas palavras e monte uma lista na tela."
# - Desafios - o número de arquivos pdf não importam.
# - Eu tenho que digitar a palavra que eu quero procurar.

# Desafios Bonus
# - Eu digito qual a pasta que eu quero procurar.
# - A lista pode ser gerada num arquivo TXT.
# imports
import os

import PyPDF2


# Programa principal
def main():
    result = []
    zetto = input("Digite o caminho da pasta: ")
    word = input("Digite a palavra desejada: ")
    paths = os.listdir(rf'{zetto}')
    for i in paths:
        if i.endswith('.pdf'):
            with open("Resultado.txt", "w") as arquivo:
                arquivo.write("\n".join(word_search(word, i, result)))

# Função de busca de palavras
def word_search(word=str, pdf=str, have=list):
    reader = PyPDF2.PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    have.append(pdf) if word.lower() in text.lower() else None
    return have


main()
