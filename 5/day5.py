def readfile(filename,part1=True):
    with open(filename) as f:
        pagemap={}
        reducepagemap={}
        pagetests=[]
        #loop thrugh file to create a map of page # to list of pages that come after it, or create a list of list of page orders
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

        # made a pagemap that attempted to only reference the page directly after it. this worked for p1 but not p2. idk
        for pagekey in pagemap:
            for num1 in pagemap[pagekey]:
                for num2 in pagemap[pagekey]:
                    if num1 in pagemap:
                        if num2 in pagemap[num1] and num2 in reducepagemap[pagekey]:
                            reducepagemap[pagekey].remove(num2)
        sum=0

        #loop through lists of page orders, while comparing to the page map,
        #if a pagekey's value appears but is not the next value in page order,
        #mark as a fail. if no fail add up sum of middle pages for part 1,
        #if fail, append to failpages list

        failpages=[]
        for page in pagetests:
            fail=False
            match=0
            pagecompare=page[0]
            while match<(len(page)-1) and not fail:

                pagecompare = reducepagemap[pagecompare][0]

                if pagecompare==page[match+1]:
                    match+=1
                elif pagecompare in page:
                    failpages.append(page)
                    fail=True
            if not fail:
                sum+=int(page[int((len(page)-1)/2)])
        if part1:
            return sum

        #loop through failpages (list of lists)
        #loop within an indivual page order list. starting with final index item, and moving toward the first,
        # check if any other pagenums in list belong to the right of current comparison pagenum.
        # if so move that item to the right of current comparison pagenum and start over
        # (look at final index item if anything belongs to its right, and loop toward first index item)
        # loop will finish after moving all the way from final to first index item with no change made
        # lastly we can sum the middle pagenum for each of these
        else:
            sumfail=0
            for page in failpages:

                i=0
                while i < (len(page)):
                    for num in page[:-i-1]:
                        if page[-i-1] in pagemap:
                            if num in pagemap[page[-i-1]]:
                                page.insert(len(page)-i,page.pop(page.index(num)))
                                i=-1
                    i+=1
                sumfail+=int(page[int((len(page)-1)/2)])
                #print(sum)
            return sumfail






print(readfile('input5.txt'))
print(readfile('input5.txt',False))
