from stats import get_num_words, count_characters, get_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        number_of_words = get_num_words(book_text)

        newDict = count_characters(book_text)

        #print(f"{number_of_words} words found in the document")
        
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count -------")
        sorted_list = get_sorted_list(newDict)
        for s in sorted_list:
            print(f"{s['char']}: {s['num']}")
        print("============= END ===============")
    

main()
