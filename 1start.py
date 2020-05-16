#https://anandology.com/python-practice-book/getting-started.html

'''
# Problem 3: 1 \n 1
x=1
def f():
	return x
print(x)
print(f())
'''


'''
#Problem 4: 1 \n 2 \n 1
x=1
def f():
	x=2
	return x
print(x)
print(f())
print(x)
'''

'''
#Problem 5: 1 \n 4 \n 1
x=1
def f():
	x=2
	y=x
	#Note: error message would occur if local variable x is referenced in y before assignment
	return x+y
print(x)
print(f())
print(x)
'''


'''
#Problem 6: 2 9
x=2
def f(a):
	x=a*a
	return x
y=f(3)
print(x,y)
'''


'''
#Problem 7
def count_digits(x):
	return len(str(x))
print(count_digits(1345), count_digits(8736492734))
'''


'''
#Problem 8: hahaha, I use the lambda operator. It makes sense, very simple and minimalistic
istrcmp = lambda x, y: x.lower()==y.lower()
print(istrcmp('hello','hello'))
print(istrcmp('hello', "HelLo"))
print(istrcmp('hello', 'jello'))
'''


'''
#Problem 9: True \n True \n True \n False
print(2<3 and 3>1)
print(2<3 or 3>1)
print(2<3 or not 3>1)
print(2<3 and not 3>1)
'''


'''
#Problem 10: shit, its True. I was initial expecting an error
x=4
y=5
p=x<y or x<z
print(p)
'''


'''
#Problem 11: It won't give an error message
x=2
if x==2:
	print(x)
else:
	print(y)
'''


'''
#Problem 12: Same as #11. Of course, it won't give error
#Oh shit, I was wrong. SyntaxError. But WTF happened?
x=2
if x==2:
	print(x)
else:
	x +
'''


'''
#Problem 13: I don't need a different add.py file
import sys
print(int(sys.argv[1])+int(sys.argv[2]))
#Note: sys.argv[0] is the file name
'''