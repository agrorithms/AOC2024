#day 1
def readFile(filename):
    right=[]
    left=[]
    rightstr=''
    leftstr=''
    switch=True
    #pipeDef={'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}
    with open(filename) as f:
        sum=0
        for line in f:
            for char in line:
                if char == ' ':
                    switch=False
                elif char == '\n':
                    switch=True
                elif switch:
                    rightstr+=char
                elif not switch:
                    leftstr+=char
            right.append(rightstr)
            left.append(leftstr)
            rightstr=''
            leftstr=''
        right.sort()
        left.sort()
        """for i in range(len(right)):
            sum+=(abs(int(right[i])-int(left[i])))
        return sum"""
        outer=0
        for i in range(len(right)):
            for j in range(len(left)):
                if right[i] ==left[j]:
                    sum+=1
            outer+=int(right[i])*sum
            sum=0
        return outer


print(readFile('input1.txt'))
