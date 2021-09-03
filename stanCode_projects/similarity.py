"""
File: similarity.py
Name: Iris Chen
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The user will enter a long sequence and a short sequence,
    then the program will print the best match sequence.
    """
    long_sequence = input("Please give me a DNA sequence to search: ")
    long_sequence = long_sequence.upper()
    short_sequence = input("What DNA sequence would you like to match? ")
    short_sequence = short_sequence.upper()
    print("The best match is "+homology(long_sequence, short_sequence))


def homology(long_sequence, short_sequence):
    """
    This function compares short sequence with long sequence
    :return: string, the similar sequence
    """
    count = 0
    # use to count how many alphabets are same as short sequence
    max_sequence = ""
    maximum = count
    for i in range(len(long_sequence)):
        test = long_sequence[i:i+len(short_sequence)]
        # test every sequence
        if len(test) == len(short_sequence):
            for j in range(len(short_sequence)):
                # test every letters in the sequence
                if test[j] in short_sequence[j]:
                    count += 1
            if count > maximum:
                # find the most similar sequence
                maximum = count
                max_sequence = long_sequence[i:i+len(short_sequence)]
            count = 0
    return max_sequence

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
