"""
File: hailstone.py
Name:Iris Chen
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    The number user input is be calculated by Hailstone Sequence.
    """
    print('This program computes Hailstone sequences.')
    print('\n')
    total_step = 0
    # count how many lines hailstone sequence runs.
    num = int(input('Enter a number: '))
    while True:
        if num == 1:
            # the program break when the number reach to 1.
            print('It took ' + str(total_step) + ' steps to reach 1. ')
            break
        elif num % 2 == 1:
            # The number is an odd number
            print(str(int(num)), end=" ")
            num = 3 * num + 1
            print(' is odd , so I make 3n+1: '+str(int(num)))
            total_step += 1
        elif num % 2 == 0:
            # The number is an even number
            print(str(int(num)), end=" ")
            num = num/2
            print(' is even , so I take half: ' + str(int(num)))
            total_step += 1



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
