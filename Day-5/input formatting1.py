Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input()
ajay
name
'ajay'
name=imput("Enter your name:")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    name=imput("Enter your name:")
NameError: name 'imput' is not defined. Did you mean: 'input'?
name=input("enter your name:")
enter your name:ajay
age=input("enter your age:")
enter your age:21
age
'21'
age=int(input("enter your age:"))
enter your age:21
age
21
type(age)
<class 'int'>
gpa=float(input("enter your gpa:"))
enter your gpa:8.6
gpa
8.6
type(gpa)
<class 'float'>
'ajay ranjith eshwar preetam'.split(' ')
['ajay', 'ranjith', 'eshwar', 'preetam']
names=input("enter the names:").split()
enter the names:ajay ranjith eshu ram
names
['ajay', 'ranjith', 'eshu', 'ram']
topics=tuple(input("enter the topic").split())
enter the topictoken stst var comm
topics
('token', 'stst', 'var', 'comm')
op=set(input("enter the operators:").split())
enter the operators:in not is isnot or not
op
{'not', 'is', 'or', 'isnot', 'in'}
marks=input("Enter the marks:").split()
Enter the marks:32 45 7 8 9 9
marks
['32', '45', '7', '8', '9', '9']
list(map(int,input("Enter the marks:").split()))
Enter the marks:32 56 78 9 04 
[32, 56, 78, 9, 4]
prices=tuple(map(int, input("Enter the prices:").split()))
Enter the prices:32 45 67  97 66 
prices
(32, 45, 67, 97, 66)
ratings=set(map(int, input("Enter the prices:").split()))
Enter the prices:43 545 4545 455 
ratings
{545, 43, 4545, 455}
perc=list(map(float,input("Enter the perc:").split()))
Enter the perc:34.5 67.8 907.7
perc
[34.5, 67.8, 907.7]
prices=tuple(map(float,input("enter the prices:").split()))
enter the prices:4 2424  4566 6676 
prices
(4.0, 2424.0, 4566.0, 6676.0)
prices=set(map(float,input("enter the price:").split()))
enter the price:3 56 78 90 
prices
{56.0, 90.0, 3.0, 78.0}
a,b=10,20
a
10
b
20
a,b=(10,20)
a
10
b
20
a,b={10,20}
>>> a
10
>>> b
20
>>> a,b,c,d=list(map(int,input("Enter the 4 values:").split()))
Enter the 4 values:23 45 67 89
>>> a
23
>>> b
45
>>> c
67
>>> d
89
>>> usr,pass=input("enter usr and pass:").split()
SyntaxError: invalid syntax
>>> usr,password=input("enter usr and pass:").split()
enter usr and pass:ajay 234
>>> usr
'ajay'
>>> password
'234'
>>> price,discount=list(map(float,input().split()))
2444 56.0
>>> price
2444.0
>>> discount
56.0
>>> a=eval(input())
12
>>> a=eval(input())
23.4
>>> a=eval(input())
'python'
>>> a=eval(input())
(1,2,3,4)
>>> a
(1, 2, 3, 4)
>>> {1,2,3,4}
{1, 2, 3, 4}
>>> a
(1, 2, 3, 4)
>>> a=eval(input())
[1,2,3,4]
>>> a
[1, 2, 3, 4]
