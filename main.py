# opens the file data and reads (saves) it to a variable
from stats import word_count, char_count, sort_dict
import sys

def main():
    # cheching if the sys input is valid
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Getting values and processing data
    file_path = sys.argv[1]
    num_words = word_count(file_path)
    response = f"Found {num_words} total words"

    num_ch = char_count(file_path)
    chars = sort_dict(num_ch)

    # Formatting Char Count
    formatted_char = ""
    for char in chars:
        if char["char"].isalpha():
            formatted_char += f"{char["char"]}: {char["num"]}\n"


    # Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(response)
    print("--------- Character Count -------")
    print(formatted_char + f"============= END ===============")

main()