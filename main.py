import sys
from stats import get_book_text
from stats import count_words
from stats import count_letters 
from stats import order

def main(file):
	text = get_book_text(file)
	words = count_words(text)
	letters = count_letters(text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file}...")
	print("----------- Word Count ----------")
	print(f"{words}")
	print("--------- Character Count -------")
	print(order(letters))
	print("============= END ===============")

if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
else:   
	filepath = sys.argv[1]

main(filepath)
