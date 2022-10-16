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

Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.

    $./console.py
    (hbnb) create BaseModel
    119be863-6fe5-437e-a180-b9892e8746b8
    (hbnb) quit
    $ cat file.json ; echo ""
    {"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8":{"updated_at": "2019-02-17T2
    1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "Base
    Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}

### Show
    
    (hbnb) show BaseModel 123-123-123.
Prints the string representation of a class instance based on a given id.

    $ ./console.py
    (hbnb) create User
    1e32232d-5a63-4d92-8092-ac3240b29f46
    (hbnb)
    (hbnb) show User    1e32232d-5a63-4d92-8092-ac3240b29f46
    [User]  (1e32232d-5a63-4d92-8092-ac3240b29f46)  {'id': '1e32232d-5a63-4d92-8092-a
    c3240b29f46', 'created_at': datetime.  datetime(2019, 2, 17, 21, 34, 3, 635828), 
    'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
    (hbnb) 
    (hbnb) User.show    (1e32232d-5a63-4d92-8092-ac3240b29f46)
    [User]  (1e32232d-5a63-4d92-8092-ac3240b29f46){'id': '1e32232d-5a63-4d92-8092-a
    c3240b29f46', 'created_at': datetime.   datetime(2019, 2, 17, 21, 34, 3, 635828), 
    'updated_at': datetime.datetime(2019, 2,    17, 21, 34, 3, 635828)}
    (hbnb) 

### Destroy
To Delete an instance of an object use "destroy id". ex:

    (hbnb) destroy BaseMOdel 123-123-123.
Deletes a class instance based on a given id. The storage file file.json is updated accordingly.

    $ ./console.py
    (hbnb) create State
    d2d789cd-7427-4920-aaae-88cbcf8bffe2
    (hbnb) create Place
    3e-8329-4f47-9947-dca80c03d3ed
    (hbnb)
    (hbnb) destroy State d2d789cd-7427-4920-aaae-88cbcf8bffe2
    (hbnb) Place.destroy(03486a3e-8329-4f47-9947-dca80c03d3ed)
    (hbnb) quit
    $ cat file.json ; echo ""
    {}

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






 
 



