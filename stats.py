#stats.py

#returns the number of words in a string
def get_num_words(book_text):
    list_of_words = book_text.split()
    return len(list_of_words)

#reads in a book and returns the text as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#counts the number of characters in a book and returns a dictionary with the character as the key and the number of times it appears as the value 
def count_characters(book_text):
    character_count_dict = {}
    for i in book_text.lower():
        if i not in character_count_dict:
            character_count_dict[i] = 1
        else:
            character_count_dict[i] += 1

    return character_count_dict

#takes a dictionary and returns a list of dictionaries
def make_list_of_dictionaries(dictionary):
    list_of_dict=[]
    for i in (dictionary):
        list_of_dict.append({"char": i,"num": dictionary[i]})
    return list_of_dict

def sort_helper(list_of_dict):
    return list_of_dict["num"]

#takes a list of dictionaries and sorts it by the value in descending order
def sort_list_of_dictionaries(list_of_dict):
    list_of_dict.sort(key=sort_helper, reverse=True)
    return list_of_dict

