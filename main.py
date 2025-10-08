from stats import get_book_text
from stats import count_words
from stats import count_letters 
from stats import order

def main(file = "books/frankenstein.txt"):
	text = get_book_text(file)
	words = count_words(text)
	letters = count_letters(text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file}...")
	print("----------- Word Count ----------")
	print(f"{words}")
	print("--------- Character Count -------")
	ordered_list = order(letters)
	print("============= END ===============")

main()
