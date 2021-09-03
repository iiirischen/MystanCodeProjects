"""
File: rocket.py
Name:Iris Chen
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	According to the SIZE, the program prints a shape which looks like a rocket.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	This function uses "/" to make the head of rocket, which SIZE equal to the length of the base.
	"""
	space = SIZE
	for i in range(SIZE):
		for j in range(space, 0, -1):
			print(end=" ")
		for k in range(i+1):
			print("/", end="")
		for m in range(i+1):
			print("\\", end="")
		print("")
		space -= 1


def belt():
	"""
	This function prints the belt,
	which the amount of ' = ' equals to twice as much as SIZE
	"""
	print('+', end="")
	for i in range(SIZE+SIZE):
		print('=', end="")
	print('+')


def upper():
	"""
	This function prints the upper body of the rocket
	"""
	dots = SIZE
	for i in range(SIZE):
		print("|", end="")
		for j in range(dots-1, 0, -1):
			print('.', end="")
		for k in range(i+1):
			print("/\\", end="")
		for m in range(dots - 1, 0, -1):
			print('.', end="")
		print("|")
		dots -= 1


def lower():
	"""
	This function prints the lower body of the rocket
	"""
	dots = SIZE
	for i in range(SIZE):
		print("|", end="")
		for j in range(i):
			print('.', end="")
		for k in range(dots, 0, -1):
			print("\\/", end="")
		for m in range(i):
			print('.', end="")
		print("|")
		dots -= 1

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()