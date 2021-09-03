"""
File: caesar.py
Name:Iris Chen
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    User enters a number and a ciphered string, the program prints out the answer.
    """
    secret_num = int(input('Secret number: '))
    ciphered_string = input("What's the ciphered string? ")
    ciphered_string = ciphered_string.upper()
    print("The deciphered string is: " + deciphered(secret_num, ciphered_string))


def deciphered(secret_num, ciphered_string):
    """
    This function find the sort of alphabet after encryption,
    and figure out the real message the user sent.
    :return: string, the deciphered string
    """
    deciphered_string = ""
    for i in range(len(ciphered_string)):
        if ciphered_string[i].isalpha():
            alphabet = ALPHABET.find(ciphered_string[i])
            # find which alphabet ciphered_string[i] is
            new_alphabet = alphabet + secret_num
            # shift the alphabet
            while new_alphabet > (len(ALPHABET)-1):
                # the new alphabet wrap around
                new_alphabet -= len(ALPHABET)
            deciphered_string += ALPHABET[new_alphabet]
        else:
            # if ciphered_string[i] is not an alphabet, just print it out without decipher
            deciphered_string += ciphered_string[i]
    return deciphered_string

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
