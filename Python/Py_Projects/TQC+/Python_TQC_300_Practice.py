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
i = eval(input())  # i =2
for line in range(1,i+1): # (1,3)
    for numb in range(1,line+1): # (1,3)
        print('%4d' %(line*numb), end ='')
    print('\n')

# %%

# %%
959/2


# %%
