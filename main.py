def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_number = len(words)
        print(f"{word_number} words found in the document")

        characters = {}
        words = file_contents.lower()
        for a in words:
            if a not in characters :
                characters[a] = 1
            else:
                characters[a] += 1
        
        characters_list = [{"character":key, "count":value} for key,value in characters.items() if key.isalpha() == True]
        def sort_on(dict):
            return dict["count"]
        characters_list.sort(reverse=True, key=sort_on)
        for dict in characters_list:
            print(f"The '{dict['character']}' character was found {dict['count']} times")




        # characters.sort(reverse= True, key= sort_on)
        # for char in characters:
        #     if char.isalpha() == False:
        #         del characters[char]
        # for char in characters:
        #     print(f"The {char} character was found {characters[char]}times")
        
    
        
main()