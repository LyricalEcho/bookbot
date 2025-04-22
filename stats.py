def get_num_words(file_contents):
    words_list = file_contents.split()
    num_words = len(words_list)
    return f"Found {num_words} total words"

def count_characters(file_contents):
    file_contents = file_contents.lower()
    char_count = {}
    for char in file_contents:
        # if key exists already
        if char in char_count:
            char_count.update({char: char_count[char] + 1})
        # Add key if not in dict
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def get_sorted_list_of_dicts(char_dict):
    sorted_list = []
    for key in char_dict:
        sorted_list.append({"char": key, "num": char_dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

