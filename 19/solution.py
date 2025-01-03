import time

startTime=time.time()

def readfile(filename,part2=False):
    with open(filename) as f:
        inputswitch=False
        designs=[]
        for line in f:
            if line =='\n':
                inputswitch=True
                continue
            if inputswitch:
                designs.append(line[:-1])
            else:
                patterns=line[:-1].split(', ')
        print (patterns,designs)
        part1=0

    def isValidDesign(availablepattern,designstr):

        if not designstr:
            return True
        for pattern in availablepattern:
            if designstr[:len(pattern)]==pattern:


                if isValidDesign(availablepattern,designstr[len(pattern):]):
                    return True


    for design in designs:
        if isValidDesign(patterns,design):
            #print(design)
            part1+=1
    return part1


print(readfile('input.txt'))
print(time.time()-startTime)
