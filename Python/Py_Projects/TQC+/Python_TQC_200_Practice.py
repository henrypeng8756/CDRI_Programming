# %%
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
