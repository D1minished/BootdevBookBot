from stats import get_word_count, get_char_count, sort_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    print(sys.argv)
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    frankenstein_path = sys.argv[1]
    frankenstein_book = get_book_text(frankenstein_path)
    frankenstein_word_count = get_word_count(frankenstein_book)
    frankenstein_character_dict = get_char_count(frankenstein_book)
    frankenstein_sorted_character_dict = sort_list(frankenstein_character_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frankenstein_path}...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_word_count} total words")
    print("--------- Character Count -------")
    for char_dict in frankenstein_sorted_character_dict:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["times"]}")
    print("============= END ===============")

main()