from os import listdir

directory_path = r"J:\Videos\System Design\00 AlgoExpert Systems Design Fundamentals"
files = listdir(directory_path)
print(f'# of files: {len(files)}')
file_names = [file.replace(".mp4", "") for file in files if not ".1." in file]
#
print(f'# of files after processed: {len(file_names)}')
# .split('.')[-2].rstrip()file_names]

with open('files-list.txt', 'w', encoding="utf-8") as file:
    for i, v in enumerate((file_names)):
        # Write some text to the file
        file.write(f'{v}\n')
