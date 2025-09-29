from stats import get_num_words
from stats import count_characters

def main():
    print (get_num_words(get_book_text("books/frankenstein.txt")))
    print (count_characters(get_book_text("books/frankenstein.txt")))
  

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

    
main()
