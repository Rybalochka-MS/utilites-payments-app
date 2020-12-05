import os
from src.load_properties import get_url

def read_file(filepath):
    file = open(filepath, "r", encoding="utf-8")
    buffer = file.read()
    file.close()
    return buffer

def write_file(filepath, buffer):
    file = open(filepath, "w", encoding="utf-8")
    file.write(buffer)
    file.close()


def replace_url():
    url = get_url()
    files = os.listdir('src/html/')
    for file in files:
        path = 'src/html/' + file
        buffer = read_file(path)
        buffer = buffer.replace("url", url)
        write_file(path, buffer)
