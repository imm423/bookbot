def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import word_counter, char_counter, char_sort

def main():
    import sys
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    char_dictionary = {}
    sorted_char_list = []
    book = sys.argv[1]
    book_contents = get_book_text(book)
    num_words = word_counter(book_contents)
    char_dictionary = char_counter(book_contents)
    sorted_char_list = char_sort(char_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        if i["char"].isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()

    