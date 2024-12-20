def readfile(filename,part2=False):
    with open(filename) as f:
        filespace=[]
        checksum=0
        filespacedict={}
        freespacedict={}

        # loop through one-line file, if part 2, create two dictionaries, one for file sizes (even indexes) and one for free spaces (odd indexes)
        # file size dict will map file index to file size (int(char)) and to its location on disk (len(filespace))
        # also create a list to represent the disk space: for each file, append the index to the list j times according to file size, do the same for free space

        for line in f:
            for i,char in enumerate(line[:-1]):

                if part2:
                    if i%2==0:
                        filespacedict[int(i/2)]=(int(char),len(filespace))
                    else:
                        freespacedict[len(filespace)]=int(char)
                    maxfileindex=int(i/2)
                    #maxfreeindex=len(filespace)


                for j in range(int(char)):
                    if i%2==0:
                        filespace.append(int(i/2))
                    else:
                        filespace.append('.')



        #print(currentspot)

        #print(len(filespace))
        #print(filespace.index(372))

        # for part two, record the highest file index and loop backwrds to 0. for each file index, the space needed is the current indexed file's size
        #start a for loop from 0 to the disk location of the current file index. check if loop iterator exists in freespacedict (is that index an open disk space)
        # if so, check if this location has enough space. if so decrease the open space by spaceneeded,
        # and increase the index of this free space by spaceneeded, or if all this free space is taken up, just remove this free space from the dict
        #
        # next for each spaceneeded, replace the free space in the filespace list (disk location representation) with the index of the current file index
        # break out of looping up to the current file index ( if we found a free space for this file. not neeed to keep looking)
        # decrease currentfile index by and repeat via while loop
        #

        if part2:
            currentfileindex=maxfileindex
            while 0<currentfileindex:
                spaceneeded=filespacedict[currentfileindex][0]


                for j in range(filespacedict[currentfileindex][1]):
                    if j in freespacedict:
                        #print(j, spaceneeded)
                        if freespacedict[j]>=spaceneeded:
                            #print('1,',freespacedict)
                            freespacedict[j]-=spaceneeded
                            if freespacedict[j]==0:
                                freespacedict.pop(j)
                             #print('2,',freespacedict)
                            else:
                                freespacedict[j+spaceneeded]=freespacedict.pop(j)
                            #print('3,',freespacedict)

                            for i in range(spaceneeded):
                                filespace[j+i]=currentfileindex
                                filespace[filespacedict[currentfileindex][1]+i]='.'
                            #currentfileindex-=1
                            #print(len(filespace),filespace)
                            break

                currentfileindex-=1

            #for part 2 loop through filespace (disk representation) and perform checksum. return checksum
            for k in range(len(filespace)):
                if str(filespace[k])!=filespace[k]:
                    checksum+=k*filespace[k]

            #print(filespace)
            #print(len(filespace))
            #print(filespace.index(372))
            #print(filespacedict, freespacedict)
            return checksum


        #part1 first remove any trailing freespace.
        #loop through len of filespace, if encounter a free space, pop from end of filespace into the free space, and add to checksum, increase iterator
        #remove any trailing freespace and repeat. return checksum
        else:
            while filespace[-1]=='.':
                    filespace.pop()
            k=0
            while k <len(filespace):

                if filespace[k] =='.' and k!=len(filespace):
                    filespace[k]=filespace.pop()
                checksum+=k*filespace[k]
                k+=1
                while filespace[-1]=='.':
                    filespace.pop()
            return checksum



print(readfile('input9.txt'))
print(readfile('input9.txt',True))
