# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%

from cmath import pi
from email.contentmanager import raw_data_manager
from importlib import import_module
from tkinter import N, Y
from tkinter.tix import InputOnly


print(1)
print(1+2)
print(1-25*12345)
print(12.345*98.7864541)

# %%

num1=50
num2='50'
num3=50>60
num4=15.51

print(num1)
print(num2)
print(num3)
print(num4)
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))

# %%

print(int('10'))
print(int(3.14))
print(int(True))
print(int(False))
print(str(1.23))

# %%
print(1+2)
print(1.5+2.3)

print(15-3)
print(20-True)

print(12*21)
print('ABC'*2)

print(6/3)
print(12/True)

print(8//3)
print(108//11)

print(28%10)
print(12.5%10)

print(5**3)
print(3**5)

# %%
print(123 == '123')
print('ABC' == 'abc')

''' == = 是不是, = = 右邊數值等於左邊
'''
print(True == 1)
print(False == 0)

print ((3>2) == True)
print(3>2 == True)

# %%
print((1>2) & (3>2))
print((1>2) and (3>2))

print((1>2) | (3>2))
print((1>2) or (3>2))

print(not(1>2))

# %%
a=3
b=5
c=7
a,b,c = 3,5,7
a *= b
print(a)
c %= 5
print(c)


# %%
# single line comment

'''multiple line comment 
just like this
'''

# %%
name=input()
print(name)

# %%
name=input('Please insert your name:')
print(name)

# %%
PI = 3.1415926
radius = eval(input("Please enter radius value:"))
print('Radius is', radius, "Circular Area is", PI * radius**2 )

# eval 會協助自動轉換至對應的資料型態, 可以使用變數的string, 但是無法單用strings 
#%%
numA=eval(input('First Number'))
numB=eval(input('Second Number'))
numC=eval(input('Third Number'))
numD=eval(input('Forth Number'))

# %%
print(1)
print(1,2,5,True,'xyz')

# %%
name1='Henry'
print('Hello', name1, sep='^^^', end='\n')
print('nice to meet you', end=' ')
print('too')
print('So, ', end='')
print('What is your name', end='???')
print('Hello', name1, sep='', end='\n')

# %%
yourName = input('what is your name')
print(yourName)

# %%
print('Hello, %s' % 'World!')
print('you only have $%d' % 666)
print('%d divide %d is %f' % (20,7,20/7))
print('%5d divide %5d is %.3f' % (20,7,20/7))
print('%-5d divide %-5d is %.3f' % (20,7,20/7))
print('%-8d divide %-8d is %10.3f' % (20,7,20/7))

# %%
PI=3.1415926
print('{:.2f}'.format(PI))
print('{:+.2f}'.format(PI))
print('{:.0f}'.format(PI))
print('{:0>2d}'.format(5))
print('{:x<4d}'.format(10))
print('{:,}'.format(1000000))
print('{:10d}'.format(13))
print('{:<10d}'.format(13))
print('{:^10d}'.format(13))
print('{:.2%}'.format(PI))
print('{:.2e}'.format(100000000000))

# %%
print('{0:d}-{2:b}-{1:o}-{0:x}'.format(10,20,30))
# d eicmal
# b inary
# o ctal
# he x 
# f loat
# s tring 

# %%
print('{0:d} divide {1:d} is {2:f}'.format(10, 3, 10/3))
print('{0:5d} divide {1:5d} is {2:10.2f}'.format(10, 3, 10/3))
print('{n1:5d} divide {n2:5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:<5d} divide {n2:<5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:>5d} divide {n2:>5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:!^5d} divide {n2:?^5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))

# %%
#print('n1%!^5d divide n2%?^5d is r%.2f' % (n1=10, n2=3, r=10/3))
#print('0%!^5d divide 1%?^5d is 2%.2f' % (10, 3, 10/3))
#print('0%^5d divide 1%?^5d is 2%.2f' % (10, 3, 10/3))
#print('0%5d divide 1%?^5d is 2%.2f' % (10, 3, 10/3))
#print('0%5d divide 1%^5d is 2%.2f' % (10, 3, 10/3))

print('0%5d divide 1%5d is 2%.2f' % (10, 3, 10/3))

# %%
sideLength= eval(input('Please Enter Side of the Square: '))
print('Square Side Lengths: ', '{:.2f}'.format(sideLength))
print('Square Perimeter: ', '{:.2f}'.format(sideLength*4))
print('Square Area:', '{:.2f}'.format(sideLength**2))

# %%
long = eval(input('請輸入正方形邊長:'))
print("邊長為:"+'{:.2f}'.format(long), 
      "\n周長為:"+'{:.2f}'.format(4*long), 
      "\n面積為:"+'{:.2f}'.format(long**2), 
            )

# %%
def CtoF1(degreeC):
      degreeF = degreeC * 1.8 + 32 
      print('{:.1f}'.format(degreeC), 'Celcius is ', '{:.1f}'.format(degreeF), 'Fahrenheit')
tempertureC = eval(input('Please Enter Celcius: '))
CtoF1(tempertureC)

# %%
def CtoF2(degreeC2):
      degreeF2 = degreeC2 * 1.8 + 32
      return '{:.1f}'.format(degreeF2)
tempertureC2 = eval(input('Please Enter Celcius: '))
CtoF2(tempertureC2)

# %%
def CtoF2(degreeC2):
      degreeF2 = degreeC2 * 1.8 + 32
      return '{:.1f}'.format(degreeF2)
CtoF2(35.666)

# %%
def teaTime(dessert, drink = 'Black Tea'):
      print('My Dessert: ', dessert, ' ; My Drink: ', drink, sep="")
teaTime('Macaron','Coffee')
teaTime('Panini')
teaTime(drink = 'Milk Tea', dessert= 'Sandwich')
teaTime('Red Bean Cake', drink= 'Green Tea')
# teaTime(drink= 'Green Tea', 'Red Bean Cake')
#      teaTime(drink= 'Green Tea', 'Red Bean Cake')
#                                                 ^
#SyntaxError: positional argument follows keyword argument

# %%
def autoteaTime(myDessert = 'Cheese Cake', myDrink = 'Water'):
      print('Your Dessert: ', '{:s}'.format(myDessert), ' ; Your Drink: ', '{:s}'.format(myDrink), sep="")
orderDessert = str(input('Please Select Your Dessert: '))
orderDrink = str(input('Please Select Your Drink: '))
autoteaTime(orderDessert, orderDrink)

# %%
def cal(x,y):
      div = x // y
      mod = x % y
      return div, mod
a, b = cal(120, 7)
print('120 divide 7 | floor division =', a, ', modulus =',b )
c, d = cal(250, 15)
print('250 divide 15 | floor division =', c, ', modulus =',d )

# %%
x = eval(input())
y = eval(input())
def cal(x,y):
      div = x // y
      mod = x % y
      return div, mod
a, b = cal(x, y)
print( x, 'divide', y, '| floor division =', a, ', modulus =',b )
c, d = cal(x, y)
print( x, 'divide', y, '| floor division =', c, ', modulus =',d )
# %%
x = 100
def test():
      print(x)
test()

# %%
X = 100
def test():
      Y = 200
      return Y
test()
print(test())
Y = test()
print(Y) 

# %%
a = 'Happy' + 'Birthday' + 'to' + 'you'
print(a)

b = 3*'Yeah!'
print(b)

c = 'X' > 'M'
print(c)
# Due to unicode X unicode value is larger than M in unicode 

d = '123' > '456'
print(d)

e = 'for' not in 'forever'
print(e)

# %%
def int01():
      A = 'HENRY'
      return A

def int02():
      B = 'henry'
      return B
A = int01()
B = int02()
print(int01()>int02())
print(X > Y)

# %%
def int01():
      A = str(input())
      return A

def int02():
      B = str(input())
      return B
A = int01()
B = int02()
int01()
int02()
print(A)
print(B)
print(int01()>int02())
print(A > B)

# %%
def a():
      a = 'for'
      return a
def b():
      b = 'forever'
      return b
print(a())
print(b())
print(a() not in b())
a = a()
b = b()
print(a)
print(b)
print(a not in b)

# %%
S = 'Python程式運算'
print(S[2:5])
# expecting tho
print(S[3:8])
# expecting hon程式
print(S[5:-1])
# expecting n程式運
print(S[:-2])
# expecting Python程式
print(S[2:])
# expecting thon程式運算

# %%
S1 = 'HappyNewYear'
S2 = 'happynewyear'
S3 = 'new'
len(S1)
print(S1==S2)
max(S1)
print(S3 in S1)
print(S1[4:9])

# %%
print(ord('A'))
print(ord('$'))

print(chr(65))
print(chr(36))

# %%
X = 'Good Afternoon! How Are you?'
print(X.upper())
print(X.lower())
print(X.swapcase())
print(X.capitalize())
print(X.title())
print(X.replace('oo','xx'))
print(X)

# %%
print(str.isupper('abcde'))
print(str.isupper('ABCDE'))
print(str.islower('abcde'))
print(str.islower('Abcde'))
print(str.isidentifier('a1bcde'))
print(str.isidentifier('1abcde'))
print(str.isspace('  a    '))
print(str.isspace('       '))
print(str.istitle('It Is ok'))
print(str.istitle('It Is Ok'))
print(str.isalpha('ABCDE'))
print(str.isalpha('abcde'))
print(str.isalpha('abcde1'))
print(str.isdigit('12345'))
print(str.isdigit('123.45'))
print(str.isdigit('I'))
print(str.isdigit('一'))
print(str.isdecimal('12345'))
print(str.isdecimal('123.45'))
print(str.isdecimal('I'))
print(str.isdecimal('一'))
print(str.isnumeric('12345'))
print(str.isnumeric('123.45'))
print(str.isnumeric('I'))
print(str.isnumeric('一'))

print('----------------------------')

print('abcde'.isupper())
print('ABCDE'.isupper())
print('abcde'.islower())
print('ABCDE'.islower())
print('a1bcde'.isidentifier())
print('1abcde'.isidentifier())
print('  a   '.isspace())
print('      '.isspace())
print('It Is ok'.istitle())
print('It Is Ok'.istitle())
print('ABCDE'.isalpha())
print('abcde'.isalpha())
print('abcde1'.isalpha())
print('12345'.isdigit())
print('123.45'.isdigit())
print('I'.isdigit())
print('一'.isdigit())
print('12345'.isdecimal())
print('123.45'.isdecimal())
print('I'.isdecimal())
print('一'.isdecimal())
print('12345'.isnumeric())
print('123.45'.isnumeric())
print('I'.isnumeric())
print('一'.isnumeric())

# %%
Y = 'HiHiHiHiHi'
print(Y.count('Hi'))
print(Y.startswith('Hi'))
print(Y.startswith('HiH'))
print(Y.endswith('HiH'))
print(Y.endswith('iHi'))
print(Y.find('iHi'))
print(Y.rfind('iHi'))

# %%
X = 'A B C D E'
Y = X.split()
print(Y)

# %%
X = '1,3,5,7,9'
Y = X.split(',')
print(Y)

# %%
print('     abcde       '.strip())
print('abcxyzd ef'.strip('abcdef'))

# %%
Z = 'tw.yahoo.com'
print(Z.strip('.omtw'))
print(Z.rstrip('tomw'))
print(Z.strip('tomw'))

# %%
X = 'Hello Python'
print(X.center(20))
print(X.ljust(20))
print(X.rjust(20))
print(X.zfill(6))
print(X.zfill(20))

# %%
PI=3.1415926
print('{:.2f}'.format(PI))
print('{:+.2f}'.format(PI))
print('{:.0f}'.format(PI))
print('{:0>2d}'.format(5))
print('{:x<4d}'.format(10))
print('{:,}'.format(1000000))
print('{:10d}'.format(13))
print('{:<10d}'.format(13))
print('{:^10d}'.format(13))
print('{:.2%}'.format(PI))
print('{:.2e}'.format(100000000000))

# %%
print('{0:d}-{2:b}-{1:o}-{0:x}'.format(10,20,30))
# d eicmal
# b inary
# o ctal
# he x 
# f loat
# s tring 

# %%
print('{0:d} divide {1:d} is {2:f}'.format(10, 3, 10/3))
print('{0:5d} divide {1:5d} is {2:10.2f}'.format(10, 3, 10/3))
print('{n1:5d} divide {n2:5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:<5d} divide {n2:<5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:>5d} divide {n2:>5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:!^5d} divide {n2:?^5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))

# %%
print(abs(50))
print(abs(-50))
print(pow(2,5))
print(pow(3,4))
print(divmod(100,8))
print(divmod(125,9.5))

# %%
print(max(10,20,30))
print(max(-10,-20,-30))
print(max(True,-20,-30))
print(min(1,3,False))
print(max('a','b','c'))
print(min('A','b','c'))

# %%
print(bin(100))
print(oct(100))
print(hex(100))

# %%
print(int(666.666))
print(int('666'))
# print(int('666.666'))
# print(int('六六六'))

# %%
print(float(666))
print(float('666'))
print(float('666.666'))
# print(float('六六六'))

# %%
print(round(123.123))
print(round(123.123,2))
print(round(-567.567))
print(round(-567.567,2))
print(round(5.5))
print(round(6.5))
print(round(-5.5))
print(round(-6.5))
# print(round('999'))

# %%
import random
num = random.randint(1,3)
answer = eval(input('Please Guess the Number from 1 ~ 3: '))
print(num,'==',answer, 'is', num == answer)

# %%
import math
print(max(10,9,-8,200,77,-120,50))
print(min(10,9,-8,200,77,-120,50))
print(10**2*math.pi)
print(math.gcd(616,1331))

# %%
print(format(123,'^10'))
print(format(123,'!^10'))
print(format(123456789,','))

# %%
print(format(1234.5678,'10.2f'))
print(format(1234.5678,'<10.2f'))

# %%
def compute(x,y):
      multi = x*y
      return multi
x = eval(input())
y = eval(input())
print(compute(x,y))

# %%
a = 100
b = 200
if a>b:
      print(a)

# %%
x = 15
y = 10 
if x > y :
      z = x - y
      print('x is',z ,'more than y')

# %%
score = eval(input('Please Insert Your Math Score: '))
if score >= 60:
      print('Pass!')
else:
      print('Fail!')

# %%
num1 = 50
num2 = 40
if num1 > num2:
      print('True !')

print('===========')
if bool(num1 > num2):
      print('True !')

# %%
num2 = eval(input())
if num2 > 100:
      num3 = 30
print(num3)
# %%
# def test():
#       numa = 30
# print(numa)
# will Fail

# %%
score = eval(input('Please Insert Your Math Score: '))
if score >= 90:
      print('You got an A!')
elif score >= 80:
      print('You got a B!')
elif score >= 70:
      print('You got a C!')
elif score >= 60:
      print('You got a D!')
else:
      print('You failed!')

# %%
score = eval(input('Please Insert Your Math Score: '))
if score >= 90:
      print('You got an A!')
else:
      if score >= 80:
            print('You got a B!')
      else:
            if score >= 70:
                  print('You got a C!')
            else:
                  if score >= 60:
                        print('You got a D!')
                  else:
                        print('You failed!')
# %%
i = 0
while i < 5:
      print(i)
      i = i + 1

# %%
x = 'Please Spell 快樂 in English:'
answer = input(x)
while answer.upper() != "HAPPY":
      answer = input('Wrong! Please try again!\n %s' % x)
else:
      print('Correct!')

# %%
list(range(5))
print(list(range(5)))
# range(stop)
list(range(1,10))
# range(start,stop)
list(range(10,-10,-2))
# range(start,stop,step)

# %%
for i in range(5):
      print(i)

# %%
name = 'Bob'
for i in range(len(name)):
      print(i,name[i])

# %%
name ='Bob'
for i in name:
      print(i, name[0:3])
      
# %%
word = 'Please Spell 好 in English: ' 
answer = input(word)
while answer.upper() != 'GOOD':
      if answer.upper() == 'QUIT':
            print('Practice makes perfect!\nSee you next time!')
            break
            print('Bye!')
      elif answer.upper() == 'FUCK':
            print('FUCK YOU')
            break
            print('FUCK OFF')
      answer = input('Wrong,\n%s' % word)
else:
      print('Correct!')

# %%
i = 0
while i < 10:
      i = i + 1
      if i % 3 != 0:
            continue
            i = i + 2
      print(i)

# %%
for n in range(1,5,2):
      print(n, end='')
print(n)

# %%
sum = 0
n = 8 
for i in range(1,n+1,2):
      sum += i
print(sum)

# %%
# list = []
# tuple = ()
# dict = {}

# %%
X = list()
print(X)

Y = list([1,2,3])
print(Y)

# %%
X2 = []
print(X2)

Y2 = [1,2,3]
print(Y2)

# %%
list1 = [1, 2.5, 'xyz', False]
print(type(list1))
print(list1[0])
print(list1[2])

# %%
L = [3,6,9,12,15,18,21,24,27,30]
del L[2]
del L[3]
print(L)

# %%
a = [3,6,9]
b = [2,5,8.5,'Hello']
c = []
d = [16,[a,b]]
e = a + b

b[0] = 42
x = a[1]
y = b[1:3]
z = d[1][0][1]
print(x)
print(y)
print(z)


# %%
print([1,2,3]+[4,5,6])
print([1,2,3]+['A','B','C'])
print([1,2,3]+['A', True, 2.5, 0])

# %%
print(3*[1,2,3])
print(['A', 2, 10.5, True]*3)

# %%
print([1,3,4,'X']==['X',3.5,1])
print([1,2,3]==[3,2,1])

# %%
print(3 in [1,2,3,4,5])
print('Y' in ['XYZ','ABC'])
print('XYZ' in ['XYZ','ABC'])

# %%
L = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(L[1:5])
print(L[2:-2])

# %%
listc=[i for i in range(10)]
print(listc)
listc2=[j+3 for j in range(10)]
print(listc2)

# %%
list1 = [1,3,5,7,9]
list2 = [2,5,8,11,14]
list1.append(11)
print(list1)
list1.extend(list2)
print(list1)
print(list1.count(11))
print(list1.index(9))
list1.insert(3,999)
print(list1)
list1.pop()
print(list1)
list1.remove(5)
print(list1)
list1.reverse()
print(list1)
list1.pop(5)
print(list1)

# %%
X = [1,3,2,4,5]
print(sorted(X))
print(X)
X.sort()
print(X)

# %%
print(pow(2,7,6))
print(2**7%6)

# %%
tup = tuple()
print(tup)
tup2 = tuple((1,3,5))
print(tup2)
tup3 = ()
print(tup3)
tup4 = (2,4,6)
print(tup4)

# %%
a = (3,5,2,6)
b = ()
c = (2,[4,6],(10,11,12))
print(a[1])
print(a[1:3])
print(c[1][1])

# %%
tup = (3,False,'XYZ')
# tup = a,b,c
a,b,c = tup
print(a)
print(b)
print(c)

# %%
a, *b=(1,3,5,7,9)
print(a)
print(b)
x, *y, z=(2,4,6,8,10)
print(x)
print(y)
print(z)

# %%
x1 =[(1,2),[3,4]]
y1 =([5,6],(7,8))
x1[0] = 20
print(x1)
# y1[0] = 30

# %%
x2 =[(1,2),[3,4]]
y2 =([5,6],(7,8))
# x2[0][0] = 20
y2[0][0] = 30
print(y2)

# %%
x3 = [(1,2),[3,4]]
y3 = list((i for i in range(10)))
print(x3)
print(y3)

# %%
i = eval(input('Please give a number: '))
sumList = list((i for i in range(0,i+1,7)))
print('The sum of multiples of 7 from 1 to %d is %d' %(i,sum(sumList)))

# %%
A = set()
A.add(3)
A.add('ABC')
A.add(True)
print(A)

# %%
X = {'a','b',1,2}
Y = {1,2,'a','b'}
print(X==Y)
print(X)
print(Y)

# %%
S1 = {1,1,2,2,2,2,3,3,5,5,6,6,6,}
S2 = {6,3,1,5,2,2,5,3,1,2}
print(S1==S2)
print(S1)
print(S2)

# %%
S1 = {1,2,3,4,5}
S2 = {3,4,5,6,7}
# S3 = S1 +S2 
print(S1-S2)
# print(S1[1:3])
# print(S2[2])

# %%
A = {1,5,3,7,9,5,7,3}
print(len(A))
print(max(A))
print(min(A))
print(sum(A))

# %%
