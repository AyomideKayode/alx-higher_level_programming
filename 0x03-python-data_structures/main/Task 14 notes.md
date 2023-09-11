### Thoughts
* To create a C function that prints basic information about Python lists as described in your task, you need to follow these steps:

	- Include the necessary Python headers: You'll need to include Python's C API headers to work with Python objects and types. In this case, we include `Python.h`. We include the `Python.h` header to access Python C API functions and types.

	- Define the function `print_python_list_info` with the prototype provided: The function should take a single argument of type `PyObject*`, which represents the Python list we are going to inspect.

	- Inside the function, I'd need to perform the following tasks:

		- Check if the given object is a Python list. You can use `PyList_Check` to verify this.

		- Print the size of the list (number of elements) using `PyList_Size`.

		- Print the amount of memory allocated for the list using the `ob_item` member of the `PyListObject` structure. This requires casting the `PyObject*` to a `PyListObject*`.

		- Iterate through the elements of the list and determine their types using the `Py_TYPE` macro and `Py_TYPE_NAME` macro.

	- Compile the C code into a shared library (e.g., `libPyList.so`) using the provided compilation command.

	- Create a Python script (e.g., `100-test_lists.py`) that imports the shared library, defines some Python lists, and calls the `print_python_list_info` function on these lists.

	- This has been provided in the task page. Can easily be copied and used to test if the C function is correct.

	- While compiling the C file with the flags provided, I ran into an error. Specifically because the Python version provided `3.4` in the one given is lesser than the one running on my terminal `3.6`. To correct that, I just changed the compilation to `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.6 100-print_python_list_info.c`

	- I'm guessing any compilation error you might have will stem from that version difference or if it has a different path in your local terminal. The path may vary depending on your system and Python version. Common paths include `/usr/include/python3.x` or `/usr/local/include/python3.x.`

	- Run the Python script to verify that your C function correctly prints the information about the Python lists.

	- Cheers.🎊🥳