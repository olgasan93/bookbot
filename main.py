def main():
    import sys
    from stats import get_book_text
    from stats import word_counter
    from stats import alphabet_counter
    from stats import alphabet_sorter
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        book = get_book_text(f)
        print("----------- Word Count ----------")
        word_counter(book)
        print("--------- Character Count -------")
        alphabet_dict = alphabet_sorter(alphabet_counter(book))
        for a in alphabet_dict:
            if a["character"].isalpha() == True:
                print(f"{a['character']}: {a['count']}")
        print(f"============= END ===============")
main()


    # with open("books/frankenstein.txt") as f:
    #     file_contents = f.read()
    #     words = file_contents.split()
    #     word_number = len(words)
    #     print(f"{word_number} words found in the document")

    #     characters = {}
    #     words = file_contents.lower()
    #     for a in words:
    #         if a not in characters :
    #             characters[a] = 1
    #         else:
    #             characters[a] += 1
        
    #     characters_list = [{"character":key, "count":value} for key,value in characters.items() if key.isalpha() == True]
    #     def sort_on(dict):
    #         return dict["count"]
    #     characters_list.sort(reverse=True, key=sort_on)
    #     for dict in characters_list:
    #         print(f"The '{dict['character']}' character was found {dict['count']} times")




        # characters.sort(reverse= True, key= sort_on)
        # for char in characters:
        #     if char.isalpha() == False:
        #         del characters[char]
        # for char in characters:
        #     print(f"The {char} character was found {characters[char]}times")           