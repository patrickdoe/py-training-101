# py-training-101
Just a quick recap of the basics.   
More basic uses of Python can be seen in the main.py file.

---


### Python syntax
Refers to the rules that defines the structure of the Python programming language.
Python is known for its simplicity and readability.

#### Indentation:
Indentation in the form of spaces or tabs is used to define different code blocks.
```
if user_choice == "1":
  print('You chose the first option.')
```

#### Comments:
Comments start with a hashtag sign ("#"). Anything after the comment isn't executed.
```
# This is what a comment looks like.
if user_choice == "1":
  print('You chose the first option.')
```

#### Variables:
Variables are containers for data values. In Python there's no need to declare what type of a variable it is, this is determined by the created variables value.
```
x = 2      # Integer
y = "Bye"  # String
z = 3.14   # Float
```
Numeric types:   
- int (Integer)
- float (Decimal values)
- complex (Complex numbers)

Sequence types:   
- str (String text)
- list (Mutable collection of items)
- tuple (Immutable collection of items)

Mapping type:
- dict (Dictionary that stores key-value pairs, looks similar to the JSON format)
```
person = {"name": "Lisa", "age": 25}
```
Set types:
- set (Unordered collection of unique items)
```
unique_numbers = {1, 2, 3}
```
- frozenset (Immutable version of a set)

Boolean type:
- bool (True or False value)

None type:
- NoneType (Absence of a value, value = None)

Variables can be global and local:
```
x = "global variable"

def func():
  x = "local variable"
  print(x)                  # Prints "local variable"

print(x)                    # Prints "global variable"
```

#### Functions:
A function is a block of code that performs a specific task. Functions are defined by the "def" keyword and can contain multiple arguments.   
In the function below "name" is the argument of the function.
```
name = "Pat"

def greet(name)
  print(f"Hello, {name}.")   # Prints "Hello Pat"

# Calling a function:
greet("Lisa")                # Prints "Hello Lisa" by calling the greet function with a new argument value.
```

Common built-in functions in Python:
- print()                            = Displays output
- len()                              = Returns the length of an object
- type()                             = Returns the type (ex: int) of an object
- input()                            = Get user input as string
- int(), str(), float(), bool()      = Type conversions (ex: from string to integer)
- range()                            = Generate a sequence of numbers   
  ex: "range(start, stop, step)"


#### Return Values:
Used for functions that return values. Defined by the "return" keyword.
```
# The result variable calls the function "adding" 
def adding(a, b)
  return a + b      # Return the addition of the two arguments.

result = add(2, 2)  # result = 4.
```

#### Classes & Objects:
A Class can be seen as an object constructor, or a "blueprint" for creating objects.
```
# Class
class MyClass:
  x = 5

# Object
p1 = MyClass()
print(p1.x)
```

The "__init__()" function:   
All classes have a function called __init__(), which is always executed when the class is being initiated.   
Use the __init__() function to assign values to object properties, such as:
```
class Person:
  def __init__(self, name, age):    # Arguments
    self.name = name                # Value to object property
    self.age = age                  # Value to object property

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```
The self Parameter:   
The self Parameter is used to refer to a current instance of the class and access variables that belong to the class.   
It does not require you to call it "self" as in the example above.

The __str__() Function:   
The __str__() function controls what should be returned when the class object is represented as a string.   
If the __str__() function is not set, the string representation of the object is returned.
```
# Without the __str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)                  # Prints "<__main__.Person object at 0x15039e602100>"
```
```
# With the __str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)                  # Prints "John(36)"
```

Object Methods:   
Objects can contain <mark>methods</mark> which are functions that belong to the object.
```
class Person:                                  # Class
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):                            # Method 
    print("Hello my name is " + self.name)

p1 = Person("John", 36)                        # Object
p1.myfunc()                                    # Method is executed through the p1 object
```

#### enumerate() Function:
The enumerate() function adds a counter to the items in the list, allowing you to iterate through both the index and the item at the same time.
```
x = ('apple', 'banana', 'cherry')
y = enumerate(x)                                # Prints "[(0, 'apple'), (1, 'banana'), (2, 'cherry')]"
```
Enumerate syntax: enumerate(iterable, start)   
(Default start index is 0 if nothing else is specified.)

#### Lambda:
A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
Often used in simple cases where defining a full function would be overkill such as inside functions like; map(), filter(), or sorted()).
```
# List of tuples (name, age)
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]

# Sort by the second element (age)
sorted_people = sorted(people, key=lambda person: person[1])

print(sorted_people)                    # Prints "[('Charlie', 20), ('Alice', 25), ('Bob', 30)]"
```
