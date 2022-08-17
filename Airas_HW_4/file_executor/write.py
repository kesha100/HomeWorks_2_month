from pathlib import Path
import os

def write_to_file(file, body):
    if os.path.isfile(f"{file}"):
        with open(f'{file}', 'w', encoding='UTF-8') as file_:
            file_.write(f"{body}")
            file_.close()
    else:
        print(f"Файла {file} не существует")