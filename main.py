def main(file = "books/frankenstein.txt"):
	text = get_book_text(file)
	msg = count_letters(text)
	print(msg)

main()
