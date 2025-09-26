def wordcount(book):
	num_words = book.split()
	return len(num_words)

def charcount(book):
	char_dict = {}
	for char in book:
		lower_chars = char.lower()
		if lower_chars in char_dict:
			char_dict[lower_chars] += 1
		else:
			char_dict[lower_chars] = 1
	return char_dict

def sort_on(d):
	return d["num"]

def sortcount(char_num_dict):
	sort_list = []
	for char in char_num_dict:
		sort_list.append({"char": char, "num": char_num_dict[char]})
	sort_list.sort(reverse=True, key=sort_on)
	return sort_list
