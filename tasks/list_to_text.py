import fitz  # PyMuPDF
import json


def generate_toc_json(pdf_path, json_path):
    # Load the PDF
    pdf = fitz.open(pdf_path)
    toc_structure = {}
    current_chapter_num = None
    current_section = None
    current_subsection = None

    # Extract TOC from PDF
    toc = pdf.get_toc()

    for entry in toc:
        level, title, page = entry

        # Handle Level 1 (chapters) without writing them to JSON
        if level == 1:
            current_chapter_num = str(len(toc_structure) + 1)
            current_section = None  # Reset section and subsection for new chapter
            current_subsection = None
            continue  # Do not add chapter titles to JSON

        # Handle Level 2: Main sections under each chapter
        elif level == 2 and current_chapter_num:
            toc_structure[current_chapter_num] = {
                "title": title, "sections": {}}
            current_section = toc_structure[current_chapter_num]["sections"]

        # Handle Level 3: Subsections within main sections
        elif level == 3 and current_section is not None:
            subsection_num = f"{current_chapter_num}.{
                len(current_section) + 1}"
            current_section[subsection_num] = {
                "title": title, "subsections": {}}
            current_subsection = current_section[subsection_num]["subsections"]

        # Handle Level 4 and deeper: Nested subsections within Level 3 subsections
        elif level >= 4 and current_subsection is not None:
            nested_num = f"{subsection_num}.{len(current_subsection) + 1}"
            current_subsection[nested_num] = {
                "title": title, "subsections": {}}

    # Save the final JSON structure
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(toc_structure, f, ensure_ascii=False, indent=4)

    pdf.close()
    print(f"Table of contents saved to {json_path}")


# Paths for input and output files
pdf_path = r"J:\Books\Data Structures\- Grokking Data Structures - Marcello La Rocca (2024).pdf"
json_path = r"C:\Users\STC\Downloads\grokking.json"

# Execute the function
generate_toc_json(pdf_path, json_path)


# ------ 3rd old try --------

# import fitz  # PyMuPDF
# import json


# def generate_toc_json(pdf_path, json_path):
#     # Load the PDF
#     pdf = fitz.open(pdf_path)
#     toc_structure = {}
#     stack = []  # Stack to keep track of the current path in the JSON structure
#     # Track if the current chapter has sections
#     current_chapter_has_sections = False

#     # Extract TOC from PDF
#     toc = pdf.get_toc()

#     for entry in toc:
#         level, title, page = entry

#         # Step 1: Handle Level 1 (chapter)
#         if level == 1:
#             # Check if the previous chapter had any sections to write
#             if current_chapter_has_sections:
#                 current_chapter_has_sections = False  # Reset for the new chapter
#             else:
#                 stack = []  # Clear stack to ignore empty chapter sections

#             continue  # Do not add Level 1 title to JSON

#         # Level 2: Main sections to be added in JSON if chapter has sections
#         if level == 2:
#             current_chapter_has_sections = True  # Mark that this chapter has sections
#             section_num = str(len(toc_structure) + 1)
#             toc_structure[section_num] = {"title": title, "sections": {}}
#             stack.append((toc_structure, section_num, "sections"))

#         # Level 3: Subsections within Level 2 sections
#         elif level == 3 and stack:
#             parent = stack[-1][0][stack[-1][1]]["sections"]
#             subsection_num = f"{stack[-1][1]}.{len(parent) + 1}"
#             parent[subsection_num] = {"title": title, "subsections": {}}
#             stack.append((parent, subsection_num, "subsections"))

#         # Level 4 and deeper: Nested subsections within Level 3 sections
#         elif level >= 4 and stack:
#             parent = stack[-1][0][stack[-1][1]][stack[-1][2]]
#             nested_num = f"{stack[-1][1]}.{len(parent) + 1}"
#             parent[nested_num] = {"title": title, "subsections": {}}
#             stack.append((parent, nested_num, "subsections"))

#     # Save the final JSON structure
#     with open(json_path, "w", encoding="utf-8") as f:
#         json.dump(toc_structure, f, ensure_ascii=False, indent=4)

#     pdf.close()
#     print(f"Table of contents saved to {json_path}")


# # Paths for input and output files
# pdf_path = r"J:\Books\Data Structures\- Grokking Data Structures - Marcello La Rocca (2024).pdf"
# json_path = r"C:\Users\STC\Downloads\grokking.json"


# # Execute the function
# generate_toc_json(pdf_path, json_path)


# ------ 2nd old try --------
# import json
# import fitz  # PyMuPDF
# import pymupdf


# def extract_toc_to_dict(pdf_path):
#     # Open file (PDF)
#     pdf_file = open(pdf_path,  'r', encoding="utf-8")
#     doc = fitz.open(pdf_file)  # fitz.open(pdf_path)

#     # Extract the TOC
#     toc = doc.get_toc()

#     # Initialize the dictionary to hold the TOC
#     toc_dict = {}

#     # for item in toc:
#     for i, item in enumerate(toc):
#         # print(item)
#         level, title, page_num = item

#         if level == 1:
#             # This is a chapter
#             # continue
#             current_chapter = str(len(toc_dict) + 1)
#             toc_dict[current_chapter] = {"title": title, "sections": {}}
#             # if (toc_dict[current_chapter]['sections'] == {}):
#             #     toc_dict.pop(current_chapter)
#             #     continue
#             # print(toc_dict[current_chapter]['sections'] == {})
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


# def save_toc_as_json(toc_dict, output_path):
#     with open(output_path, 'w', encoding='utf-8') as f:
#         json.dump(toc_dict, f, ensure_ascii=False, indent=4)
#     print(f'TOC saved to {output_path}')


# pdf_path = r"J:\Books\Data Structures\- Grokking Data Structures - Marcello La Rocca (2024).pdf"
# output_path = r"C:\Users\STC\Downloads\grokking.json"

# toc_dict = extract_toc_to_dict(pdf_path)
# save_toc_as_json(toc_dict, output_path)


# # ----- 1st old try ------
# '''
# import json
# import fitz  # PyMuPDF
# import pymupdf


# def generate_toc_json(pdf_path, json_path):
#     # Load the PDF and initialize the TOC structure
#     pdf_file = open(pdf_path,  'r', encoding="utf-8")
#     pdf = pymupdf.open(pdf_file)
#     # toc_structure = {}

#     # Extract TOC from PDF
#     toc = pdf.get_toc()

#     # print(f'toc type: {type(toc)}')
#     # print(f'contents: {toc}')

#     # my_string = ' '.join([str(elem) for elem in toc])
#     # print(my_string)

#     # json_string = json.dumps(toc)
#     json_string = json.dumps(toc, ensure_ascii=False, indent=4)
#     print(json_string)

#     # Save the final structure to the JSON file
#     # with open(json_path, "w", encoding="utf-8") as f:
#     #     json.dump(toc_structure, f, ensure_ascii=False, indent=4)

#     pdf.close()
#     print(f"Table of contents successfully exported")


# # File paths
# # pdf_path = r"C:\Users\STC\Downloads\uz-history.pdf"
# # json_path = r"C:\Users\STC\Downloads\uz_toc.json"

# pdf_path = r"J:\Books\Data Structures\- Grokking Data Structures - Marcello La Rocca (2024).pdf"
# json_path = r"C:\Users\STC\Downloads\grokking.json"

# # Generate the TOC JSON
# generate_toc_json(pdf_path, json_path)
# '''
