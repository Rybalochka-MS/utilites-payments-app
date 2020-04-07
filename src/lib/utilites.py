# Read file from file path to buffer
def read_file(filepath):
    file = open(filepath, 'r', encoding='utf-8')
    buf = file.read()
    file.close()
    return buf
