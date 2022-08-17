from pathlib import Path
import os

def delete_file(file):
    if os.path.isfile(f"{file}"):
        os.remove(f"{file}")
        return f"Файл {file} успешно удален!!!"
    else:
        return f"Файла {file} не существует"