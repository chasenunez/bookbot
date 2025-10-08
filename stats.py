def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return(file_contents)

def count_words(file_contents):
        num_words = len(file_contents.split())
        msg = f"Found {num_words} total words"
        return msg

def count_letters(file_contents):
	small_letters = list(file_contents.lower())
	letters = dict()
	for letter in small_letters:
  		letters[letter] = letters.get(letter, 0) + 1
	return(letters)
