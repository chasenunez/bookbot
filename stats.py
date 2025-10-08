def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return file_contents

def count_words(file_contents):
        num_words = len(file_contents.split())
        msg = f"Found {num_words} total words"
        return msg

def count_letters(file_contents):
	small_letters = list(file_contents.lower())
	letter_counts = dict()
	for letter in small_letters:
		if letter.isalpha():
			letter_counts[letter] = letter_counts.get(letter, 0) + 1
		else:
			continue

	return letter_counts

def order(letter_counts):
	ordered_letters = dict(sorted(letter_counts.items(), key=lambda item:item[1], reverse = True))
	for entry in ordered_letters:
                print(f"{entry}: {ordered_letters[entry]}")
