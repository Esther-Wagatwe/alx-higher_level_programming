# 0x14-javascript-web_scraping

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
Why JavaScript programming is amazing
How to manipulate JSON data
How to use request and fetch API
How to read and write a file using fs module

### Requirements

- Allowed editors: vi, vim, emacs
- Interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All files should end with a new line
- First line of all files should be `#!/usr/bin/node`
- A `README.md` file at the root of the project folder is mandatory
- Code should be semistandard compliant, using Standard rules with semicolons
- All files must be executable

### How to Install Node 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### How to Install semi-standard

```bash
$ sudo npm install semistandard --global
```

### How to Install request module

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

### Tasks Overview

* [0.Readme](./0-readme.js)
   - Write a script that reads and prints the content of a file.

* [1.Write me](./1-writeme.js)
   - Write a script that writes a string to a file.

* [2.Status code](./2-statuscode.js)
   - Write a script that displays the status code of a GET request.

* [3.Star wars movie title](./3-starwars_title.js)
   - Write a script that prints the title of a Star Wars movie based on the episode number provided.

* [4.Star wars Wedge Antilles](./4-starwars_count.js)
   - Write a script that prints the number of movies where the character "Wedge Antilles" is present.

* [5.Loripsum](./5-request_store.js)
   - Write a script that retrieves the contents of a webpage and stores it in a file.

* [6.How many completed?](./6-completed_tasks.js)
   - Write a script that computes the number of tasks completed by user id.

* [100.Who was playing in this movie?](./100-starwars_characters.js)
   - Write a script that prints all characters of a Star Wars movie.

* [101.Right order](./101-starwars_characters.js)
   - Write a script that prints all characters of a Star Wars movie in the same order as the list "characters" in the response.
