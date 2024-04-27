# 0x12-javascript-warm_up
In this project, I learnt:
- How to run a JavaScript script
- How to create variables and constants
- What are differences between var, const and let
- What are all the data types available in JavaScript
- How to use the if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use while and for loops
- How to use break and continue statements
- What is a function and how do you use functions
- What does a function that does not use any return statement return
- Scope of variables
- What are the arithmetic operators and how to use them
- How to manipulate dictionary
- How to import a file

## Requirements

- Allowed editors: vi, vim, emacs
- Your JavaScript code will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All JavaScript files must end with a new line.
- The first line of all JavaScript files must start with `#!/usr/bin/node`.
- A `README.md` file, located at the root of the project directory, is mandatory.
- Your code must follow the [semistandard style](https://github.com/Flet/semistandard) (version 16.x.x), which is a set of rules for writing clean and consistent JavaScript code. Semicolons should be used at the end of statements.
- All JavaScript files must be executable.
- The length of your files will be tested using `wc`.
- You need to install Node.js 14 for this project. You can install it using the following command:
  ```
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```
- You should also install the `semistandard` package for code linting using the following command:
  ```
  $ sudo npm install semistandard --global
  ```

## Tasks

### 0. First constant, first print

Write a script that prints the string "JavaScript is amazing".

- Create a constant variable called `myVar` with the value "JavaScript is amazing".
- Use `console.log(...)` to print all output.
- Do not use the `var` keyword.

**File:** [0-javascript_is_amazing.js](./0-javascript_is_amazing.js)

### 1. 3 languages

Write a script that prints 3 lines:

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"

Use `console.log(...)` to print all output. Do not use the `var` keyword.

**File:** [1-multi_languages.js](./1-multi_languages.js)

### 2. Arguments

Write a script that prints a message depending on the number of arguments passed to it:

- If no arguments are passed, print "No argument".
- If only one argument is passed, print "Argument found".
- Otherwise, print "Arguments found".

Use `console.log(...)` to print all output. Do not use the `var` keyword.

**File:** [2-arguments.js](./2-arguments.js)

### 3. Value of my argument

Write a script that prints the first argument passed to it:

- If no arguments are passed, print "No argument".

Use `console.log(...)` to print all output. Do not use the `var` keyword or the `length` property.

**File:** [3-value_argument.js](./3-value_argument.js)

### 4. Create a sentence

Write a script that prints two arguments passed to it, in the following format: `<first argument> is <second argument>`.

Use `console.log(...)` to print all output. Do not use the `var` keyword.

**File:** [4-concat.js](./4-concat.js)

### 5. An Integer

Write a script that prints "My number: `<first argument converted to integer>`" if the first argument can be converted to an integer:

- If the argument can't be converted to an integer, print "Not a number".

Use `console.log(...)` to print all output. Do not use the `var` keyword or the `length` property. You are not allowed to use `try/catch`.

**File:** [5-to_integer.js](./5-to_integer.js)

### 6. Loop to languages

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of strings and a loop.

The first line: "C is fun"
The second line: "Python is cool"
The third line: "JavaScript is amazing"

You must use `console.log(...)` to print all output. Do not use the `var` keyword or any `if/else` statement. You can use only one `console.log` statement and you must use a loop (while, for, etc.).

**File:** [6-multi_languages_loop.js](./6-multi_languages_loop.js)

### 7. I love C

Write a script that prints `x` times "C

 is fun".

- The first argument is the number of times to print the string.
- If the first argument can't be converted to an integer, print "Missing number of occurrences".

Use `console.log(...)` to print all output. Do not use the `var` keyword. You can use only two `console.log` statements and you must use a loop (while, for, etc.).

**File:** [7-multi_c.js](./7-multi_c.js)

### 8. Square

Write a script that prints a square:

- The first argument is the size of the square.
- If the first argument can't be converted to an integer, print "Missing size".

Use the character 'X' to print the square. You must use `console.log(...)` to print all output. Do not use the `var` keyword. You must use a loop (while, for, etc.).

**File:** [8-square.js](./8-square.js)

### 9. Add

Write a script that prints the addition of two integers:

- The first argument is the first integer.
- The second argument is the second integer.
- You have to define a function with the prototype `function add(a, b)`.

Use `console.log(...)` to print all output. Do not use the `var` keyword.

**File:** [9-add.js](./9-add.js)

### 10. Factorial

Write a script that computes and prints a factorial:

- The first argument is the integer used for computing the factorial.
- Factorial of NaN is 1.
- You must do it recursively.
- You must use a function.
- You must use `console.log(...)` to print all output.

Do not use the `var` keyword.

**File:** [10-factorial.js](./10-factorial.js)

### 11. Second biggest!

Write a script that searches the second biggest integer in the list of arguments:

- You can assume all arguments can be converted to integers.
- If no argument is passed, print 0.
- If the number of arguments is 1, print 0.

Use `console.log(...)` to print all output. Do not use the `var` keyword.

**File:** [11-second_biggest.js](./11-second_biggest.js)

### 12. Object

Update this script to replace the value 12 with 89:

You are not allowed to use the `var` keyword.

**File:** [12-object.js](./12-object.js)

### 13. Add file

Write a function that returns the addition of two integers:

- The function must be visible from outside.
- The name of the function must be `add`.

You are not allowed to use the `var` keyword.

**File:** [13-add.js](./13-add.js)

## Author
* Esther Wagatwe
* Email -> estherwagatwe@gmail.com
