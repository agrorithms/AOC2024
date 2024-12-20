#day 1
def readFile(filename):
    right=[]
    left=[]
    rightstr=''
    leftstr=''
    switch=True
    with open(filename) as f:
        sum=0
        part1=0
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
        for i in range(len(right)):
            part1+=(abs(int(right[i])-int(left[i])))

        part2=0
        for i in range(len(right)):
            for j in range(len(left)):
                if right[i] ==left[j]:
                    sum+=1
            part2+=int(right[i])*sum
            sum=0
        return part1, part2


print(readFile('input1.txt'))
