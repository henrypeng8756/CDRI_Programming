# %%
from curses.ascii import isalpha


i = eval(input())
if i%2 == 0:
    print('{:d}'.format(i),'is an even number.')
else:
    print('{:d}'.format(i),'is not an even number.')

# %%
i = eval(input())
if i % 3 == 0 and i % 5 == 0:
    print(i, 'is a multiple of 3 or 5.')
elif i % 3 == 0:
    print(i, 'is a multiple of 3.')
elif i % 5 == 0:
    print(i, 'is a multiple of 5.')
else:
    print(i,'is not a multiple of 3 or 5.')

# %%
leapYear = eval(input())
if leapYear % 4 == 0 and leapYear % 100 != 0 or leapYear % 400 == 0:
    print(leapYear, 'is a leap year.')
else:
    print(leapYear,'is not a leap year.')

# %%
a = eval(input())
b = eval(input())
opt = str(input())
if opt == '+':
    print(a+b)
elif opt == '-':
    print(a-b)
elif opt == '*':
    print(a*b)
elif opt == '/':
    print(a/b)
elif opt == '//':
    print(a//b)
else:
    print(a%b)

# %%
i = input()
if i.isalpha() == True:
    print(i, 'is a alphabet')
elif i.isdigit() == True:
    print(i, 'is a number.')
else:
    print(i, 'is a symbol.')

# %%
score = eval(input())
if score >= 80:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
else:
    print('F')


# %%
price = eval(input())
if price >= 38000:
    print('%.1f' - '%d' * 0.7 % (price, price))
elif price >= 28000:
    print('%.1f' - '%d' * 0.8 % (price, price))
elif price >= 18000:
    print('%.1f' - '%d' * 0.9 % (price, price))
elif price >= 8000:
    print('%.1f' - '%d' * 0.95 % (price, price))
else:
    print('%.1f' %price)
# %%