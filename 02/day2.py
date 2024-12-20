def readfile(filename, part1=True):
    if part1:
        maxfail=0
    else:
        maxfail=1
    with open(filename) as f:
        safelines=0
        for line in f:
            num=''
            numlst=[]
            fail=0
            delta=''
            for char in line:
                if fail>maxfail:
                    break
                if char == ' ' or char =='\n':
                    if numlst:

                        if abs(numlst[-1]-int(num))>3 or (numlst[-1]-int(num))==0:
                            fail+=1
                        if isinstance(delta,int):
                            if(delta>0 and (numlst[-1]-int(num))<0) or (delta <0 and numlst[-1]-int(num)>0):
                                fail+=1
                        delta=numlst[-1]-int(num)

                    numlst.append(int(num))
                    num=''
                else:
                    num+=char
            if fail<=maxfail:
                safelines+=1

    return safelines




print(readfile('input2.txt'))
print(readfile('input2.txt',False))
