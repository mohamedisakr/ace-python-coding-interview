import os
import re


# Function to rename files in the specified directory

def rename_files(directory):
    # Regular expression pattern to match the file name
    pattern = re.compile(r"Chapter_(\d+)_\.(.+)")

    # Iterate through the files in the directory
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            seq_number = match.group(1)
            file_name = match.group(2)

            # Replace underscores with spaces in the file name
            new_filename = f"{seq_number} Chapter {
                seq_number} {file_name.replace('_', ' ')}"

            # Get the full paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} -> {new_file}")


# Specify the directory containing the files
directory = r"J:\Videos\Algorithms\- Oreilly Grokking Algorithms Second Edition 2024-3 - Copy"

# Call the function to rename files
rename_files(directory)
