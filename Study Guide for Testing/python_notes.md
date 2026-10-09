# Python Quick Revision Notes

## 1. Data Types

```python
x = 10            # int
y = 3.14          # float
name = "Karthik"  # string
is_ok = True      # bool
lst = [1,2,3]     # list
tup = (1,2,3)     # tuple
st = {1,2,3}      # set
dic = {"a":1}     # dict
n = None          # NoneType
```

### String Slicing
```python
s = "PythonNotes"
s[0]        # 'P'        -> first char
s[-1]       # 's'        -> last char
s[0:6]      # 'Python'   -> index 0 to 5
s[:6]       # 'Python'   -> from start
s[6:]       # 'Notes'    -> to end
s[::-1]     # 'seto...'  -> reverse string
s[::2]      # every 2nd char
```

### List/Array Slicing
```python
lst = [10,20,30,40,50]
lst[1:3]    # [20,30]
lst[:2]     # [10,20]
lst[-2:]    # [40,50]
lst[::-1]   # reverse list
lst[::2]    # every 2nd element
lst.append(60)      # add item
lst.remove(20)       # remove value
lst.pop()            # remove last
```

### Tuple
```python
t = (1,2,3)   # immutable, same slicing as list
t[0]          # 1
```

### Set
```python
s1 = {1,2,3}
s1.add(4)
s1.union({5,6})
s1.intersection({2,3})
```

### Dictionary
```python
d = {"name":"Karthik","age":25}
d["name"]        # access
d.get("age")     # safe access
d["city"]="Chennai"   # add key
d.keys(); d.values(); d.items()
```

---

## 2. Type Conversion
```python
int("10")     # 10
str(10)       # "10"
float("3.5")  # 3.5
list("abc")   # ['a','b','c']
```

---

## 3. Operators

| Type | Examples |
|---|---|
| Arithmetic | `+ - * / // % **` |
| Comparison | `== != > < >= <=` |
| Logical | `and or not` |
| Assignment | `= += -= *= /=` |
| Bitwise | `& \| ^ ~ << >>` |
| Membership | `in`, `not in` |
| Identity | `is`, `is not` |

```python
a, b = 10, 3
a // b   # 3  (floor division)
a % b    # 1  (remainder)
a ** b   # 1000 (power)
```

---

## 4. Conditional Statements
```python
age = 20
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
else:
    print("Adult")

# Ternary
status = "Adult" if age >= 18 else "Minor"
```

---

## 5. Looping Statements
```python
# for loop
for i in range(5):
    print(i)          # 0 1 2 3 4

for ch in "abc":
    print(ch)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1

# break / continue
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
```

---

## 6. Functions
```python
def greet(name="Guest"):     # default arg
    return f"Hello {name}"

greet("Karthik")

def add(*args):               # variable args
    return sum(args)

def info(**kwargs):           # keyword args
    return kwargs

square = lambda x: x*x        # lambda function
```

---

## 7. Lambda Function
```python
# lambda arguments : expression
square = lambda x: x*x
square(5)          # 25

add = lambda a, b: a+b
add(3,4)            # 7

# with default value
greet = lambda name="Guest": f"Hi {name}"
greet()             # Hi Guest

# used with map, filter, sorted
nums = [1,2,3,4,5]
list(map(lambda x: x*2, nums))        # [2,4,6,8,10]
list(filter(lambda x: x%2==0, nums))  # [2,4]

points = [(1,2), (3,1), (5,0)]
sorted(points, key=lambda p: p[1])    # sort by 2nd value
```

---

## 8. OOPs Concepts
```python
class Animal:
    def __init__(self, name):   # constructor
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):              # inheritance
    def speak(self):            # polymorphism (method overriding)
        print(f"{self.name} barks")

d = Dog("Rex")
d.speak()   # Rex barks
```

Key concepts:
- **Encapsulation**: `self.__var` (private variable via double underscore)
- **Inheritance**: `class Child(Parent):`
- **Polymorphism**: same method name, different behavior
- **Abstraction**: using `abc` module with `@abstractmethod`

```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

---

## 9. File Handling
```python
# write
with open("data.txt","w") as f:
    f.write("Hello Python")

# read
with open("data.txt","r") as f:
    content = f.read()

# append
with open("data.txt","a") as f:
    f.write("\nNew line")

# read line by line
with open("data.txt") as f:
    for line in f:
        print(line.strip())
```

---

## 10. JSON Handling
```python
import json

data = {"name":"Karthik","age":25}

json_str = json.dumps(data)     # dict -> JSON string
back = json.loads(json_str)     # JSON string -> dict

# write to file
with open("data.json","w") as f:
    json.dump(data, f)

# read from file
with open("data.json") as f:
    d = json.load(f)
```

---

## 11. Exception Handling
```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
except Exception as e:
    print("Other error:", e)
else:
    print("Runs if no error")
finally:
    print("Always runs")

# raise custom error
raise ValueError("Invalid input")
```

---

## 12. Modules & Import
```python
import math
math.sqrt(16)

from datetime import datetime
datetime.now()
```

---

## 13. Extra Must-Knows
```python
# List comprehension
squares = [x*x for x in range(5)]

# Dict comprehension
d = {x: x*x for x in range(5)}

# enumerate & zip
for i, v in enumerate(["a","b"]):
    print(i, v)

for a, b in zip([1,2], [3,4]):
    print(a, b)
```
