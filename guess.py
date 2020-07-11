import random

r = random.randint(1, 100)
count += 1
while True:
    num = input('請輸入1~100隨機一個數字')
    num = int(num)
    if num == r:
        print('終於猜對了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
         print('比答案大喔!')
    elif num < r:
        print('比答案小喔') 
    print('這是你猜的第', count, '次') 