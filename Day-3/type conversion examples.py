Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=10.5
int(b)
10
complex(b)
(10.5+0j)
str(b)
'10.5'
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
d='python;
SyntaxError: unterminated string literal (detected at line 1)
d='python'
a='1234'
'2345.6778'
'2345.6778'
int(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(s)
NameError: name 's' is not defined
int(a)
1234
int(b)
10
float(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float(s)
NameError: name 's' is not defined
float(a)
1234.0
float(b)
10.5
list(s)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list(s)
NameError: name 's' is not defined
list(a)
['1', '2', '3', '4']
list(b)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    tuple(s)
NameError: name 's' is not defined
list(d)
['p', 'y', 't', 'h', 'o', 'n']
numbers = [1, 2, 3, 4, 5]
int(numbers)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(numbers)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(numbers)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(numbers)
TypeError: float() argument must be a string or a real number, not 'list'
bool(numbers)
True
str(numbers)
'[1, 2, 3, 4, 5]'
tuple(numbers)
(1, 2, 3, 4, 5)
dict(numbers)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(numbers)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
set(numbers)
{1, 2, 3, 4, 5}
n = ("Ajay", "Rahul", "Sai")
int(n)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(n)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(n)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    float(n)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(n)
"('Ajay', 'Rahul', 'Sai')"
list(n)
['Ajay', 'Rahul', 'Sai']
>>> dict(n)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dict(n)
ValueError: dictionary update sequence element #0 has length 4; 2 is required
>>> set(n)
{'Sai', 'Rahul', 'Ajay'}
>>> complex(n)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    complex(n)
TypeError: complex() argument must be a string or a number, not tuple
>>> a = {1, 2, 3}
>>> str(a)
'{1, 2, 3}'
>>> list(a)
[1, 2, 3]
>>> tuple(a)
(1, 2, 3)
>>> bool(a)
True
>>> s = {
...     "name": "Ajay",
...     "age": 21,
...     "course": "Python"
... }
>>> str(s)
"{'name': 'Ajay', 'age': 21, 'course': 'Python'}"
>>> list(s)
['name', 'age', 'course']
>>> tuple(s)
('name', 'age', 'course')
>>> set(s)
{'age', 'name', 'course'}
>>> bool(s)
True
>>> a = True
>>> int(a)
1
>>> float(a)
1.0
>>> str(a)
'True'
>>> complex(a)
(1+0j)
