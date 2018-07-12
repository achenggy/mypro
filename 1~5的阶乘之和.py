jc  = 1         #factorial
sum = 0
for i in range(1, 6):
    jc *= i
    print(jc)
    sum += jc
print(sum)


'''
factorial=1
sum = 0
for i in range(1,6):
    for j in range(1, i+1):
        factorial *= j
    sum += factorial
    print(factorial)
    factorial = 1
print(sum)
'''




