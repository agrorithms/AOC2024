def readfile(filename,part2=False):
    with open(filename) as f:
        antennae={}
        antinode={}
        maxx=0
        maxy=0
        antinodeset=set()
        badantinodeset=set()
        '''
        loop through lines adding to dictionary of antenna frequency (key) to coordinate of antennae (values)

        '''
        for y, line in enumerate(f):
            maxy=y
            for x, char in enumerate(line[:-1]):
                maxx=x
                if char !='.':
                    if char in antennae:

                        antennae[char].append(complex(x,y))
                    else:
                        antennae[char]= [complex(x,y)]

        '''
        for every frequency in the dict, loops through each coordinate pair, if part 2, saving the 2 antennae coord as the 1st two antinodes,
        then looping through while antinodes remain within the bounds of the map. saving the antinode into an antinode dictionary,
        then adding or subtracting one more phase (coord-coord2) to each antinode. if part 2,  add/subtract one phase to each antenna coordinate, and save in dict
        at the end of each frequncy loop, update a set with any new antinodes
        '''
        for frequency in antennae:
            for i, coord in enumerate(antennae[frequency]):
                for coord2 in antennae[frequency][i+1:]:
                    if part2:
                        antinode1=coord
                        antinode2=coord2
                        while antinode1.imag<=maxy and antinode1.real<=maxx and antinode1.imag>=0 and antinode1.real>=0:
                            if frequency in antinode:
                                antinode[frequency].append(antinode1)
                            else:
                                antinode[frequency] = [antinode1]
                            antinode1+=(coord-coord2)
                        while antinode2.imag<=maxy and antinode2.real<=maxx and antinode2.imag>=0 and antinode2.real>=0:
                            if frequency in antinode:
                                antinode[frequency].append(antinode2)
                            else:
                                antinode[frequency] = [antinode2]
                            antinode2-=(coord-coord2)

                    else:
                        #print(coord,coord2)
                        antinode1=coord + (coord-coord2)
                        antinode2=coord2 - (coord-coord2)
                        if frequency in antinode:
                            antinode[frequency].append(antinode1)
                            antinode[frequency].append(antinode2)
                        else:
                            antinode[frequency] = [antinode1,antinode2]
            antinodeset.update(antinode[frequency])

        '''
        this part i think is only needed in part 1 but i left it in for either.
        check each item in antinode set to make sure it is within map bounds. if not, save to another set and then remove anything in the bad set
        lastly, return len(set) to get # of unique antinodes
        '''
        for item in antinodeset:
            if item.imag>maxy or item.real>maxx:
                badantinodeset.add(item)
            elif item.imag<0 or item.real<0:
                badantinodeset.add(item)
        differenceset=antinodeset.difference(badantinodeset)


        #print (antennae)
        #print (antinode)


        return len(differenceset)


print(readfile('input8.txt'))
print(readfile('input8.txt',True))
