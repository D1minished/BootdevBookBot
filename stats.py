def get_word_count(book_text):
    word_array = book_text.split()
    return len(word_array)

def get_char_count(book_text):
    chars_found = {}
    
    for char in book_text:
        lower_char = char.lower()
        if lower_char in chars_found:
            chars_found[lower_char] += 1
        else:
            chars_found[lower_char] = 1
            
    return chars_found

def sort_on(dict):
    return dict["times"]

def sort_list(char_dict):
    list_to_sort = []
    for key in char_dict:
        list_to_sort.append({
            "char": key,
            "times": char_dict[key]
        })
    list_to_sort.sort(reverse=True, key=sort_on)
    return list_to_sort
    
        