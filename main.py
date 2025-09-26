import sys

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:
	bookpath = sys.argv[1]

from stats import (
	wordcount,
	charcount,
	sortcount
)

def main():
	text = get_book_text(bookpath)
	word_num = wordcount(text)
	char_num = charcount(text)
	sort_dict = sortcount(char_num)
	report(bookpath, word_num, sort_dict)

def get_book_text(bookpath):
	with open(bookpath) as f:
		return f.read()

def report(book, words, sorted):
	print("Bookbot.py")
	print("Version 3.13")
	print(f"Beginning Bookbot functions for {book}")
	print("===============================")
	print("WORD COUNT:")
	print(f"Found {words} total words.")
	print("===============================")
	print("CHARACTER COUNT:")
	for item in sorted:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")

	print("========REPORT COMPLETE========")
main()
