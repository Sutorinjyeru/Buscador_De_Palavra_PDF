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


def main():
    zetto = input("Digite o caminho da pasta: ")
    word = input("Digite a palavra desejada: ")
    paths = os.listdir(rf'{zetto}')
    for i in paths:
        if i.endswith('.pdf'):
            word_search(word, i)


def word_search(word, pdf):
    reader = PyPDF2.PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    print("tem: " + pdf) if word in text else print("Não tem:" + pdf)


main()
