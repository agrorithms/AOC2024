import time
startTime=time.time()
def logic(line,gates,skipped):
    '''
    saves an operator and assigns a value to a wire (key) for any wires where both input values already exist in dict.
    saves a list of lines that could not be assigned due to input not existing yet
    '''
    space1=line.index(' ')
    space2=line.index(' ',line.index(' ')+1)
    operator=line[space1+1:space2]
    if line[space2+1:line.index('-')-1] not in gates or line[:space1] not in gates:
        skipped.append(line)
    else:
        if operator=='AND':
            gates[line[line.index('>')+2:-1]]=int(gates[line[:space1]] and gates[line[space2+1:line.index('-')-1]])
        elif operator =='OR':
            gates[line[line.index('>')+2:-1]]=int(gates[line[:space1]] or gates[line[space2+1:line.index('-')-1]])
        elif operator=='XOR':
            gates[line[line.index('>')+2:-1]]=int(gates[line[:space1]] != gates[line[space2+1:line.index('-')-1]])
    return gates,skipped


def readfile(filename,part2=False):
    '''
    reads file to initiate dictionary with given wire values, calls logic to assign wire values to wires dependent on inputs
    repeatedly calls logic while looping through lines that could not assign in a first iteration due to missing inputs
    returns decimal of binary output of z wires
    '''
    with open(filename) as f:
        inputswitch=True
        gatedict={}
        uninitiated=[]
        for line in f:
            if line =='\n':
                inputswitch=False
                continue
            if inputswitch:
                gatedict[line[:line.index(':')]]=int(line[line.index(':')+1:-1])
            else:
                gatedict,uninitiated=logic(line,gatedict,uninitiated)

        i=0
        while uninitiated:
            unused=[]
            gatedict,unused=logic(uninitiated.pop(i%len(uninitiated)),gatedict,unused)

            if unused not in uninitiated:
                uninitiated.extend(unused)
                i+=1
            i+=1

        output = list([(x,y) for x,y in gatedict.items() if x[0]=='z'])
        output.sort(key=lambda x : x[0],reverse=True)
        binstr=''.join([str(x[1]) for x in output])
        return (int(binstr,2))


print(readfile('input.txt'))
#print(readfile('input11t.txt',True))
print(time.time()-startTime)
