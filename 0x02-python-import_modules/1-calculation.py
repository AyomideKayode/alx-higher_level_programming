#!/usr/bin/python3
if __name__ == '__main__':
    # Import the functions from calculator_1.py
    from calculator_1 import add, sub, mul, div

    # Assign the values to variables a and b
    a = 10
    b = 5

    # Print the results
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
