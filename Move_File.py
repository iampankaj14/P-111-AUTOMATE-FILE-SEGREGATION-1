import os 
import shutil

from_dir = "C:/Users/panka/Downloads"
to_dir = "C:/Users/panka/OneDrive/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    if ext == "":
        continue