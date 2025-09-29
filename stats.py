def get_num_words(book_text):
    list_of_words = book_text.split()
    return len(list_of_words)

def count_characters(book_text):
    character_count_dict = {}
    for i in book_text.lower():
        if i not in character_count_dict:
            character_count_dict[i] = 1
        else:
            character_count_dict[i] += 1

    return character_count_dict
        
        