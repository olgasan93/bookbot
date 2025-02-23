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

