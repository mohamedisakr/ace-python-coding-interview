import os
import re


def clean_filename(filename):
    # Remove the trailing timestamp
    filename = re.sub(r'-\d{2}-\d{2}-\d{2}$', '', filename)
    # Replace hyphens with spaces
    filename = filename.replace('-', ' ')
    # Capitalize each word
    filename = filename.title()
    return filename


def rename_files(directory):
    for filename in os.listdir(directory):
        # Split filename and extension
        file_root, file_ext = os.path.splitext(filename)
        # Clean up the filename
        clean_name = clean_filename(file_root)
        # Form the new filename
        new_name = f"{clean_name}{file_ext}"
        # Rename the file
        os.rename(os.path.join(directory, filename),
                  os.path.join(directory, new_name))
        print(f"Renamed: {filename} -> {new_name}")


# Provide the directory containing your files
directory_path = r'J:\Videos\Algorithms\00 Back To Back SWE Coding Interview Class'
rename_files(directory_path)
