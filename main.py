import sys
from stats import get_num_words, count_characters, get_sorted_list_of_dicts

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    num_words = get_num_words(file_contents)
    char_count = count_characters(file_contents)
    sorted_list = get_sorted_list_of_dicts(char_count)

    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for dict in sorted_list:
        character = dict['char']
        number = dict['num']
        if character.isalpha():
            print(f"{character}: {number}")
    print("============= END ===============")

main()