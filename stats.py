def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return(file_contents)

def count_letters(file_contents):
        num_words = len(file_contents.split())
        msg = f"Found {num_words} total words"
        return msg
