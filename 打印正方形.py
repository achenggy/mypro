#打印边长为n的正方形
while True:
    n = int(input("正方形边长>>>"))
    if n < 3:
        print("边长太短,请重新输入")
        continue
    else:
        for i in range(1,n+1):
            if i == 1 or i ==n:
                print('*' *(2*n+1))
            else:
                print("*" + (' ' * (2*n-1))+ "*")
        break


