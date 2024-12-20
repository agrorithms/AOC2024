import time
from collections import defaultdict

startTime=time.time()

def readfile(filename,part2=False):
    with open(filename) as f:
        maze=defaultdict(str)
        for y,line in enumerate(f):
            for x,char in enumerate(line[:-1]):             #create dict of walls and record start and end
                if char=='#':
                    maze[x+y*1j]=char
                elif char=='S':
                    start= x+y*1j
                elif char=='E':
                    end=x+y*1j
        pos=start
        psec=0
        pathdict={start:psec}
        cheatdict={}
        timesave=100
        if part2:
            maxcheat=20
        else:
            maxcheat=2
        while pos != end:                                               #loop through maze finding path forward (no walls and not already pathed)
            for i in range(4):
                if maze[pos+1j**i]!='#' and pos+1j**i not in pathdict:
                    psec+=1
                    pos+=1j**i
                    pathdict[pos]=psec
                    break
            for coord in pathdict.keys():   # for each coord already pathed, if within cheat limit and saves more than min timesave, record start and end points
                if (abs((pos-coord).imag)+abs((pos-coord).real))<=maxcheat and (pathdict[pos]-pathdict[coord]-abs((pos-coord).imag)-abs((pos-coord).real))>=timesave:
                    cheatdict[coord,pos]=pathdict[pos]-pathdict[coord]-abs((pos-coord).imag)-abs((pos-coord).real)
        numcheats=len(cheatdict)
        return numcheats                    #return count of unique start and end points


print(readfile('input.txt'))
print(readfile('input.txt',True))
print(time.time()-startTime)
