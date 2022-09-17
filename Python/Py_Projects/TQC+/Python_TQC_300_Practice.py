# %%
a = eval(input())
b = eval(input())
sumList = []
sortList = [a,b]
sortList.sort()
for i in range(sortList[0],sortList[1]+1):
    sumList.append(i)
print(sum(sumList))


# %%
a = eval(input())
b = eval(input())
evenList = []
sortList = [a,b]
for i in range(sortList[0],sortList[1]+1):
    if i % 2 == 0: 
        evenList.append(i)
print(sum(evenList))
    
# %%
