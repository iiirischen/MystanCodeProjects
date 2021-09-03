"""
File: quadratic_solver.py
Name:Iris Chen
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Enter three numbers to finish the function.
	"""
	print("stanCode Quadratic Solver!")
	a = int(input('Enter a :'))
	b = int(input('Enter b :'))
	c = int(input('Enter c :'))
	if a == 0:
		print('Error!')
	else:
		calculate(a, b, c)


def calculate(a, b, c):
	"""
	calculate the root of the function
	:param a: int, the number to be calculated
	:param b: int, the number to be calculated
	:param c: int, the number to be calculated
	"""
	if b*b-4*a*c > 0:
		ans1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
		ans2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
		print('Two roots: '+str(ans1)+' , '+str(ans2))
	elif b*b-4*a*c == 0:
		ans1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
		print('One root: ' + str(ans1))
	else:
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
