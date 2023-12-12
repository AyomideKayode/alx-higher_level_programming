# Project: 0x13. JavaScript - Objects, Scopes and Closures

## Resources

### Read or watch:

* [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
* [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
* [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
* [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
* [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
* [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
* [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* [this/self](https://alistapart.com/article/getoutbindingsituations/)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

### General

* Why JavaScript programming is amazing
* How to create an object in JavaScript
* What <code>this</code> means
* What <code>undefined</code> means 
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

## Description of each files shows (Tasks):

* main - help folder to hold main.js files provided by ALX and or images to make README better.

0. [Rectangle #0](./0-rectangle.js) :

Write an empty class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class

```sh
ayomide@Kazzywiz:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./0-main.js 
Rectangle {}
[Function: Rectangle]
ayomide@Kazzywiz:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

1. [Rectangle #1](./1-rectangle.js) :

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`

```sh
ayomide@Kazzywiz:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./1-main.js 
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
ayomide@Kazzywiz:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ 
```

2. [Rectangle #2](./2-rectangle.js) :

Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object

```sh
ayomide@Kazzywiz:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./2-main.js 
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
ayomide@Kazzywiz:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ 
```

3. [Rectangle #3](./3-rectangle.js) :

Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments: w and h
- Initialize the instance attribute width with the value of w
- Initialize the instance attribute height with the value of h
- If w or h is equal to 0 or not a positive integer, create an empty object
- Create an instance method called print() that prints the rectangle using the character X

```sh
ayomide@Kazzywiz:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./3-main.js 
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
ayomide@Kazzywiz:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```


| Task | File |
| ---- | ---- |
|  |
|  |
| 4. Rectangle #4 | [4-rectangle.js](./4-rectangle.js) |
| 5. Square #0 | [5-square.js](./5-square.js) |
| 6. Square #1 | [6-square.js](./6-square.js) |
| 7. Occurrences | [7-occurrences.js](./7-occurrences.js) |
| 8. Esrever | [8-esrever.js](./8-esrever.js) |
| 9. Log me | [9-logme.js](./9-logme.js) |
| 10. Number conversion | [10-converter.js](./10-converter.js) |