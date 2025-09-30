import sys
from stats import get_num_words
from stats import count_characters
from stats import get_book_text
from stats import count_characters
from stats import make_list_of_dictionaries
from stats import sort_helper
from stats import sort_list_of_dictionaries

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    list_of_characters = count_characters(text)
    list_of_dict = make_list_of_dictionaries(list_of_characters)
    sorted_list = sort_list_of_dictionaries(list_of_dict)
    num_words = get_num_words(text)
    num_characters = count_characters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        ch = item["char"]
        cnt = item["num"]
        if ch.isalpha():
            print(f"{ch}: {cnt}")
    print("============= END ===============")



    
main()
