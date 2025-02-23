def get_book_text(filepath):
    file_contents = filepath.read()
    return file_contents

def word_counter(book_string):
    words = book_string.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def alphabet_counter(book_string):
    alphabets = {}
    book_alphabet = book_string.lower()
    for char in book_alphabet:
        if char not in alphabets:
            alphabets[char] = 1
        else:
            alphabets[char] += 1
    return alphabets

def alphabet_sorter(dict):
    #Convert dictionary into sorted list of dictionaries
    alphabet_list = [{"character":key, "count":value} for key,value in dict.items()]
    
    def sort_on(dict):
        return dict["count"]
    
    alphabet_list.sort(reverse=True, key=sort_on)
    return alphabet_list
    print(alphabet_list)


