
#打印菱形
for i in range(-3, 4):
    # if i < 0:
    #     perspace = -i
    # else:
    #     perspace = i
    perspace = i if i>0 else -i
    print(' '*perspace+'*'*(7-2*perspace))

#-------------------------------------------
#变形
for i in range(-3, 4):
    if i<0:
        print(' '*(-i)+'*'*(4+i))
    elif i>0:
        print(' '*3+'*'*(4-i))
    else:
        print('*'*7)