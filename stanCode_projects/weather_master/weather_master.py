"""
File: weather_master.py
Name: Iris chen
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	This program lets the users enter numbers
	and finds the maximum and minimum temperature,
	and also count how many temperatures are lower than 16 degree
	"""
	print('stanCode \"Weather Master 4.0\" !')
	temp = int(input('Next Temperature: (or -100 to quit) ?'))
	if temp == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = temp
		minimum = temp
		total_temp = temp
		# to plus all the temperature together in order to calculate the average
		total_num = 1
		# count how many times does the user enter
		total = 0
		if temp < 16:
			total += 1
		# count how many temperatures are lower than 16 degree
		while True:
			temp = int(input('Next Temperature: (or -100 to quit) ?'))
			if temp == EXIT:
				print('Highest temperature = ' + str(maximum))
				print('Lowest temperature = ' + str(minimum))
				print('Average = ' + str(average_temp(total_temp, total_num)))
				print(str(total) + ' cold day(s)')
				break
			if temp > maximum:
				maximum = temp
			elif temp < minimum:
				minimum = temp
			if temp < 16:
				total += 1
			total_temp += temp
			total_num += 1


def average_temp(total_temp, total_num):
	"""
	:param total_temp: the sum of all the temperatures.
	:param total_num:  the sum of the input numbers.
	:return: the average of the temperatures.
	"""
	average = total_temp/total_num
	return average



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
