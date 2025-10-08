## ETANI SHORDUL (BookBot)

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
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```
