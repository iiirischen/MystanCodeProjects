"""
File: hangman.py
Name:Iris Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """

    """
    answer = random_word()
    dash = dashed(answer)
    # ' ----- '
    count = N_TURNS
    # count how many chances left
    input_ch = input_(dash, count)
    # the function user input answers
    guess(input_ch, answer, dash, count)


def guess(input_ch, answer, dash, count):
    """
    this function checks whether the user guesses the answer.
    """
    guess_word = ""
    while True:
        # check whether the alphabet user entered matches the answer
        for i in range(len(answer)):
            if answer[i] == input_ch:
                guess_word += input_ch
            elif dash[i].isalpha():
                guess_word += dash[i]
            else:
                guess_word += "-"
        dash = guess_word
        guess_word = ""
        if answer.find(input_ch) == -1:
            # the user guesses wrong
            count -= 1
            print('There is no ' + input_ch + "'s in the word.")
        if dash.isalpha():
            # the user guesses the word
            print('You are correct!')
            print('You win!!')
            break
        elif count == 0:
            # the user uses all the chance, and game over
            print('You are completely hung : ( ')
            break
        else:
            input_ch = input_(dash, count)
    print('The word was: ' + answer)


def input_(dash, count):
    """
    :param dash: string, " ----- "
    :param count: int, count how many chances left
    :return: string, the alphabet user enters.
    """
    print("The word looks like: " + dash)
    print("You have " + str(count) + " guesses left.")
    input_ch = input('Your guess: ')
    while len(input_ch) > 1 or not input_ch.isalpha():
        # the user enters wrong format
        print('illegal format.')
        input_ch = input('Your guess: ')
    input_ch = input_ch.upper()
    return input_ch


def dashed(answer):
    """
    :answer: string, the answer user going to guess.
    :return: string, "-----"
    """
    dash = ""
    for i in range(len(answer)):
        dash += '-'
    return dash


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
