"""
File: complement.py
Name:Iris Chen
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    User can enter any dna, and the program will find the complement.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()
    # make all the letters in upper classes
    print("The complement of "+dna + " is "+build_complement(dna))


def build_complement(dna):
    """
    find the complement
    :return: string, the complement of dna
    """
    ans = ""
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
