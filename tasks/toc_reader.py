import json
import fitz  # PyMuPDF
import pymupdf


def extract_toc_to_dict(pdf_path):
    """Extract the table of contents (TOC) from a PDF and structure it into a dictionary.

    Parameters
    ----------
    pdf_path : (str)
        The file location of the PDF

    Returns
    -------
    dict
        A nested dictionary representing the TOC with chapters, sections, and subsections.
    """
    # Open file (PDF)
    pdf_file = open(pdf_path,  'r', encoding="utf-8")
    doc = pymupdf.open(pdf_file)  # fitz.open(pdf_path)

    # Extract the TOC
    toc = doc.get_toc()

    # Initialize the dictionary to hold the TOC
    toc_dict = {}

    for item in toc:
        level, title, page_num = item

        if level == 1:
            # This is a chapter
            current_chapter = str(len(toc_dict) + 1)
            toc_dict[current_chapter] = {"title": title, "sections": {}}
        elif level == 2:
            # This is a section
            current_section = f"{current_chapter}.{
                len(toc_dict[current_chapter]['sections']) + 1}"
            toc_dict[current_chapter]["sections"][current_section] = {
                "title": title, "subsections": {}}
        elif level == 3:
            # This is a subsection
            current_subsection = f"{current_section}.{
                len(toc_dict[current_chapter]['sections'][current_section]['subsections']) + 1}"
            toc_dict[current_chapter]["sections"][current_section]["subsections"][current_subsection] = {
                "title": title}

    return toc_dict


def save_toc_as_json(toc_dict, output_path):
    """Save a nested dictionary representing the table of contents (TOC) to a JSON file.

    Parameters
    ----------
        toc_dict (dict): The TOC dictionary to be saved.
        output_path (str): The file path where the JSON file will be saved.

    Returns
    -------
        None
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(toc_dict, f, ensure_ascii=False, indent=4)
    print(f'TOC saved to {output_path}')


# Example usage
pdf_path = r"C:\Users\STC\Downloads\uz-history.pdf"
# pdf_path = r"C:\Users\STC\Downloads\aops-intro-algebra-toc.pdf"
# pdf_path = r"J:\Books\Data Structures\- Grokking Data Structures - Marcello La Rocca (2024).pdf"
output_path = r"C:\Users\STC\Downloads\output_toc.json"  # 'output_toc.json'

toc_dict = extract_toc_to_dict(pdf_path)
save_toc_as_json(toc_dict, output_path)


# '''
# import pymupdf  # imports the pymupdf library

# # open a document
# doc = pymupdf.open(r"C:\Users\STC\Downloads\aops-intro-algebra-toc.pdf")
# # doc = pymupdf.open(r"C:\Users\STC\Downloads\uz-history.pdf")
# toc = doc.get_toc()
# print(toc)

# # metadata = doc.metadata
# # print(metadata)


# # for page in doc:  # iterate the document pages
# #     text = page.get_text()  # get plain text encoded as UTF-8
# #     print(text)
# '''
