#!/usr/bin/python3
if __name__ == '__main__':
	# Import the functions from calculator_1.py
	from calculator_1 import add, sub, mul, div

	# Assign the values to variables a and b
	a = 10
	b = 5

	# Call each imported function with a and b as arguments
	result_add = add(a, b)
	result_sub = sub(a, b)
	result_multiply = mul(a, b)
	result_divide = div(a, b)

	# Print the results
	print("{:d} + {:d} = {:d}".format(a, b, result_add))
	print("{:d} - {:d} = {:d}".format(a, b, result_sub))
	print("{:d} * {:d} = {:d}".format(a, b, result_multiply))
	print("{:d} / {:d} = {:d}".format(a, b, result_divide))
