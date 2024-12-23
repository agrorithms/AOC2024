import time
from collections import defaultdict
startTime=time.time()

def readfile(filename):
    with open(filename) as f:
        part1=0

        seqdict=defaultdict(int)
        for j,line in enumerate(f):
            num=int(line[:-1])
            difflist=[]
            buyerset=set()
            for i in range(2000):                               #loop each num 2000 times, perform operation,mix,prune
                num2=((64*num) ^ num) %16777216
                num3=(num2//32 ^ num2)%16777216
                num4=(num3*2048 ^num3) %16777216
                price=num4%10
                difflist.append((price-num%10,price))           #save price change and price in list of tuples
                num=num4
                if len(difflist)>3:                             #after 4 price changes, get sequence of last 4 changes
                    seq=(difflist[i-3][0],difflist[i-2][0],difflist[i-1][0],difflist[i][0])
                    if seq not in buyerset:
                        buyerset.add(seq)                       #if sequence does not exist for this buyer, record sequence
                        seqdict[seq]+=difflist[i][1]            #and aggregate sequence total

            part1+=(num4)
        return part1, max(seqdict.values())


print(readfile('input.txt'))
print(time.time()-startTime)
