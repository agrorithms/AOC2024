import sympy as sp
from sympy.solvers import solve

def readfile(filename,part2=False):
    '''
    read file and put button values and prize values into a dictionary of lists. could have just been list of lists
    if part 2 add 10000000000000 to each prize value
    '''
    with open(filename) as f:
        gamedict={}
        tokens=0
        for i,line in enumerate(f):
            if line=='\n':
                continue
            if i//4 not in gamedict:
                gamedict[i//4]=[[int(line[line.index('X')+2:line.index(',')]),int(line[line.index('Y')+2:line.index('\n')])]]
            elif line[:5]=='Prize' and part2:
                gamedict[i//4].append([10000000000000+int(line[line.index('X')+2:line.index(',')]),10000000000000+int(line[line.index('Y')+2:line.index('\n')])])
            else:
                gamedict[i//4].append([int(line[line.index('X')+2:line.index(',')]),int(line[line.index('Y')+2:line.index('\n')])])

        #for each game, solve system of equations. if solutions are integers and are less than 100, token count is added (3*x + 1*y)
        for game in gamedict:
            x, y = sp.symbols('x y')
            #print(gamedict[game][0][0])
            eq1=sp.Eq(gamedict[game][0][0]*x+gamedict[game][1][0]*y,gamedict[game][2][0])
            eq2=sp.Eq(gamedict[game][0][1]*x+gamedict[game][1][1]*y,gamedict[game][2][1])
            output = list(solve([eq1,eq2], (x, y)).values())
            #print(output[0])

            if part2 and int(output[0])==output[0] and int(output[1])==output[1]:
                tokens+=output[0]*3+output[1]
            elif output[0]<=100 and int(output[0])==output[0] and output[1]<=100 and int(output[1])==output[1]:
                tokens+=output[0]*3+output[1]
        return(tokens)

print(readfile('input13.txt'))
print(readfile('input13.txt',True))
