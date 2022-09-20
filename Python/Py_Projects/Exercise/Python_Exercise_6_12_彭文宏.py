# %%
import enum
from unittest import result


def cleanstrList(dirtyList):
    dirtyList = str(dirtyList)
    dirtyList = dirtyList.strip('[]')
    dirtyList = dirtyList.replace(',','')
    print(dirtyList)

numList=[]
valueNum = eval(input('Enter a number: '))
for valueNum in range(1,valueNum+1):
    numList.append(valueNum)
    cleanstrList(numList)
cleanstrList(numList)
for valueNum in range(1,valueNum+1):
    numList.pop()
    cleanstrList(numList)

# %%
itemNumber = eval(input('Enter a number: '))
for i in range(1, itemNumber+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print('\n')

for i in range(1, itemNumber+1):
    for j in range(1,itemNumber+2-i):
        print(j, end=' ')
    print('\n')
        
# %%
nameList = ['Henry','Ken','Wen']
for i, name in enumerate(nameList):
    print('No.%d : %s ' %(i+1,name))

# %%
nameList = ['Henry','Ken','Wen']
for i, name in enumerate(nameList,1):
    print('No.%d : %s'%(i,name))

# %%
countryCode = ['TW','JP','US','UK','AU']
countryNum = ['886','81','1','44','62']
code = zip(countryCode,countryNum)
for i in code:
    print(i)

# %%
countryCode = ['TW', 'JP', 'US', 'UK', 'AU']
countryNum = ['886', '81', '1', '44', '62']
info = {}
for name, i in zip(countryCode,countryNum):
    info[name] = i
print(info)

# %%
numList = [1,2,3,4,5]
def cal(x):
    return x**2

result1 = list(map(cal,numList))
print(result1)

result2 = list(map(lambda x:x**3, numList))
print(result2)

# %%
numList1 = [1,2,3,4,5]
numList2 = [10,20,30]
def cal(x,y):
    return x+y 
result = list(map(cal,numList1,numList2))
print(result)

# %%
numList1 = ['100','200','300','400']
newList = list(map(int,numList1))
print(newList)

# %%
list1 = [0, 2.5, False, 30]
def cal(x):
    if x > 0:
        return x
ans1 = list(filter(cal,list1))
print(ans1)

ans2 = list(filter(lambda x:x>1, list1))
print(ans2)

# %%
ans1 = list(filter(None,[0,1,2,3,4,5]))
print(ans1)

list1 = [i for i in range(6)]
def cal(x):
    if x%2==0:
        return x
ans2 = list(filter(cal,list1))
print(ans2)

ans3 = list(filter(lambda x:x%2==0,list1))
print(ans3)

# %%
def show(*args):
    print(args)
show(3)
show(3,12,41)

# %%
########
def show(*aa):
    for i in aa:
        return aa
show(4)    

# %%
ans1 = lambda: 2020
print(ans1())

# %%
ans2 = list(map(lambda x:x*10, [i for i in range(1,6)]))
print(ans2)

# %%
ans3 = lambda x,y: x+y
print(ans3(2,9))

# %%
ans4 = lambda *args : sum(args)
print(ans4)

#%%
ans5 = lambda **kwargs : kwargs
print(ans5(name='Henry', age=15)) 

# %%
x = []
for i in range(1,6):
    x.append(i)
print(x)

# %%
x = [i for i in range(1,6)]
print(x)

# %%
x = [eval(i) for i in range(1,6)]
print(x)

# %%
x = [ 1 for i in range(1,6)]
print(x)

# %%
x = [0 for _ in range(1,6)]
print(x)

# %%
x = [i==0 for i in range(1,6)]
print(x)

# %%
x = [ 1 for _ in range(1,6)]
print(x)

# %%
