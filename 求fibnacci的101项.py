a = 1
b =1
index =2
print('{0},{1}'.format(0,0))
print('{0},{1}'.format(1,1))
print('{0},{1}'.format(2,1))
while True:
    a,b = b, a+b
    index += 1
    print('{0},{1}'.format(index,a+b))
    if index == 101:
        break
