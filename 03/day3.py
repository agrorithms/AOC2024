import re

def readfile(filename, part1=True):
    sum=0
    switch=True
    with open(filename) as f:
        for line in f:
            line = re.sub("do\(\)", "mul(0000,0000)", re.sub("don't\(\)", "mul(00000,00000)",line))
            for item in re.findall('mul\(\d+,\d+\)',line):
                if item == 'mul(0000,0000)':
                    switch=True
                elif item == 'mul(00000,00000)':
                    switch = False
                elif switch or part1:
                    sum+=int(item[4:item.index(',')])*int(item[item.index(',')+1:item.index(')')])
        return sum





print(readfile('input3.txt'))
print(readfile('input3.txt',False))
