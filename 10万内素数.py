import datetime

upperlimit = 100000
delta = [0, 0]                           #循环所用的时间
counts = [0, 0]                          #素数的个数

start = datetime.datetime.now()
for _ in range(10):
    counts[0] = 0
    for x in range(2, upperlimit):
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                break
        else:

            counts[0]+=1
delta[0] = (datetime.datetime.now()-start).total_seconds()


#-------------------------------------------------------------------

start = datetime.datetime.now()
for _ in range(10):
    counts[1] = 1
    for x in range(3,upperlimit, 2):
        for i in range(3, int(x**0.5)+1,2):
            if x%i == 0:
                break
        else:
            counts[1] += 1
delta[1] = (datetime.datetime.now()-start).total_seconds()
print(delta, sep = '\t')
print(counts, sep = '\t')