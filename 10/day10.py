def readfile(filename,part2=False):
    '''
    read file to create a dictionary mapping coordinate to topographic value, a list of trailheads.
    for each ele in trailheads, run hike function and augment scores by unique hike ends for part1, and by total hike ends for part 2
    return scores
    '''
    with open(filename) as f:
        mapdict={}
        trailheads=[]
        scores=0
        for y,line in enumerate(f):

            for x,char in enumerate(line[:-1]):
                mapdict[x+y*1j]=int(char)
                if char=='0':
                    trailheads.append(x+y*1j)

        for i in trailheads:
            if part2:
                scores+=len(hike(i,mapdict,[]))
            else:
                scores+=len(set(hike(i,mapdict,[])))
        return scores

def hike(currentspot,trailmap,finaldestination=[]):
    '''
    given a current spot, check 4 nearby spots (up,down,right,left) to see if it has topographic value (tv) of 1 higher than current spot's.
    if so, check if tv is 9 - if yes, append coord to finaldestination list.
    if not, run hike from current spot, and pass into it the current finald list. return finald list
    '''
    for i in range(-1,2,2):
        if currentspot+i in trailmap:
            if trailmap[currentspot+i]==trailmap[currentspot]+1:
                if trailmap[currentspot+i]==9:
                    finaldestination.append(currentspot+i)
                else:
                    hike(currentspot+i,trailmap,finaldestination)

    for i in range(-1,2,2):
        if currentspot+i*1j in trailmap:
            if trailmap[currentspot+i*1j]==trailmap[currentspot]+1:
                if trailmap[currentspot+i*1j]==9:
                    finaldestination.append(currentspot+i*1j)
                else:
                    (hike(currentspot+i*1j,trailmap,finaldestination))

    return finaldestination

print(readfile('input10.txt'))
print(readfile('input10.txt',True))
