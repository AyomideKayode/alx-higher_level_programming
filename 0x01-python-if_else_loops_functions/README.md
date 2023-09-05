# Project: 0x01. Python - if/else, loops, functions
![img](./main/Python-if-else.png)
> Each file in this repository holds code that illustrates an essential concept of programming,
> specific to the Python programming language: if/elif/else loops, range, ord(), chr(),
>  modulo, copy of string, bytecode

## Resources

#### Read or watch:

* [More Control Flow Tools](https://intranet.alxswe.com/rltoken/jpjs5EnZTpBLLEremJYjPQ)
* [IndentationError](https://intranet.alxswe.com/rltoken/F9n2AE-fpEPzt2PfBMGYAQ)
* [How To Use String Formatters in Python 3](https://intranet.alxswe.com/rltoken/ZdtRIAkFu8dMBT99DcFBNg)
* [Learn to Program](https://intranet.alxswe.com/rltoken/ElQgZYNHrLI7kV_ysEB1hQ)
* [Learn to Program 2 : Looping](https://intranet.alxswe.com/rltoken/ElQgZYNHrLI7kV_ysEB1hQ)
* [Pycodestyle -- Style Guide for Python Code](https://intranet.alxswe.com/rltoken/TuTTnEg_Rwn8U1g3PEsZmA)
## Learning Objectives

### General

* Why Python programming is awesome
* Why indentation is so important in Python
* How to use the <code>if</code>, <code>if ... else</code> statements
* How to use comments
* How to affect values to variables
* How to use the <code>while</code> and <code>for</code> loops
* How is Python’s <code>for</code> different from <code>C</code>‘s?
* How to use the <code>break</code> and <code>continues</code> statements
* How to use <code>else</code> clauses on loops
* What does the <code>pass</code> statement do, and when to use it
* How to use <code>range</code>
* What is a function and how do you use functions
* What does return a function that does not use any <code>return</code> statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them
---
### Description of what each file shows (Tasks):

* main --- folder holds test files that showcase examples of how to use functions.
* lists.h --- holds the `.c` files' function prototypes.

* Files that start with:
0. [Positive anything is better than negative nothing](0-positive_or_negative.py) : This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
	- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
	- The variable `number` will store a different value every time you will run this program.
	- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code.
	- The output of the program should be:
		- The number, followed by
			- if the number is greater than 0: `is positive`
			- if the number is 0: `is zero`
			- if the number is less than 0; `is negative`
		- followed by a new line.
1. [The last digit](1-last_digit.py) : This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.
	- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py)
	- The variable `number` will store a different value every time you will run this program.
	- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000,10000)`
	- The output of the program should be:
		- The string `Last digit of`, followed by
		- the number, followed by
		- the string `is`, followed by the last digit of `number`, followed by
			- if the last digit is greater than 5: the string `and is greater than 5`
			- if the last digit is 0: the string `and is 0`
			- if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
		- followed by a new line.
2. [I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game](2-print_alphabet.py) : Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
	- You can only use one `print` function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
3. [When I was having that alphabet soup, I never thought that it would pay off](3-print_alphabt.py) : Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
	- Print all the letters except `q` and `e`
	- You can only use one `print` function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
4. [Hexadecimal printing](4-print_hexa.py) : Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)
	- Print all the letters except `q` and `e`
	- You can only use one `print` function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
5. [00...99](5-print_comb2.py) : Write a program that prints numbers from `0` to `99`.
	- Numbers must be separated by `,`, followed by a space
	- Numbers should be printed in ascending order, with two digits
	- The last number should be followed by a new line
	- You can only use no more than 2 `print` functions with string format
	- You can only use one loop in your code
	- You are not allowed to store numbers or strings in a variable
	- You are not allowed to import any module
6. [Inventing is a combination of brains and materials. The more brains you use, the less material you need](6-print_comb3.py) : Write a program that prints all possible different combinations of two digits.
	- Numbers must be separated by `,`, followed by a space
	- The two digits must be different
	- `01` and `10` are considered the same combination of the two digits `0` and `1`
	- Print only the smallest combination of two digits
	- Numbers should be printed in ascending order, with two digits
	- The last number should be followed by a new line
	- You can only use no more than 3 `print` functions with string format
	- You can only use no more than 2 loops in your code
	- You are not allowed to store numbers or strings in a variable
	- You are not allowed to import any module
7. [islower](7-islower.py) : Write a function that checks for lowercase character.
	- Prototype: `def islower(c):`
	- Returns `True` if `c` is lowercase
	- Returns `False` otherwise
	- You are not allowed to import any module
	- You are not allowed to use `str.upper()` and `str.isupper()`
	- **Tips:** [ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
	- You don’t need to understand `__import__`
8. [To uppercase](8-uppercase.py) : Write a function that prints a string in uppercase followed by a new line.
	- Prototype: `def uppercase(str):`
	- You can only use no more than 2 `print` functions with string format
	- You can only use one loop in your code
	- You are not allowed to import any module
	- You are not allowed to use `str.upper()` and `str.isupper()`
	- **Tips:** [ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
	- You don’t need to understand `__import__`

---
### Environment
* Language: Python 3.4.3 (and C for #10)
	* OS: Ubuntu 14.04 LTS
	* Compiler: python3 (and gcc 4.8.4)
	* Style guidelines: 
		- [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/)
		- [Betty style](https://github.com/holbertonschool/Betty/wiki)

---
### Author

- <em>Website</em> - [Ayomide Kayode](https://github.com/AyomideKayode)
- <em>ALX Software Engineering Program</em> - [ALX_AFRICA](https://www.alxafrica.com/programmes/)
- <em>Twitter</em> - [@kazzy_wiz](https://www.twitter.com/kazzy_wiz)