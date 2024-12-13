def readfile(filename,part2=False):
    '''
    loop through input building a dict of coord to char
    build second dict of char to list of set(s) of coords - each set representing a region
    '''
    with open(filename) as f:
        mapdict={}
        flowerdict={}
        price=0
        for y,line in enumerate(f):

            for x,char in enumerate(line[:-1]):
                mapdict[x+y*1j]=char
                if char not in flowerdict:
                    flowerdict[char]=[{x+y*1j}]

                else:
                    added=False                                                                  # set added to false
                    for i in range(len(flowerdict[char])):                                       #loop through all existing sets for char

                        if i>=len(flowerdict[char]):                                             #in case element was removed and iterator is too high
                            continue

                        # if set contains an adjecent cell to current char, add char to set. mark that we have added this to a set

                        if x+y*1j-1j in flowerdict[char][i] or x+y*1j-1 in flowerdict[char][i]:
                            flowerdict[char][i].add(x+y*1j)
                            added=True
                            for j,region in enumerate(flowerdict[char][:i]):                   #if coord is added to a set, check if coord exists
                                if x+y*1j in region:                                           #in other sets. if so, combine them (only leave 1)

                                    flowerdict[char][i].update(flowerdict[char].pop(j))

                    if not added:                                                             #if coord is never added to an existing set,
                        flowerdict[char].append({x+y*1j})                                     #append a new one (set(cord)) to list

                maxcoord=x+y*1j                         #save maxcord to later check if coords are in the map

        '''
        loop through flower:region dictionary . loop through each region
        area for each region is length of set
        '''

        for flower in flowerdict.keys():
            for i in range(len(flowerdict[flower])):
                area=len(flowerdict[flower][i])

                '''
                if part 2, create two dicts an x direction edge checker and one for y direction. initiate totsides to 0.
                loop through each coordinate in the region
                '''

                if part2:
                    xsides={}
                    ysides={}
                    totsides=0
                    for coord in flowerdict[flower][i]:
                        if (coord+1j).imag<=maxcoord.imag:                              # if next coord in y direction is in map
                            if mapdict[coord+1j]!=flower:                               #and if that next coord is a different flower
                                if coord.real+1j not in ysides:                         #add the y value of the "edge" (coord.imag+1) to a set
                                    ysides[coord.real +1j]={coord.imag+1}               #this will be the value
                                else:                                                   #key is the x value (coord.real) and y direction (+1j)
                                    ysides[coord.real+1j].add(coord.imag+1)             #if set already exists, add to it instead of initiating new
                        else:
                            if coord.real+1j not in ysides:                             # if next coord is y direction not in map,it must be an edge
                                ysides[coord.real +1j]={coord.imag+1}                   #so we do the same as aboe
                            else:
                                ysides[coord.real+1j].add(coord.imag+1)

                        if (coord-1j).imag>=0:                                          #next repeat the same thing 3 times once more in y direction
                            if mapdict[coord-1j]!=flower:                               #but looking backwards (up or -1j) then same 2 ideas for x
                                if coord.real-1j not in ysides:
                                    ysides[coord.real -1j]={coord.imag-1}
                                else:
                                    ysides[coord.real-1j].add(coord.imag-1)
                        else:
                            if coord.real-1j not in ysides:
                                ysides[coord.real -1j]={coord.imag-1}
                            else:
                                ysides[coord.real-1j].add(coord.imag-1)

                        if (coord+1).real<=maxcoord.real:                               #do x direction looking forward (+1)
                            if mapdict[coord+1]!=flower:                                #dictionary key is now
                                if coord.imag+1j not in xsides:                         #y coord (coord.imag) + x direction (+1j)
                                    xsides[coord.imag+1j]={coord.real+1}
                                else:
                                    xsides[coord.imag+1j].add(coord.real+1)
                        else:
                            if coord.imag+1j not in xsides:
                                xsides[coord.imag +1j]={coord.real+1}
                            else:
                                xsides[coord.imag+1j].add(coord.real+1)

                        if (coord-1).real>=0:                                           #finally do x direction looking backward (-1, left)
                            if mapdict[coord-1]!=flower:
                                if coord.imag-1j not in xsides:
                                    xsides[coord.imag-1j]={coord.real-1}
                                else:
                                    xsides[coord.imag-1j].add(coord.real-1)
                        else:
                            if coord.imag-1j not in xsides:
                                xsides[coord.imag-1j]={coord.real-1}
                            else:
                                xsides[coord.imag-1j].add(coord.real-1)

                    '''
                    loop through these side dicts, if the previous x or y value has the same edge then it is the same side and we do not add
                    for any edges that differ in x or y from the previous edge location (edge-1) then count them
                    if edge-1 doesnt exist, all sides are added
                    sum totsides*area
                    '''

                    for edge in ysides.keys():
                        if edge-1 not in ysides:
                            totsides+=len(ysides[edge])
                        else:
                            if ysides[edge] != ysides[edge-1]:
                                for num in ysides[edge]:
                                    if num not in ysides[edge-1]:
                                        totsides+=1

                    for edge in xsides.keys():
                        if edge-1 not in xsides:
                            totsides+=len(xsides[edge])
                        else:
                            if xsides[edge] != xsides[edge-1]:
                                for num in xsides[edge]:
                                    if num not in xsides[edge-1]:
                                        totsides+=1
                    price+=totsides*area


                else:

                    '''
                    part 1. area is same. to find perimeter, loop through all cords in a region, if any coord has an adjacent coordinate that
                    is not the same flower or adj. coord is off them map, then perimeter +=1
                    sum perimeter*area
                    '''
                    perimeter=0

                    for coord in flowerdict[flower][i]:

                        if (coord+1j).imag<=maxcoord.imag:
                            if mapdict[coord+1j]!=flower:
                                perimeter+=1
                        else:
                            perimeter+=1
                        if (coord-1j).imag>=0:
                            if mapdict[coord-1j]!=flower:
                                perimeter+=1
                        else:
                            perimeter+=1
                        if (coord+1).real<=maxcoord.real:
                            if mapdict[coord+1]!=flower:
                                perimeter+=1
                        else:
                            perimeter+=1
                        if (coord-1).real>=0:
                            if mapdict[coord-1]!=flower:
                                perimeter+=1
                        else:
                            perimeter+=1
                    price+=perimeter*area

        return price

print(readfile('input12.txt'))
print(readfile('input12.txt',True))
