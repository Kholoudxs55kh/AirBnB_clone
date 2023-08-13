# Project: 0x00. AirBnB clone - The console


#### This project is our first step to bo build our First Full Web App in ALX, in this project we are cloning the AirBnB Site In a Simple Way, Starting basicly with building a special console for the Application to ease the interaction between the user and the data base which will be in this phase "JSON file"


## The  Command Interpreter:

### How To Start It:

#### We are Building the Interpreter "our console", by calling the module cmd, that will let us build it with a few steps and less effort (depending on understanding it's functionality well)

### How To Use It:

#### we have to use it in interactive mode like this:
```python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### And Non-interactively, like this :
```python
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
