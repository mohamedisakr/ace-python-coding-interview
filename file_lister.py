from os import listdir

directory_path = r"J:\Videos\Algorithms\Udacity Intro to Computer Science"
files = listdir(directory_path)
print(f'# of files: {len(files)}')
file_names = [fname for fname in files]  # if fname.endswith('.mp4')]
# [file.replace(".mp4", "") for file in files if not ".1." in file]
#
print(f'# of files after processed: {len(file_names)}')
# .split('.')[-2].rstrip()file_names]
# files = [fname for fname in allfiles if fname.endswith('.mp4')]
with open('files-list.txt', 'w', encoding="utf-8") as file:
    for i, v in enumerate((file_names)):
        # Write some text to the file
        # print(file_names[i][0:-4])
        print(file_names[i])
        file.write(f'{v}\n')
