from pathlib import Path
import os

def create_file(file_name, extension):
    if os.path.isfile(f"{file_name}.{extension}"):
        return "Такой файл уже существует в этой директории"
    else:
        my_file = open(f"{file_name}.{extension}", 'w')
        my_file.close()
        return (Path(f"{file_name}.{extension}").absolute())