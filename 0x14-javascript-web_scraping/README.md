# Project: 0x14. JavaScript - Web scraping

## Resources

### Read or watch:-

- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

### General

- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use `request` and fetch API
- How to read and write a file using `fs` module

### More Info

#### Install Node 14

```sh
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semi-standard

[Documentation](https://github.com/standard/semistandard)

```sh
$ sudo npm install semistandard --global
```

#### Install `request` module and use it

[Documentation](https://github.com/request/request)

```sh
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

**Notes**: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

## Tasks

0. [Readme](./0-readme.js) :

Write a script that reads and prints the content of a file.

- The first argument is the file path
- The content of the file must be read in `utf-8`
- If an error occurred during the reading, print the error object

```sh
ayomide@Kazzywiz:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./0-readme.js cisfun 
C is super fun!

ayomide@Kazzywiz:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./0-readme.js doesntexist
{ [Error: ENOENT: no such file or directory, open 'doesntexist']
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
ayomide@Kazzywiz:~/alx-higher_level_programming/0x14-javascript-web_scraping$ 
```

| Task                        | File                                           |
| --------------------------- | ---------------------------------------------- |
|                    |
| 1. Write me                 | [1-writeme.js](./1-writeme.js)                 |
| 2. Status code              | [2-statuscode.js](./2-statuscode.js)           |
| 3. Star wars movie title    | [3-starwars_title.js](./3-starwars_title.js)   |
| 4. Star wars Wedge Antilles | [4-starwars_count.js](./4-starwars_count.js)   |
| 5. Loripsum                 | [5-request_store.js](./5-request_store.js)     |
| 6. How many completed?      | [6-completed_tasks.js](./6-completed_tasks.js) |
