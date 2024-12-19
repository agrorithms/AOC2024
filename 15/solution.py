import time
from collections import defaultdict

startTime=time.time()

def readfile(filename,part2=False):
    with open(filename) as f:
        mapdict=defaultdict(str)
        mapdict2=defaultdict(str)
        directions=[]
        inputswitch=True
        part1=0
        part2ans=0
        for y,line in enumerate(f):
            if line=='\n':
                inputswitch=False

            for x, char in enumerate(line[:-1]):
                if inputswitch:
                    if char =='O' or char =='#':
                        mapdict[x+y*1j]=char
                        if part2:
                            mapdict2[2*(x)+y*1j]=char if char =='#' else '['
                            mapdict2[2*(x)+y*1j+1]=char if char =='#' else ']'

                    elif char =='@':
                        pos=x+y*1j
                        if part2:
                            pos2=2*(x)+y*1j
                            print(pos2)

                else:
                    if char =='>':
                        directions.append(1)
                    elif char =='<':
                        directions.append(-1)
                    elif char =='^':
                        directions.append(-1j)
                    elif char =='v':
                        directions.append(1j)



        for step in directions:
            blocked=False
            free=False
            if mapdict[pos+step]=='O':
                n=2
                while not blocked and not free:
                    if mapdict[pos+step*n]=='#':
                        #print(n,'block')
                        blocked=True
                    elif mapdict[pos+step*n]=='':
                        #print(n,'free')
                        mapdict[pos+step*n]='O'
                        pos+=step
                        mapdict.pop(pos)
                        free=True
                    n+=1
            elif mapdict[pos+step]=='':
                pos+=step


        for coord in mapdict:
            if mapdict[coord]=='O':
                part1+=100*coord.imag+coord.real

        if part2:
            for step in directions:
                blocked=False

                if step.imag==0:

                    if mapdict2[pos2+step] =='[' or mapdict2[pos2+step] ==']':
                        n=2
                        while not blocked and not free:
                            if mapdict2[pos2+step*n]=='#':
                                #print(n,'block')
                                blocked=True
                            elif mapdict2[pos2+step*n]=='':
                                #print(pos2+step*n)
                                #print(n,'free')
                                for i in range(n,1,-1):
                                    mapdict2[pos2+step*i]=mapdict2.pop(pos2+step*(i-1))
                                pos2+=step
                                free=True
                            n+=1
                    elif mapdict2[pos2+step]=='':
                        pos2+=step
                else:

                    push=[]
                    obslist={}


                    if mapdict2[pos2+step]=='[':
                        push.append(pos2+step)
                        push.append(pos2+step+1)
                        obslist={0,1}
                        n=2
                    elif mapdict2[pos2+step]==']':
                        push.append(pos2+step-1)
                        push.append(pos2+step)
                        obslist={-1,0}
                        n=2

                    while not blocked and obslist:
                        # obslist=[] represents forwardmost row, which x values (rel to pos2) still have rocks
                        obsiter=list(obslist)
                        for relx in obsiter:

                            if mapdict2[pos2+relx+step*n]=='#': ## need to detect blocks for all obstacles
                            #print(n,'block')
                                blocked=True
                            elif mapdict2[pos2+relx+step*n]=='[':
                                push.append(pos2+relx+step*n)
                                push.append(pos2+relx+step*n+1)
                                obslist.add(relx+1)
                            elif mapdict2[pos2+relx+step*n]==']':
                                push.append(pos2+relx+step*n-1)
                                push.append(pos2+relx+step*n)
                                obslist.add(relx-1)
                            elif mapdict2[pos2+relx+step*n]=='':
                                obslist.remove(relx)
                        if not obslist:
                            push.sort(key=lambda x:x.imag, reverse=True if step.imag>0 else False)
                            #print(push)
                            for obscord in push:
                                #print(obscord+step, obscord,mapdict2[obscord])
                                if obscord in mapdict2:
                                    mapdict2[obscord+step]=mapdict2.pop(obscord)



                            pos2+=step
                            #print(mapdict2)
                        n+=1

                    if mapdict2[pos2+step]=='':
                        pos2+=step



            print(pos2)
            print(mapdict2)
            for coord in mapdict2:
                if mapdict2[coord]=='[':
                    part2ans+=100*coord.imag+coord.real

        return part1, part2ans


#print(readfile('input.txt'))
print(readfile('inputtest.txt',True))
print(time.time()-startTime)

#1370599 too low
'''
                        while not blocked and not free:
                            if step.real==0:
                                if mapdict2[pos+step]==']':
                                    l=-1
                                elif mapdict2[pos+step]=='[':
                                    r=2
                                pushdict=defaultdict(set)
                            if mapdict2[pos+step*n]=='#':
                                #print(n,'block')
                                blocked=True
                            elif mapdict2[pos+step*n]=='':
                                #print(n,'free')
                                for i in range():
                                mapdict[pos+step*n]='O'
                                pos+=step
                                mapdict.pop(pos)
                                free=True

                        n+=1


                    while not blocked and not free:
                        #print(pos,n,step)
                        #print(mapdict[pos+step*n])
                        pushdict=defaultdict(set)
                        if mapdict2[pos+step*n]=='#':
                            #print(n,'block')
                            blocked=True
                        elif mapdict2[pos+step*n]=='':
                            #print(n,'free')
                            mapdict[pos+step*n]='O'
                            pos+=step
                            mapdict.pop(pos)
                            free=True


                        #elif step ==-1j or step ==1j:
                        #
                        #    pushdict[mapdict2[pos+step*n]].add(pos+step*n)

                        n+=1

                        #print(mapdict)
                elif mapdict[pos+step]=='':
                    pos+=step

'''
