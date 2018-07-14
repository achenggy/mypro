#prime number

'''
from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    '''



from math import sqrt
n = int(input('>>>'))
for i in range(2,int(sqrt(n))+1):
    if n % i == 0:
        print(n ,"is not prime")
    else:
        print(n ,"is prime")

