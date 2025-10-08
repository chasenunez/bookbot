## BookBot

BookBot is a simple Python tool that ingests a text file of a book and outputs key statistics about its composition — including total word count and a ranked frequency of letters. It’s a quick way to explore how language patterns differ between literary works.

### What It Does

BookBot performs the following:

1. **Reads** a book text file (e.g., `frankenstein.txt`).
2. **Counts** total words in the text.
3. **Counts** how many times each letter appears (case-insensitive).
4. **Sorts and displays** letters in descending order of frequency.

### Project Structure

```
bookbot/
├── main.py         # Entry point for the script
├── stats.py        # Helper functions for counting and ordering
└── books/          # Folder containing example .txt books
```

### How to Use

#### 1. Clone the Repository

```bash
git clone https://github.com/chasenunez/bookbot.git
cd bookbot
```

#### 2. Add Some Books

Place plain-text `.txt` files into a folder named `books/`.
You can download free public-domain books from [Project Gutenberg](https://www.gutenberg.org/).

#### 3. Run BookBot

```bash
python3 main.py books/frankenstein.txt
```

#### 4. Example Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
...
============= END ===============
```

### Example Results from Classic Novels

* Across all three novels, **“e”** is by far the most common letter.
* The relative frequency of letters tends to follow general English patterns (ETAOIN SHRDLU).
* *Frankenstein* and *Pride and Prejudice* both contain around **75k–130k words**, much smaller than *Moby-Dick*’s massive **215k+ words**.
