from os import listdir
from typing import List
from pathlib import Path


def list_video_names(directory_path: str) -> List[str]:
    # Define common video extensions
    video_extensions = {'.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'}

    # Create a Path object
    path = Path(directory_path)

    # Check if the directory exists to avoid errors
    if not path.is_dir():
        return "Invalid directory path."

    # Use a list comprehension to find files and grab their 'stem' (name without extension)
    video_names = [
        file.stem for file in path.iterdir()
        if file.suffix.lower() in video_extensions
    ]

    return video_names


# Example usage:
video_names = list_video_names(r"J:\Videos\Calculus\TTC Mathematics Describing the Real World Precalculus and Trigonometry")
for vid_name in video_names:
    print(vid_name)


# directory_path = r"J:\Videos\Algorithms\Udacity Intro to Computer Science"
# files = listdir(directory_path)
# print(f'# of files: {len(files)}')
# file_names = [fname for fname in files]  # if fname.endswith('.mp4')]
# # [file.replace(".mp4", "") for file in files if not ".1." in file]
# #
# print(f'# of files after processed: {len(file_names)}')
# # .split('.')[-2].rstrip()file_names]
# # files = [fname for fname in allfiles if fname.endswith('.mp4')]
# with open('files-list.txt', 'w', encoding="utf-8") as file:
#     for i, v in enumerate((file_names)):
#         # Write some text to the file
#         # print(file_names[i][0:-4])
#         print(file_names[i])
#         file.write(f'{v}\n')
