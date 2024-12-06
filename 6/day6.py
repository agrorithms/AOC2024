def readfile(filename,part2=False):
    with open(filename) as f:
        guardmap={}
        #build map of coordinate to character in coordinate spot
        #using complex numbers for easy addition of coordinate
        for y, line in enumerate(f):

            for x, char in enumerate(line[:-1]):
                guardmap[complex(x,y)]=char
                if char =='^':
                    start= complex(x,y)

        #call createpatrolpath
        patrolpath = createpatrolpath(guardmap,start,part2)
        #if part 1 , return length of patrol path (num of spaces patrolled)
        if not part2:
            return len(patrolpath)
        # if part 2 loop through the whole map of coordinate to character,
        # insert an obstacle in each coordinate that is not already one or the starting location
        # rung the createpatrolpath, if this returns false, patrol is in a loop. add 1 to part2sum
        # reset the obstacle that was inserted and continue looping
        #return part2sum which is number of locations we can put an obstacle to make patrol a loop
        # this will take long (~1 minute?)
        else:
            part2sum=0
            for coord in guardmap.keys():
                if guardmap[coord]!='#' and guardmap[coord]!='^':
                    guardmap[coord]='#'
                    #print(coord)
                    if createpatrolpath(guardmap,start,part2)==False:
                        part2sum+=1
                        #print(part2sum)
                    guardmap[coord]='.'
            return part2sum





# while current position (start variable) is in the guardmap add each current position to a dictionary key. value will be number of times the coord is touched
# if the next space based on current direction is an obstactle, turn right and add this turn coordinate to a list
# if part 2, check if this turn coordinate is already in the existing list of turn coordinates
# if so, return False to indicate the path is in a loop
# if not part 2 or no loop is found, continue looping through current coord+direction, adding to the patrolpath dict for each space
# until we end up outside of the map, at which point return the patrolpath dict
def createpatrolpath(guardmap,start,part2=False,direction=-1j):
    patrolpath={}
    turncoords=[]

    while start in guardmap:

        if start not in patrolpath:
            patrolpath[start]=1
        else:
            patrolpath[start]+=1
        if start+direction in guardmap:
            while guardmap[start+direction]=='#':
                turncoords.append([start,start+direction])
                #print(turncoords[-4:])
                #print(turncoords[-8:-4])
                if turncoords[-1] in turncoords[:-1] and part2:
                    return False

                direction=direction*1j
                #print(turncoords)
        start=start+direction
    return patrolpath


print(readfile('input6t.txt'))
print(readfile('input6.txt',part2=True))
