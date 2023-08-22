# "Faça um programa em python que leia em uma pasta arquivos pdfs diversos
# procurando uma palavara especifica.
# No final, mostre em quais arquivos estão estas palavras e monte uma lista na tela."
# - Desafios - o número de arquivos pdf não importam.
# - Eu tenho que digitar a palavra que eu quero procurar.

# Desafios Bonus
# - Eu digito qual a pasta que eu quero procurar.
# - A lista pode ser gerada num arquivo TXT.
# imports
import PyPDF2

path = "bitcoin_pt.pdf"
pdf_file = open(path)

data = PyPDF2.PdfFileReader(pdf_file)


"""
def main():
    



def word_search():


main()"""
