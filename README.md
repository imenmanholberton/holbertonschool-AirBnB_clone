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

### all  or all BaseModel or BaseModel.all()

Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.

    $ ./console.py
    (hbnb) create BaseModel
    fce2124c-8537-489b-956e-22da455cbee8
    (hbnb) create BaseModel
    450490fd-344e-47cf-8342-126244c2ba99
    (hbnb) create User
    b742dbc3-f4bf-425e-b1d4-165f52c6ff81
    (hbnb) create User
    8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
    (hbnb)
    (hbnb) all BaseModel
    ["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99){'updated_at': datetime.da
    tetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2
    , 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
    eModel] (fce2124c-8537-489b-956e-22da455cbee8){'updated_at': datetime.datetime
    (2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17,
    21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
    (hbnb)
    (hbnb) User.all()
    ["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe){'updated_at': datetime.datetim
    e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
    , 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User] 
    (b742dbc3-f4bf-425e-b1d4-165f52c6ff81){'updated_at': datetime.datetime(2019, 2
    , 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44,
    15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
    (hbnb) 
    (hbnb) all
    ["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe){'updated_at': datetime.datetim
    e(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17
    , 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseMo
    del] (450490fd-344e-47cf-8342-126244c2ba99){'updated_at': datetime.datetime(20
    19, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21,
    45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742db
    c3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 2
    1, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 97
    4608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8
    537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 4
    3, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348
    ), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
    (hbnb) 

### Update

Update an instance based on the class name and id:

    (hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"

Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at). However, any attribute can be updated by providing a dictionary.

    $ ./console.py
    (hbnb) create User
    6f348019-0499-420f-8eec-ef0fdc863c02
    (hbnb)
    (hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"
    (hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
    [User] (6f348019-0499-420f-8eec-ef0fdc863c02){'created_at': datetime.datetime(
    2019, 2, 17, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': date
    time.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-
    ef0fdc863c02'}
    (hbnb)
    (hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02, address, "98 Mission S
    t")
    (hbnb) User.show(6f348019-0499-420f-8eec-ef0fdc863c02)
    [User] (6f348019-0499-420f-8eec-ef0fdc863c02){'created_at': datetime.datetime(
    2019, 2, 17, 21, 54, 39, 234382), 'address': '98 Mission St', 'first_name': 'Ho
    lberton', 'updated_at': datetime.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id
    ': '6f348019-0499-420f-8eec-ef0fdc863c02'}
    (hbnb)
    (hbnb) User.update(6f348019-0499-420f-8eec-ef0fdc863c02,{'email': 'holberton@h
    olberton.com', 'last_name': 'School'})
    [User] (6f348019-0499-420f-8eec-ef0fdc863c02){'email': 'holberton@holberton.co
    m', 'first_name': 'Holberton', 'updated_at': datetime.datetime(2019, 2, 17, 21,
    54, 39, 234382), 'address': '98 Mission St', 'last_name': 'School', 'id': '6f34
    8019-0499-420f-8eec-ef0fdc863c02', 'created_at': datetime.datetime(2019, 2, 17,
    21, 54, 39, 234382)}
    (hbnb) 

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






 
 



