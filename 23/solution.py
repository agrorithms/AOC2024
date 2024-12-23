import time
from collections import defaultdict
startTime=time.time()

def readfile(filename):
    with open(filename) as f:
        landict=defaultdict(set)
        threesets=set()
        biglanset=set()
        lansize=0
        part1=0
        for line in f:                              #loop through file, create dictionary of host to connections
            host1=line[:line.index('-')]
            host2=line[line.index('-')+1:-1]
            landict[host1].add(host2)
            landict[host2].add(host1)
            lanparty=landict[host1]
            lanparty.add(host1)
            for c in landict[host1]:                                    #for each item connected to a host1,
                if c in landict[host2] and c != host1 and c!=host2:     #check if it is also connected to host2 (and not host1 or 2)
                    threesets.add((c,host1,host2))                      #then add it to set of 3-sets, if one host start with t, append part1
                    if c[0] =='t' or host1[0]=='t' or host2[0]=='t':
                        part1+=1

            lanparty.add(host1)                                         #add host to its own set, loop through set getting intersection of new
            for j in lanparty:                                          #host lists each time
                lanparty=lanparty&landict[j]
                lanparty.add(j)
            if len(lanparty)>lansize:                                   #after looping through, if lanparty is higher than prior max,
                biglanset=lanparty                                      #save into new set and update lansize
                lansize=len(lanparty)

            lanparty=landict[host2]                                     #repeat that bit for host2
            lanparty.add(host2)
            for h in lanparty:
                lanparty=lanparty&landict[h]
                lanparty.add(h)
            if len(lanparty)>lansize:
                biglanset=lanparty
                lansize=len(lanparty)



        passwordlist=list(biglanset)
        passwordlist.sort()
        return part1, ','.join(passwordlist)




print(readfile('input.txt'))
print(time.time()-startTime)
