

def import_data(file):
    with open(file, 'r') as books:
        read_books = books.readlines()
        print(read_books)

import_data("test_this_file.txt")
