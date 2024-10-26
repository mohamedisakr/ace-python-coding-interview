import json
import fitz  # PyMuPDF
import pymupdf


def generate_toc_json(pdf_path, json_path):
    # Load the PDF and initialize the TOC structure
    pdf_file = open(pdf_path,  'r', encoding="utf-8")
    pdf = pymupdf.open(pdf_file)
    toc_structure = {}

    # Extract TOC from PDF
    toc = pdf.get_toc()

    print(f'toc type: {type(toc)}')
    # print(f'contents: {toc}')
    # print(toc)

    # Trackers for section, subsection, and sub-subsection
    current_main_section = None
    current_subsection = None
    current_sub_subsection = None

    # Parse through each TOC entry and build the structure
    for entry in toc:
        level, title, page = entry
        section_entry = {"title": title, "sections": {}, "subsections": {}}

        # Level 1: Main sections
        if level == 1:
            main_section_num = str(len(toc_structure) + 1)
            toc_structure[main_section_num] = {"title": title, "sections": {}}
            current_main_section = main_section_num
            current_subsection = None  # Reset lower levels
            current_sub_subsection = None

        # Level 2: Subsections of the main sections
        elif level == 2 and current_main_section:
            subsection_num = f"{current_main_section}.{
                len(toc_structure[current_main_section]['sections']) + 1}"
            toc_structure[current_main_section]["sections"][subsection_num] = {
                "title": title, "subsections": {}}
            current_subsection = subsection_num
            current_sub_subsection = None

        # Level 3: Sub-subsections within Level 2 subsections
        elif level == 3 and current_subsection:
            sub_subsection_num = f"{current_subsection}.{len(
                toc_structure[current_main_section]['sections'][current_subsection]['subsections']) + 1}"
            toc_structure[current_main_section]["sections"][current_subsection]["subsections"][sub_subsection_num] = {
                "title": title}

    # Save the final structure to the JSON file
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(toc_structure, f, ensure_ascii=False, indent=4)

    pdf.close()
    print(f"Table of contents successfully saved to {json_path}")


# File paths
pdf_path = r"C:\Users\STC\Downloads\uz-history.pdf"
json_path = r"C:\Users\STC\Downloads\uz_toc.json"

# Generate the TOC JSON
generate_toc_json(pdf_path, json_path)


# import fitz  # PyMuPDF
# import json


# def generate_toc_json(pdf_path, json_path):
#     # Load the PDF
#     pdf = fitz.open(pdf_path)
#     toc_structure = {}
#     stack = []  # Stack to keep track of the current path in the JSON structure

#     # Extract TOC from PDF
#     toc = pdf.get_toc()

#     for entry in toc:
#         level, title, page = entry

#         # Step 1: Skip Level 1 (chapter) without writing it to JSON
#         if level == 1:
#             stack = []  # Clear the stack for a new chapter
#             continue  # Do not add the chapter to JSON structure

#         # Navigate through the stack to the current level
#         while len(stack) >= level - 1:
#             stack.pop()  # Step up in the hierarchy as needed

#         # Build the current section number (e.g., "2", "2.1", "2.1.1")
#         if level == 2:
#             section_num = str(len(toc_structure) + 1)
#             toc_structure[section_num] = {"title": title, "sections": {}}
#             stack.append((toc_structure, section_num, "sections"))

#         elif level == 3:
#             parent = stack[-1][0][stack[-1][1]]["sections"]
#             subsection_num = f"{stack[-1][1]}.{len(parent) + 1}"
#             parent[subsection_num] = {"title": title, "subsections": {}}
#             stack.append((parent, subsection_num, "subsections"))

#         elif level >= 4:
#             parent = stack[-1][0][stack[-1][1]][stack[-1][2]]
#             nested_num = f"{stack[-1][1]}.{len(parent) + 1}"
#             parent[nested_num] = {"title": title, "subsections": {}}
#             stack.append((parent, nested_num, "subsections"))

#     # Write the final JSON structure
#     with open(json_path, "w", encoding="utf-8") as f:
#         json.dump(toc_structure, f, ensure_ascii=False, indent=4)

#     pdf.close()
#     print(f"Table of contents saved to {json_path}")


# # Paths for input and output files
# pdf_path = r"C:\Users\STC\Downloads\uz-history.pdf"
# json_path = r"C:\Users\STC\Downloads\uz_toc.json"

# # Execute the function
# generate_toc_json(pdf_path, json_path)
