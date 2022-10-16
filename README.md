#  **AirBnB clone  - The console**

# _Description of the project_:


---
 The AirBnB clone is for us to put in practice what we've learned so far, inheritance, classes, opening and closing files and changing them.
---
# _The Console_:
 The AirBnb console(command interpreter) is to manipulate a powerful storage system, serializing and deserializing json files. The console can be run in two different modes, interactive mode and non-interactive mode.
# _Installation_:
in order to run the AirBnb console, you must "install" in your repository the console by cloninh the following repository in your machine running:
## [Knn]
git clone https://github.com/imenmansouri93/holbertonschool-AirBnB_clone.git
## _Description of the command interpreter_:

Do you remember the shell? It'is exactly the same but limited  to a specific use-case. In our case, we want to be able to manage the objects of our project:

 - Create a new object(ex: a new se or a new Place)
 - Retrieve an object from a file, a database etc...
 - Do operations on objects(count, compute stats, etc...)
 - Update attribute of an abject
 - Destroy an object
## _Execution_
- How to use in The 'prompt(hbnb)' tells you that the console is ready to receive instuctions, type the instruction:

    (hbnb)

You could work like this in interacctive mode:

    $ ./console.py
    (hbnb) help

 Output:

    Documented commands (type help <topic>):
    ========================================
    EOF help quit

    (hbnb)
    (hbnb)
    (hbnb) quit
    $
    
 ## Commands:
- EOF: Exit the program.

 (hbnb) EOF

~/Holberton/holbertonschool-AirBnB_clone$
- create - create an object
- show - show an object (base on id)
- destroy - destroy an object
- all - show all objects, of one type or all type
- update - Update an instance based on the class name and id
- quit/EOF - quit the console
- help-see descriptions of commands

To start console type in shell

    AirBnB_clone$ ./console.py 
    (hbnb) 


### Create
To create an object use format "create" ex:

    (hbnb) create BaseModel

### Show
    
    (hbnb) show BaseModel 123-123-123.

### Destroy
To Delete an instance of an object use "destroy id". ex:

    (hbnb) destroy BaseMOdel 123-123-123.

### All

all Ex:

    (hbnb) all

### Update

Update an instance based on the class name and id:

    (hbnb) update BaseModel 123-123-123. user "holbertonschool"

### Quit 

  quit or EOF

## _Supported classes_

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

## _Authors_

- imen mansouri - imenmansouri@holbertonstudents.com






 
 



