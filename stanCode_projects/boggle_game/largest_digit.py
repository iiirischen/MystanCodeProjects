"""
File: largest_digit.py
Name: Iris
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	if n is negative, this function will convert to positive first, then continue the program
	:param n: int, the number which is going to search
	:return: int, positive number
	"""
	if n < 0:
		n *= -1
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, new_n):
	"""
	:param n: int, the number which is going to search
	:param new_n: int, the largest digit
	"""
	if n == 0:
		return new_n
	else:
		if n % 10 > new_n:				# compare new_n and a digit
			new_n = n % 10
		return find_largest_digit_helper(n//10, new_n)


if __name__ == '__main__':
	main()
