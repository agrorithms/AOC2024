import time

startTime=time.time()

def readfile(filename,part2=False):
    with open(filename) as f:
        robots=[]
        fp=[]
        quadrantcount=[0,0,0,0]
        part1=1
        if filename=='inputtest.txt':
            maxx=10
            maxy=6
        else:
            maxx=100
            maxy=102
        for i,line in enumerate(f):
            p=line.split(' ')[0]
            v=line.split(' ')[1]
            robots.append([int(p[p.index('p=')+2:p.index(',')])+(int(p[p.index(',')+1:]))*1j,int(v[v.index('v=')+2:v.index(',')])+(int(v[v.index(',')+1:]))*1j])


        for pv in robots:
            fp.append(pv[0]+pv[1]*100)
            while fp[-1].imag<0 or fp[-1].imag>maxy:
                if fp[-1].imag<0:
                    fp[-1]+=(maxy+1)*1j
                elif fp[-1].imag>maxy:
                    fp[-1]-=(maxy+1)*1j
            while fp[-1].real<0 or fp[-1].real>maxx:
                if fp[-1].real<0:
                    fp[-1]+=(maxx+1)
                elif fp[-1].real>maxx:
                    fp[-1]-=(maxx+1)
            if fp[-1].real>maxx/2:
                if fp[-1].imag>maxy/2:
                    quadrantcount[3]+=1
                elif fp[-1].imag<maxy/2:
                    quadrantcount[0]+=1
            elif fp[-1].real<maxx/2:
                if fp[-1].imag>maxy/2:
                    quadrantcount[1]+=1
                elif fp[-1].imag<maxy/2:
                    quadrantcount[2]+=1

        #print(len(set(fp)))
        if not part2:
            for n in quadrantcount:
                #print (n, ans)
                part1*=n

            return part1
        else:
            fp=[]
            maxnearby=0

            for j in range(11000):

                nearby=0

                for i in range(len(robots)):
                    if j==0:
                        fp.append(robots[i][0])
                    else:
                        fp[i]+=robots[i][1]
                    if fp[i].imag<0:
                        fp[i]+=(maxy+1)*1j
                    elif fp[i].imag>maxy:
                        fp[i]-=(maxy+1)*1j

                    if fp[i].real<0:
                        fp[i]+=(maxx+1)
                    elif fp[i].real>maxx:
                        fp[i]-=(maxx+1)
                fpset=set(fp)
                for i in fpset:
                    if i+1 in fpset or i-1 in fpset or i+1j in fpset or i-1j in fpset:
                        nearby+=1
                if nearby>maxnearby:
                    maxnearby=nearby
                    print(j,nearby, len(fpset))
                    sec=j
                elif nearby>200:
                    print(j,nearby, len(fpset))
            return sec




print(readfile('input.txt'))
print(readfile('input.txt',True))
print(time.time()-startTime)
