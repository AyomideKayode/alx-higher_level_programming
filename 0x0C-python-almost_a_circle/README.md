# Project: 0x0C. Python - Almost a circle

<video width="100%" controls loop>
  <source src="./main/Python-Almost-A-Circle.mp4" type="video/mp4">
</video>

## Resources

#### Read or watch:

* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
## Learning Objectives

### General

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is <code>*args</code> and how to use it
* What is <code>**kwargs</code> and how to use it
* How to handle named arguments in a function


## Description of what each file shows (Tasks):
* **main**	--- folder that holds all main.py files provided as test cases.
* **models**	--- folder that holds the main projects functions for submission
* **tests**	--- folder that contains all testcase file for functions written (Unittest module)

0. [If it's not tested it doesn't work](./tests/) : All your files, classes and methods must be unit tested and be PEP 8 validated.
	```sh
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ python3 -m unittest discover tests
	........
	----------------------------------------------------------------------
	Ran 8 tests in 0.001s

	OK
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ 
	```
- <em>Note that this is just an example. The number of tests you create can be different from the above example.</em>
1. [Base class](./models/base.py),
	[Python Package](./models/__init__.py) : Write the first class `Base`:
- Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package
- Create a file named `models/base.py`:
	- Class `Base`:
		- private class attribute `__nb_objects = 0`
		- class constructor: `def __init__(self, id=None):`:
			- if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
			- otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`
- This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
	```sh
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ ls
	0-main.py  README.md  main  models  tests
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ ./0-main.py 
	1
	2
	3
	12
	4
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ 
	```
2. [First Rectangle](./models/rectangle.py) : Write the class `Rectangle` that inherits from `Base`:
	- In the file `models/rectangle.py`
	- Class `Rectangle` inherits from `Base`
	- Private instance attributes, each with its own public getter and setter:
	 	- `__width` -> `width`
	 	- `__height` -> `height`
	 	- `__x` -> `x`
	 	- `__y` -> `y`
	- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`
	 	- Call the super class with `id` - this super call with use the logic of the `__init__` of the `Base` class
	 	- Assign each argument `width`, `height`, `x` and `y` to the right attribute
- Why private attributes with getter/setter? Why not directly public attribute?
- Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
	```sh
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ ./1-main.py 
	1
	2
	12
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ python3 -m unittest tests/test_models/test_rectangle.py
	........
	----------------------------------------------------------------------
	Ran 8 tests in 0.002s

	OK
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ 
	```
3. [Validate attributes](./models/rectangle.py) : Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):
	- If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
	- If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
	- If `x` or `y` is under 0, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`
	```sh
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ ./2-main.py 
	[TypeError] height must be an integer
	[ValueError] width must be > 0
	[TypeError] x must be an integer
	[ValueError] y must be >= 0
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ 
	```
4. [Area first](./models/rectangle.py) : Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.
	```sh
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ ./3-main.py 
	6
	20
	56
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ python3 -m unittest tests/test_models/test_rectangle.py
	.........
	----------------------------------------------------------------------
	Ran 9 tests in 0.003s

	OK
	kazzywiz@Kazzywiz:~/alx-higher_level_programming/0x0C-python-almost_a_circle$ 
	```










| Task | File |
| ---- | ---- |
| 5. Display #0 | [models/rectangle.py](./models/rectangle.py) |
| 6. __str__ | [models/rectangle.py](./models/rectangle.py) |
| 7. Display #1 | [models/rectangle.py](./models/rectangle.py) |
| 8. Update #0 | [models/rectangle.py](./models/rectangle.py) |
| 9. Update #1 | [models/rectangle.py](./models/rectangle.py) |
| 10. And now, the Square! | [models/square.py](./models/square.py) |
| 11. Square size | [models/square.py](./models/square.py) |
| 12. Square update | [models/square.py](./models/square.py) |
| 13. Rectangle instance to dictionary representation | [models/rectangle.py](./models/rectangle.py) |
| 14. Square instance to dictionary representation | [models/square.py](./models/square.py) |
| 15. Dictionary to JSON string | [models/base.py](./models/base.py) |
| 16. JSON string to file | [models/base.py](./models/base.py) |
| 17. JSON string to dictionary | [models/base.py](./models/base.py) |
| 18. Dictionary to Instance | [models/base.py](./models/base.py) |
| 19. File to instances | [models/base.py](./models/base.py) |