"""
File: boggle.py
Name: Iris
----------------------------------------
At the beginning, the user needs to input SIZE rows of letters,
and the program will start to connect the adjacent letters on the letter plate
to find all the words that exist in this SIZE x SIZE square letter platter.
"""

import time
import copy                   # to copy the data in list to a new list


# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

SIZE = 4         # the size of the letter platter


def main():
	"""
	check whether the letters the user input legal.
	If all the letters legal, it will start to find words
	"""
	start = time.time()
	dic = read_dictionary()                 # dictionary
	row_num = 1								# count the times user enters
	row = []								# lst, store the letters the user input
	while row_num <= SIZE:
		user_input = input(str(row_num)+' row of letters: ').lower().split()
		if len(user_input) != SIZE:
			print('Illegal input')
			return
		for i in range(0, SIZE-1):
			if len(user_input[i]) != 1 or user_input[i].isalpha() is False:
				print('Illegal input')
				return
		row.append(user_input)
		row_num += 1
	if len(row) == SIZE:
		find_letters(row, dic)

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_letters(row, dic):
	"""
	:param row: lst, store the letters the user input
	:param dic: dict, dictionary
	"""
	words = [] 							# store the words found
	for x in range(len(row[0])):
		for y in range(len(row)):
			word = ''       			# store the letters which is trying to combine into single word
			new_row = copy.deepcopy(row)
			word += new_row[x][y]		# starting word
			new_row[x][y] = ""			# pop out the letter which has been chosen
			find_letters_helper(new_row, word, dic, x, y, words)
	print('There are '+str(len(words))+' words in total.')


def find_letters_helper(row, word, dic, x, y, words):
	"""
	:param row: lst, store the letters the user input
	:param word: str, store the letters which is trying to combine into single word
	:param dic: dict, dictionary
	:param x: int,  the index in row
	:param y: int, the index in row[x]
	:param words: lst, all the words found
	"""
	if len(word) >= SIZE and word in dic[word[0]] and word not in words:	 	# the word whose length is more than SIZE
		if dic[word[0]][dic[word[0]].index(word)+1].startswith(word):		# keep looking for words longer than SIZE
			print(f'Found \"{word}\"')
			words.append(word)
			find_letters_helper(row, word, dic, x, y, words)
		else:
			print(f'Found \"{word}\"')
			words.append(word)
	else:
		for i in range(x - 1, x + 2):       								# Neighbors on the top and bottom
			for j in range(y - 1, y + 2):									# neighbors on the left and right
				if i < 0 or j < 0 or i >= len(row[x]) or j >= len(row):   	# exclude points that are not in the range
					pass
				elif i == x and j == y:										# repeated letter
					pass
				elif row[i][j] == "":										# letter has been selected
					pass
				else:
					# choose
					word += row[i][j]
					row[i][j] = ""
					old_x = x
					old_y = y
					x = i
					y = j
					# explore
					if has_prefix(word, dic) is True:
						find_letters_helper(row, word, dic, x, y, words)
					# un-choose
					row[x][y] = word[-1]
					word = word[0:-1]
					x = old_x
					y = old_y


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python dictionary
	which sorts by beginning letter.
	"""
	dic = {}
	with open(FILE, 'r') as f:
		for line in f:
			voc = line.strip()
			if len(voc) >= SIZE:
				if voc[0] in dic:
					dic[voc[0]].append(voc)
				else:
					dic[voc[0]] = [voc]
	return dic


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a SIZExSIZE square grid
	:param dic: dict, a dictionary which stores all the data in FILE
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic[sub_s[0]]:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
