# %%
a = eval(input())
b = eval(input())
sumList = []
sortList = [a,b]
sortList.sort()
for i in range(sortList[0],sortList[1]+1):
    sumList.append(i)
print(sum(sumList))

a = eval(input())
b = eval(input())
sortList = [a,b]
sortList.sort()
numbSum = 0
for i in range(sortList[0],sortList[1]+1):
    numbSum += i
print(numbSum)

# %%
a = eval(input())
b = eval(input())
evenList = []
sortList = [a,b]
for i in range(sortList[0],sortList[1]+1):
    if i % 2 == 0: 
        evenList.append(i)
print(sum(evenList))
    
a = eval(input())
b = eval(input())
sortList = [a,b]
sortList.sort()
numbSum = 0
for i in range(sortList[0],sortList[1]+1):
    if i % 2 == 0:
        numbSum += i
print(numbSum)

# %%
i = eval(input())  
for line in range(1,i+1): 
    for numb in range(1,line+1): 
        print('%4d' %(line*numb), end ='')
    print()

# %%
a = eval(input())
numbSum = 0
for numb in range(1,a+1):
    if numb % 5 == 0:
       numbSum += numb
print(numbSum)

# %%
numb = input()
print(numb[::-1])
# %%

# %%

# %%

# %%
