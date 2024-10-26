import json
import fitz  # PyMuPDF
import pymupdf


def generate_toc_json(pdf_path, json_path):
    # Load the PDF and initialize the TOC structure
    pdf_file = open(pdf_path,  'r', encoding="utf-8")
    pdf = pymupdf.open(pdf_file)
    # toc_structure = {}

    # Extract TOC from PDF
    toc = pdf.get_toc()

    print(f'toc type: {type(toc)}')
    my_string = ' '.join([str(elem) for elem in toc])
    print(my_string)

    # print(f'contents: {toc}')

    # Save the final structure to the JSON file
    # with open(json_path, "w", encoding="utf-8") as f:
    #     json.dump(toc_structure, f, ensure_ascii=False, indent=4)

    pdf.close()
    print(f"Table of contents successfully exported")


# File paths
# pdf_path = r"C:\Users\STC\Downloads\uz-history.pdf"
pdf_path = r"J:\Books\Data Structures\- Grokking Data Structures - Marcello La Rocca (2024).pdf"
json_path = r"C:\Users\STC\Downloads\uz_toc.json"

# Generate the TOC JSON
generate_toc_json(pdf_path, json_path)
