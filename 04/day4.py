def readfile(filename,part1=True):
    with open(filename) as f:
        path={}
        sum=0
        for i, line in enumerate(f):

            for j, char in enumerate(line):
                if char == '\n':
                    continue
                if part1:

                    a=(i,j)
                    x=(i,j-1)
                    y=(i-1,j)
                    z=(i-1,j-1)
                    w=(i-1,j+1)
                    if char == 'X' or char == 'S':
                        path[(i,j)]=[char,char,char,char,char]

                    if x in path:
                        if a not in path:
                            path[a]=[char,char,char,char,char]
                        path[a][0]=char
                        path[(a)][1]=path[x][1][max(len(path[x][1])-3,0):]+char
                    if y in path:
                        if a not in path:
                            path[a]=[char,char,char,char,char]
                        path[a][0]=char
                        path[(a)][2]=path[y][2][max(len(path[y][2])-3,0):]+char
                    if z in path:
                        if a not in path:
                            path[a]=[char,char,char,char,char]
                        path[a][0]=char
                        path[(a)][3]=path[z][3][max(len(path[z][3])-3,0):]+char
                    if w in path:
                        if a not in path:
                            path[a]=[char,char,char,char,char]
                        path[a][0]=char
                        path[(a)][4]=path[w][4][max(len(path[w][4])-3,0):]+char
                    if a in path:
                        for string in path[a]:
                            if string =='XMAS' or string == 'SAMX':
                                sum+=1
                else:
                    a=(i,j)
                    b=(i-1,j-1)
                    c=(i-1,j+1)
                    if char == 'M' or char == 'S':
                        path[(i,j)]=[char,char,char,(),()]
                    if b in path:
                        if a not in path:
                            path[a]=[char,char,char,(),()]
                        path[a][0]=char
                        path[(a)][1]=path[b][1][max(len(path[b][1])-2,0):]+char
                        if path[b][0]=='A':
                            path[a][3]=b
                    if c in path:
                        if a not in path:
                            path[a]=[char,char,char,(),()]
                        path[a][0]=char
                        path[(a)][2]=path[c][2][max(len(path[c][2])-2,0):]+char
                        if path[c][0]=='A':
                            path[a][4]=c
                    if a in path:
                        for string in path[a][1:2]:
                            if string =='MAS' or string == 'SAM':
                                if j>=2:
                                    if path[(i,j-2)][2]=='MAS' or path[(i,j-2)][2]=='SAM':
                                        if path[(i,j-2)][4]==path[a][3]:
                                            sum+=1

        #print(path)
        return sum




print(readfile('input4.txt'))
print(readfile('input4.txt',False))
