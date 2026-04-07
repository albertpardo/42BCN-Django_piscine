# Django - 0 - Oob

All exercises specify allowed importsgfunctions and required filenames.

## Exercise 00 : Create your CV

- Create render.py that takes a .template file, replaces patterns with values from settings.py, and writes a .html file.
- Handle errors (wrong extension, missing file, wrong arg count).
- Provide myCV.template containing full HTML structure (doctype, __head__, __body__, __title__, name, surname, age, profession) using settings.py values.

- Example of use : `python3 render.py myCv.template`

##  Exercise 01 : coffee assistant

- Implement Intern class:
    - init(name="My name? I’m nobody, an intern, I have no name.")
    - str returns name.
    - Coffee nestedgclass with str returning "This is the worst coffee you ever tasted."
    - work() raises Exception("I’m just an intern, I can’t do that...")
    - make_coffee() returns Coffee instance.
- Tests: instantiate two interns (default and "Mark"), print names, ask Mark for coffee and print it, call work() on the other and handle exception.

##  Exercise 02 — beverages prices

- Implement HotBeverage class:
    - price g= 0.30, name = "hot beverage"
    - description() returns "Just some hot water in a cup."
    - str prints name, price (2 decimals), description.
- Subclasses: Coffee (name "coffee", price 0.40, desc "A coffee, to stay awake."), Tea (0.30), Chocolate (0.50, "Chocolate, sweet chocolate..."), Cappuccino (0.45, Italian phrase).
- Follow DRY: only override what's necessary. Tests: instantiate and display each class.

##  Exercise 03 — Machine 

- Implement CoffeeMachine:
    - Include EmptyCup subclass of HotBeverage: name "empty cup", price 0.90, desc "An empty cup?! Gimme my money back!"
    - BrokenMachineException(Exception) with message "This coffee machine has to be repaired."
    - `repair()` to reset machine.
    - `serve(beverageg_class)` randomly returns an instance of beverage_class or EmptyCup.
    - Machine breaks after serving 10 drinks; thereafter `serve()` raises `BrokenMachineException` until `repair()` called.
- Tests: instantiate `CoffeeMachine`, request drinks until it breaks, handle exception, repair and repeat.
- Example of use : `python3 machine.py`

##  Exercise 04 — Basic HTML element in Python object.

- Complete Elem class to model HTML elements (tag, content, attributes) per provided testsgspecs (fill indicated gaps).

## Exercise 05 - Element subclasses

- Create small classes that inherit Elem for common tags: __html__, __head__, __body__, __title__, __meta__, __img__, __table__, __th__, __tr__, __td__, __ul__, __ol__, __li__, __h1__, __h2__, __p__, __div__, __span__, __hr__, __br__.
- Each subclass constructor should accept content as first argument.
- Reuse Elem functionality and use inheritance; do not instantiate Elem directly.
- Provide tests demonstrating functionality and replicate the same HTML document from Ex04 using these new classes.
- Example of use : `python3 elements.py`


## Exercise 06 - Page validation

- Copy previous classes into this exercise folder.
- Implement a Page class that takes an Elem-derived instance and provides `is_valid()` returning True only if the document tree follows these rules:
    - Only allowed node types: __html__, __head__, __body__, __title__, __meta__, __img__, __table__, __th__, __tr__, __td__, __ul__, __ol__, __li__, __h1__, __h2__, __p__, __div__, __span__, __hr__, __br__, or __Text__.
    - __html__ must contain exactly a Head then a Body (in that order).
    - __head__ must contain exactly one __title__.
    - __body__ and div may contain only: __h1__, __h2__, __div__, __table__, __ul__, __ol__, __span__ or __Text__.
    - __title__, __h1__, __h2__, __li__, __th__, __td__ must contain exactly one __Text__ node (and only that).
    - __p__  must contain only __Text__.
    - __span__ may contain __Text__ or __p__  elements.
    - __ul__ and __ol__ must contain at least one __li__ and only __li__ elements.
- Example of use : `python3 Page.py`


