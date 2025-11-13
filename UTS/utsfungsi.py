import os

def create_directory(directory):
    os.makedirs(directory, exist_ok=True)  # aman bikin folder

def write_to_file(path, data):
    with open(path, 'a', encoding='utf-8') as file:  # tambah encoding
        file.write(data + '\n')

def read_data(path, limit):
    with open(path, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if count == limit:
                break
            if line.strip() == "":
                continue
            count += 1
            print(line.strip())

def does_file_exist(path):
    return os.path.isfile(path)

def remove_file(path):
    if does_file_exist(path):
        os.remove(path)
