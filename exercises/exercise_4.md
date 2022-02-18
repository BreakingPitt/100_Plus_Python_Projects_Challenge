# Question 4

### Question:

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98

Then, the output should be:

```
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```

#### Option 1

```python
numbers = int(input())
computed_values = dict()
for number in range(1, numbers + 1):
  computed_values[number] = number * number
print(computed_values)
```

#### Option 2

```python
numbers = int(input())
print({number: number * number for i in range(1, numbers + 1)})
```
