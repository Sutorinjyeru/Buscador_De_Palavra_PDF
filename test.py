# import packages
import re

import PyPDF2

# open the pdf file
reader = PyPDF2.PdfReader("bitcoin_pt.pdf")

# define key terms

# extract text and do the search


def word_search(word, pdf):
    find = []
    found = []
    reader = PyPDF2.PdfReader(pdf)
    for page in reader.pages:
        text = page.extract_text()
        # print(text)
        res_search = re.search(word, text)
        find.append(res_search)
        for i in find:
            if i == word:
                found.append(i)
    print(len(find))
    print(len(found))


word_search("Uma", "bitcoin_pt.pdf")
