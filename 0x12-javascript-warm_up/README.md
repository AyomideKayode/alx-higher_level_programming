# Project: 0x12. JavaScript - Warm up

## Resources

#### Read or watch:

- [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
- [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
- [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
- [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
- [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/)
- [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
- [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

### General

- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- What are differences between <code>var</code>, <code>const</code> and <code>let</code>
- What are all the data types available in JavaScript
- How to use the <code>if</code>, <code>if ... else</code> statements
- How to use comments
- How to affect values to variables
- How to use <code>while</code> and <code>for</code> loops
- How to use <code>break</code> and <code>continue</code> statements
- What is a function and how do you use functions
- What does a function that does not use any <code>return</code> statement return
- Scope of variables
- What are the arithmetic operators and how to use them
- How to manipulate dictionary
- How to import a file

## More Info

### Install Node 14

```sh
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

[Documentation](https://github.com/standard/semistandard)

```sh
$ sudo npm install semistandard --global
```

## **NOTE**

- Experienced some issues with the `nodejs` installed with the instruction above because I couldn't install `semistandard`.
- So I had to install `nvm` Node Version Manager.
  - **Using `curl`**:
  ```sh
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
  ```
  - **Using `wget`**:
  ```sh
  wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
  ```
- After installation, close and reopen the terminal to check that `nvm` was properly installed. `nvm --version`
- Now that we have a the `nvm`, we can use it to update or install the latest version of `Node.js`: `nvm install --lts`
- This command installs the latest LTS (Long Term Support) version of Node.js. After installation, use `nvm use <version>` to switch to the installed Node.js version.

## Description of what each file shows (Tasks):

- main - help folder to hold main.js files provided by ALX and or images to make README better.

0. [First constant, first print](./0-javascript_is_amazing.js) :

Write a script that prints “JavaScript is amazing”:

- You must create a constant variable called `myVar` with the value “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

  ```sh
  guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js
  JavaScript is amazing
  guillaume@ubuntu:~/0x12$
  guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js
  guillaume@ubuntu:~/0x12$
  ```

1. [3 languages](./1-multi_languages.js) :

Write a script that prints 3 lines:

- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

  ```sh
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./1-multi_languages.js
  C is fun
  Python is cool
  JavaScript is amazing
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$
  ```

2. [Arguments](./2-arguments.js) :

Write a script that prints a message depending of the number of arguments passed:

- If no arguments are passed to the script, print “No argument”
- If only one argument is passed to the script, print “Argument found”
- Otherwise, print “Arguments found”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

  ```sh
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./2-arguments.js
  No argument
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./2-arguments.js Best
  Argument found
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./2-arguments.js BestBest School
  Arguments found
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$
  ```

Reference: [process.argv](https://nodejs.org/api/process.html#process_process_argv)

3. [Value of my argument](./3-value_argument.js) :

Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print “No argument”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`

  ```sh
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./3-value_argument.js 
  No argument
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./3-value_argument.js kay
  kay
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ semistandard 3-value_argument.js 
  ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ 
  ```

4. [Create a sentence](./4-concat.js) :

Write a script that prints two arguments passed to it, in the following format: “ is ”

- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

	```sh
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./4-concat.js 
	undefined is undefined
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./4-concat.js Kay good
	Kay is good
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ semistandard ./4-concat.js 
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ 
	```

5. [An Integer ](./5-to_integer.js) :

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

- If the argument can’t be converted to an integer, print “Not a number”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`

	```sh
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./5-to_integer.js 
	Not a number
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./5-to_integer.js 78
	My number: 78
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ 
	```

6. [Loop to languages](./6-multi_languages_loop.js) :

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use any `if/else` statement
- You can use only one `console.log`
- You must use a loop (`while`, `for`, etc.)

	```sh
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./6-multi_languages_loop.js 
	C is fun
	Python is cool
	JavaScript is amazing
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ 
	```

7. [I love C](./7-multi_c.js) : 

Write a script that prints `x` times “C is fun”

- Where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print “Missing number of occurrences”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You can use only two `console.log`
- You must use a loop (`while`, `for`, etc.)

	```sh
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./7-multi_c.js 
	Missing number of occurences
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./7-multi_c.js 8
	C is fun
	C is fun
	C is fun
	C is fun
	C is fun
	C is fun
	C is fun
	C is fun
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$
	```

8. [Square](./8-square.js) :

Write a script that prints a square

- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print “Missing size”
- You must use the character `X` to print the square
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You must use a loop (`while`, `for`, etc.)

	```sh
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./8-square.js 
	Missing size
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./8-square.js  2
	XX
	XX
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./8-square.js 9
	XXXXXXXXX
	XXXXXXXXX
	XXXXXXXXX
	XXXXXXXXX
	XXXXXXXXX
	XXXXXXXXX
	XXXXXXXXX
	XXXXXXXXX
	XXXXXXXXX
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ 
	```

9. [Add](./9-add.js) :

Write a script that prints the addition of 2 integers

- The first argument is the first integer
- The second argument is the second integer
- You have to define a function with this prototype: `function add(a, b)`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

	```sh
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./9-add.js 4 8
	12
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./9-add.js 13 89
	102
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./9-add.js
	NaN
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$
	```

10. [Factorial](./10-factorial.js) :

Write a script that computes and prints a factorial

- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of `NaN` is `1`
- You must do it recursively
- You must use a function
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

	```sh
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./10-factorial.js 
	1
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./10-factorial.js 4
	24
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./10-factorial.js 89
	1.6507955160908452e+136
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./10-factorial.js 333
	Infinity
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ semistandard
	semistandard: Semicolons For All! (https://github.com/standard/semistandard)
	semistandard: Run `semistandard --fix` to automatically fix some problems.
	/home/ayomide/alx-higher_level_programming/0x12-javascript-warm_up/10-factorial.js:4:19: Missing space before function parentheses. (space-before-function-paren)
	ayomide@Kazzywiz:~/alx-higher_level_programming/0x12-javascript-warm_up$ 
	```

| Task                    | File                                                     |
| ----------------------- | -------------------------------------------------------- |
|                              |
|                                   |
|                     |
| 11. Second biggest!     | [11-second_biggest.js](./11-second_biggest.js)           |
| 12. Object              | [12-object.js](./12-object.js)                           |
| 13. Add file            | [13-add.js](./13-add.js)                                 |
