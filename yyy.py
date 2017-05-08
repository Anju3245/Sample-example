from sys import argv
script,first_file,second_file = argv
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(5)
    in_file = open(first_file):
    print(first_file)
