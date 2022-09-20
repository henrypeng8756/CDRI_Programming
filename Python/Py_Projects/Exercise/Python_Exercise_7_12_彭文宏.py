
# %%
from curses.ascii import isdigit
from operator import truediv


while True:
    num = input("請輸入列數(需為奇數，按0結束)：")

    if num.isdigit():  # 判定num是否為數值
        new_num = int(num)

        if new_num == 0:  # 若數值為0則結束迴圈
            print("再見")
            break
        elif new_num % 2 == 0:  # 若數值為偶數則讓使用者重新輸入
            continue
        else:
            for i in range(-new_num+1, new_num):
                for space in range(1, abs(i)+1):
                    print(" ", end="")
                for star in range(1, (new_num+1)-abs(i)):
                    print("* ", end="")
                print()

    else:
        continue

# %%
while True:
    i = input('請輸入列數(必須為奇數，輸入0離開：')

    if i.isdigit():
        num = int(i)

        if num == 0:
            print('再見')
            break
        elif num % 2 == 0:
            continue
        else:
            for line in range(-num+1, num): # (-2,3)
                for space in range(1, abs(line)+1): #range(1,1) = range(0) space =  line= 0
                    print(' ', end='')
                for star in range(1, (num+1)-abs(line)): #range(1,3) range(2) star 2 num= 3 line= 0
                    print('* ', end='')
                print()
    else:
        continue
# %%
