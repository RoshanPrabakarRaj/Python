Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x="sdbs"
>>> len(x)
4
>>> y=42
>>> print(y,x)
42 sdbs
>>> print y,x
SyntaxError: Missing parentheses in call to 'print'
>>> a=roshan@gmail.com
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a=roshan@gmail.com
NameError: name 'roshan' is not defined
>>> a="roshan@gmail.com"
>>> a.split(@)
SyntaxError: invalid syntax
>>> a.split('@')
['roshan', 'gmail.com']
>>> b="()ab()"
>>> b=b.replace('(',''))
SyntaxError: invalid syntax
>>> b=b.replace('(','')
>>> print(b)
)ab)
>>> b=b.replace(')','')
>>> print(b)
ab
>>> x=1+4
>>> y=5*10
>>> print(x+y)
55
>>> 13/3
4.333333333333333
>>> floor(13/3)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    floor(13/3)
NameError: name 'floor' is not defined
>>> math.floor(13/3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    math.floor(13/3)
NameError: name 'math' is not defined
>>> round(9.6)
10
>>> for a in range(0,10):
	a=a+100
	print(a)

	
100
101
102
103
104
105
106
107
108
109
>>> if 5 in range(0,10)
SyntaxError: invalid syntax
>>> 5 in range(0,10)
True
>>> a=5
>>> b=5
>>> a,b
(5, 5)
>>> a=[1,2,3,4]
>>> print(a)
[1, 2, 3, 4]
>>> a.split(',')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.split(',')
AttributeError: 'list' object has no attribute 'split'
>>> a="roshan"
>>> a.upper()
'ROSHAN'
>>> a.split('s')
['ro', 'han']
>>> c=[1,2,3]
>>> c.append(4)
>>> print(c)
[1, 2, 3, 4]
>>> A<b
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    A<b
NameError: name 'A' is not defined
>>> 'A'<'b'
True
>>> a=5
>>> b=6
>>> if a==b:
	print("same")
	else
	
SyntaxError: invalid syntax
>>> a=5
>>> b=6
>>> if a==b:
	print("same")

	
>>> 
>>> a=5
>>> b=6
>>> if a==b:
	print("same")
	else:
		
SyntaxError: invalid syntax
>>> if a==b:
	print("same")
else:
	print("diff")

	
diff
>>> a=[1,2,3,4]
>>> b=[5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> a[0]
1
>>> a[5
  ]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a[5
IndexError: list index out of range
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a[5]
IndexError: list index out of range
>>> c=a+b
>>> c[5
  ]
6
>>> 
