import time

startTime=time.time()

def readfile(filename,part2=False):
    def checkmatch(keylist,locklist):
        '''
        checks last item in keylist to see if it fits with any items in locklist.
        '''
        sum=0
        for lock in locklist:
            pairfit=True
            for i in range(5):
                if keylist[-1][i]+lock[i]>5:
                    pairfit=False
            if pairfit:
                sum+=1
        return sum

    with open(filename) as f:
        keylist=[]
        locklist=[]
        newgroup=True
        part1=0
        key=False
        for line in f:
            if newgroup:                            #if new group, check if last group has any fits
                if key:
                    part1+=checkmatch(keylist,locklist)
                else:
                    part1+=checkmatch(locklist,keylist)

            if line =="#####\n" and newgroup:      #determine if next group is a key or lock
                key=False
                newgroup=False
                locklist.append([0,0,0,0,0])
                continue
            elif line == '.....\n' and newgroup:
                key=True
                newgroup=False
                keylist.append([5,5,5,5,5])
                continue
            elif line == '\n':                  #determine if new group
                newgroup=True
                continue

            for i,char in enumerate(line[:-1]): # alter the current group's key/lock lengths
                if char=='.':
                    if key:
                        keylist[-1][i]-=1
                else:
                    if not key:
                        locklist[-1][i]+=1

        if key:                                #run this check one last time on final key/lock
            part1+=checkmatch(keylist,locklist)
        else:
            part1+=checkmatch(locklist,keylist)
        return part1

print(readfile('input.txt'))
print(time.time()-startTime)
