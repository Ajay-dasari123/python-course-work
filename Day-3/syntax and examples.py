Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> t=99.0
>>> type(t)
<class 'float'>
>>> y=12+8j
>>> type(y)
<class 'complex'>
>>> s='python'
>>> type(s)
<class 'str'>
>>> s="python"
>>> type(s)
<class 'str'>
>>> s='python'
>>> s='java'
>>> s
'java'
>>> s='python'
>>> id(s)
1561870646944
>>> s='java'
>>> id(s)
1561878606016
>>> l=[1,2,3,4]
>>> id(l)
1561913912960
>>> l.append(40)
>>> l.append(90)
>>> l
[1, 2, 3, 4, 40, 90]
>>> id(l)
1561913912960
