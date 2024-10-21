import json
import pymupdf  # imports the pymupdf library

# open a document
# doc = pymupdf.open(r"C:\Users\STC\Downloads\aops-intro-algebra-toc.pdf")
#
# print(f'doc is here : {doc}')

# pdf_file = open(r"C:\Users\STC\Downloads\uz-history.pdf", encoding="utf-8")
# # mode='rb')
# # doc = pymupdf.open(pdf_file)
# toc = doc.get_toc()
# print(toc)

pdf_file = open(
    r"J:\Books\Data Structures\- Grokking Data Structures - Marcello La Rocca (2024).pdf", encoding="utf-8")

doc = pymupdf.open(pdf_file)
toc = doc.get_toc()
print(toc)

# metadata = doc.metadata
# print(metadata)


# for page in doc:  # iterate the document pages
#     text = page.get_text()  # get plain text encoded as UTF-8
#     print(text)
