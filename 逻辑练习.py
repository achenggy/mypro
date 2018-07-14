
#--------------------------------------------------
# 给一个半径，求圆的周长和面积。圆周率3.14
r = int(input('r='))
print('area='+str(3.14*r*r))
print('circumference='+str(2*3.14*r))

#-------------------------------------------------

#输入两个数，比较大小后，从小到大升序打印

a = input('first: ')
b = input('second: ')
if a > b:
    print(b,a)
else:
    print(a,b)
#--------------------------------------------------

print(b,a) if a>b else print(a,b)
#--------------------------------------------------

#输入n个数，求每次输入后的算数平均数

n = 0
sum = 0
while True:
    i = input('>>>')
    if i == 'quit':
        break
    n += 1
    sum += int(i)
    avg = sum / n
    print(avg)