def readfile(filename,part2=False):
    """ loops through lines in input file, assigning the test value to test, and the remaning numbers into a list, nums
        calls testnums and if true will add testvalue to the addnums total. return addnums total after all lines are looped
    """
    with open(filename) as f:
        addnums=0
        for line in f:

            test=int(line[:line.index(':')])
            nums = [int(x) for x in line[line.index(':')+2:-1].split(' ')]
            if testnums(test,nums,part2):
                #print('testnums True')
                addnums+= test


        return addnums

def testnums(testint,numlst,part2=False):
    '''
    if numlst is only 1 int long, check if that int == testint. if so, true, if not , false.
    if numlst is more than 1 int long, remove the first two ints, assign them to variables num1,num2. create two new lists of 1 value
    first has value num1* num2, second has value of num1+num2. If part 2, third list is num1||num2 (string addition then back to int)
    extend these 2 or 3 new lists to include any remainig values from original numlst.
    return testnums of each of these list, returning true if any of them return true.
    '''
    if len(numlst)==1 and numlst[0]==testint:
        return True
    elif len(numlst)==1 and numlst[0]!=testint:
        return False
    elif len(numlst)>1:
        #print(numlst)
        num1=numlst.pop(0)
        num2=numlst.pop(0)
        #print(num1,num2)
        numlst1=[num1*num2]
        numlst2=[num1+num2]
        if part2:
            numlst3=[int(str(num1)+str(num2))]

        if len(numlst)>0:
            numlst1.extend(numlst)
            numlst2.extend(numlst)
            if part2:
                numlst3.extend(numlst)
        #print(numlst1,numlst2,numlst3)
        if part2:
            return testnums(testint,numlst1,part2) or testnums(testint,numlst2,part2) or testnums(testint,numlst3,part2)
        else:
            return testnums(testint,numlst1,part2) or testnums(testint,numlst2,part2)
















#print(readfile('input7.txt'))
print(readfile('input7.txt',True))
