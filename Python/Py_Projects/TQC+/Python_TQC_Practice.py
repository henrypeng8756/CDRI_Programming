# %%
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print('|%5d %5d|'%(a,b))
print('|%5d %5d|'%(c,d))
print('|%-5d %-5d|'%(a,b))
print('|%-5d %-5d|'%(c,d))

# %%
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print('(',x1,',',y1,')')
print('(',x2,',',y2,')')
print('Distance = %.4f'%(((x1-x2)**2+(y1-y2)**2)**0.5))

# %%
a = eval(input())
b = eval(input())
opt = input()
if opt == '+':
    print('%d'%(a+b))
elif opt == '-':
    print('%d'%(a-b))
elif opt == '*':
    print('%d'%(a*b))
elif opt == '/':
    print('%d'%(a/b))
elif opt == '//':
    print('%d'%(a//b))
else:
    print('%d'%(a%b))

# %%
i = eval(input())
if i >= 10 and i <= 16:
    print(str.upper(str((hex(i)))).lstrip('0X'))
else:
    print(i)

# %%
a = eval(input())
numSum = 0
for divsum in range(1,a+1):
    if divsum % 5 == 0:
        numSum += divsum
print(numSum)

# %%
n = eval(input())
numSum = 0
for times in range(2,n+1): #n=8
    numSum += 1/(((times-1)**0.5)+((times)**0.5))
print('%.4f'%numSum)
    
# %%
evenCount = 0
for numCount in range(10):
    i = eval(input())
    if i % 2 == 0:
        evenCount += 1
print('Even numbers: %d' %(evenCount))
print('Odd numbers: %d' %(10-evenCount))

# %%
numList = []
while True:
    n = int(input())
    if n != 9999:
        numList.append(n)
        continue
    else:
        print(min(numList))
        break

# %%
def compute():
    i = eval(input())
    j = eval(input())
    print('%d' %(i**j))
compute()

# %%
# x=(-b+(b**2-(4*c*a)**0.5)/(2*a)
# x=(-b-(b**2-(4*c*a)**0.5)/(2*a)

# %%
cards = []
cardsSum = 0
for i in range(5):
    cards.append(input())
for j in range(5):
    if cards[j] == 'A':
        cardsSum += 1
    elif cards[j] == 'J':
        cardsSum += 11
    elif cards[j] == 'Q':
        cardsSum += 12
    elif cards[j] == 'K':
        cardsSum += 13
    else:
        cardsSum += eval(cards[j])
print(cardsSum)

# %%

