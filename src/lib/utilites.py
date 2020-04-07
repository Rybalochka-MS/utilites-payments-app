# Read file from file path to buffer
def read_file(filepath):
    file = open(filepath, 'r')
    buf = file.read()
    file.close()
    return buf
