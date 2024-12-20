"""def readfile(filename,part1=True):
    with open(filename) as f:
        sortorder={}
        min=0
        max=-1
        for line in f:
            if len(line)==6:
                a= line[:2]
                b= line[3:5]
                if line[:2] not in sortorder and line[3:5] not in sortorder:
                    sortorder[a]=min
                    min+=1
                    sortorder[b]=min
                    min+=1
                elif a in sortorder:
                    if b not in sortorder:
                        sortorder[b]=min
                        min+=1
                    else:
                        if sortorder[a]>sortorder[b]:
                            for tup in sortorder.items():
                                if tup[1]>sortorder[a] and tup[1]<sortorder[b]:



                else:
                    sortorder[a]=max
                    max-=1



        return sortorder



            #for char in line:"""

def readfile(filename,part1=True):
    with open(filename) as f:
        pagemap={}
        reducepagemap={}
        pagetests=[]
        for line in f:
            if len(line)==6:
                a= line[:2]
                b= line[3:5]
                if a not in pagemap:
                    pagemap[a]=[b]
                    reducepagemap[a]=[b]
                else:
                    pagemap[a].append(b)
                    reducepagemap[a].append(b)
            elif len(line)>6:
                pagetests.append(line[:-1].split(','))


        for pagekey in pagemap:
            for num1 in pagemap[pagekey]:
                for num2 in pagemap[pagekey]:
                    if num1 in pagemap:
                        if num2 in pagemap[num1] and num2 in reducepagemap[pagekey]:
                            reducepagemap[pagekey].remove(num2)
        sum=0
        #print(pagemap)
        print(reducepagemap)
        print(pagetests[0])
        for page in pagetests:
            fail=False
            match=0
            pagecompare=page[0]
            print('page')
            print(page)
            while match<(len(page)-1) and not fail:
                #print(match)
                #print(len(page)-1)
                pagecompare = reducepagemap[pagecompare][0]

                if pagecompare==page[match+1]:
                    match+=1
                elif pagecompare in page:

                    fail=True
            if not fail:
                sum+=int(page[int((len(page)-1)/2)])
                print('sum')
                print(sum)
        return sum






print(readfile('input5.txt'))
#print(readfile('input5.txt',False))
