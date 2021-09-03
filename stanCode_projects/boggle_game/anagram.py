"""
File: anagram.py
Name: Iris
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# global variable
dic = []                      # a list to save all the vocabularies in FILE


def main():
    """
    User can input a word and the program will find out all the anagrams
    """
    read_dictionary()
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    while True:
        s = input('Find anagrams for:')
        start = time.time()
        if s == EXIT:
            break
        elif len(s) == 0:                       # the user does not enter any word
            s = input('Find anagrams for:')
            start = time.time()
        else:
            find_anagrams(s)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    list all the data in FILE
    """
    # global dic
    with open(FILE, 'r') as f:
        for line in f:
            voc = line.split()
            dic.append(voc[0])


def find_anagrams(s):
    """
    :param s: str,the word user enters
    """
    words = []                                  # save all the anagrams we found
    print('Searching...')
    find_anagrams_helper(s, "", words)
    print(f'{len(words)} anagrams:{words}')


def find_anagrams_helper(s, word, words):
    """
    :param s: str,the word user enters
    :param word: str,a anagram we found
    :param words: lst,all the anagrams we found
    """
    if word in words:                       # the word is already found
        pass
    elif len(word) == len(s):               # check whether the word is in dictionary
        if word in dic:
            words.append(word)
            print('Found:' + word)
            print('Searching...')
    else:
        for ch in s:
            if word.count(ch) >= s.count(ch):
                pass
            else:
                # choose
                word += ch
                # explore
                if has_prefix(word) is True:
                    find_anagrams_helper(s, word, words)
                # un-choose
                word = word[0:-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, the vocabulary we are going to search
    :return: boolean, return whether the dic has the word starts from sub_s
    """
    for word in dic:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
