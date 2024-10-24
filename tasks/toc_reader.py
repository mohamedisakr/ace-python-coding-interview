import json
import fitz  # PyMuPDF
import pymupdf


def extract_toc_to_dict(pdf_path):
    # Open the PDF file
    pdf_file = open(pdf_path,  'r', encoding="utf-8")
    doc = pymupdf.open(pdf_file)  # fitz.open(pdf_path)

    # Extract the TOC
    toc = doc.get_toc()

    # Initialize the dictionary to hold the TOC
    toc_dict = {}
    section_counter = 0
    current_section = None

    for item in toc:
        level, title, page_num = item

        if level == 1:
            # Skip chapter levels
            continue
        elif level == 2:
            # Count sections continuously
            section_counter += 1
            current_section = str(section_counter)
            toc_dict[current_section] = {"title": title, "subsections": {}}
        elif level == 3 and current_section is not None:
            # Count subsections within their sections
            subsection_key = f"{current_section}.{
                len(toc_dict[current_section]['subsections']) + 1}"
            toc_dict[current_section]['subsections'][subsection_key] = {
                "title": title}

    return toc_dict


# def save_toc_as_json(toc_dict, output_path):
#     with open(output_path, 'w', encoding='utf-8') as f:
#         json.dump(toc_dict, f, ensure_ascii=False, indent=4)


# # Example usage
# pdf_path = 'path_to_your_book.pdf'
# output_path = 'output_toc.json'

# toc_dict = extract_toc_to_dict(pdf_path)
# save_toc_as_json(toc_dict, output_path)

# print(f'TOC extracted and saved to {output_path}')


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

"""
first version of function that with a lot of anomalies and a slightly incorrect structure
"""


# def extract_toc_to_dict(pdf_path):
#     '''Extract the table of contents (TOC) from a PDF and structure it into a dictionary.

#     Parameters
#     ----------
#     pdf_path : (str)
#         The file location of the PDF

#     Returns
#     -------
#     dict
#         A nested dictionary representing the TOC with chapters, sections, and subsections.
#     '''
#     # Open file (PDF)
#     pdf_file = open(pdf_path,  'r', encoding="utf-8")
#     doc = pymupdf.open(pdf_file)  # fitz.open(pdf_path)

#     # Extract the TOC
#     toc = doc.get_toc()

#     # Initialize the dictionary to hold the TOC
#     toc_dict = {}

#     for item in toc:
#         level, title, page_num = item

#         if level == 1:
#             # This is a chapter
#             current_chapter = str(len(toc_dict) + 1)
#             toc_dict[current_chapter] = {"title": title, "sections": {}}
#         elif level == 2:
#             # This is a section
#             current_section = f"{current_chapter}.{
#                 len(toc_dict[current_chapter]['sections']) + 1}"
#             toc_dict[current_chapter]["sections"][current_section] = {
#                 "title": title, "subsections": {}}
#         elif level == 3:
#             # This is a subsection
#             current_subsection = f"{current_section}.{
#                 len(toc_dict[current_chapter]['sections'][current_section]['subsections']) + 1}"
#             toc_dict[current_chapter]["sections"][current_section]["subsections"][current_subsection] = {
#                 "title": title}

#     return toc_dict
