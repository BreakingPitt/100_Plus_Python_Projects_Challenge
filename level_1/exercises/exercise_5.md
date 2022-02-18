# Question 5

### Question:

Define a class which has at least two methods:

**getString**: To get a string from console input.

**printString**: To print the string in upper case.

Also, please include simple test function to test the class methods.

_Hints_:

Use __init__ method to construct some parameters

#### Option 1

```python
class InputOutputString:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())


InputOutputObject = InputOutputString()
InputOutputObject.get_string()
InputOutputObject.print_string()
```
