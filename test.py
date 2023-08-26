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
