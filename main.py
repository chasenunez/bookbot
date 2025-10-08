from stats import get_book_text
from stats import count_words
from stats import count_letters 

def main(file = "books/frankenstein.txt"):
	text = get_book_text(file)
	msg = count_letters(text)
	letters = count_letters(text)
	print (msg)
	print (letters)

main()
