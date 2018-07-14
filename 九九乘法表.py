
#九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+ "*"+str(i)+ "="+str( i*j), end = "\t")
    print()

#----------------------------------------------------------------

for i in range(1, 10):
    line=''
    for j in range(1, i+1):
        line += '{0}*{1}={2:<4}'.format(j,i,i*j)      #不能去掉0，1，2
    print(line)
#----------------------------------------------------------------
#上三角打印九九乘法表
for i in range(1,10):
    print(' '*7*(i-1),end='')
    for j in range(i,10):
        product = i*j
        end = '  ' if product <10 else ' '
        print(str(i)+"*"+str(j)+"="+str(product),end=end)
    print()
