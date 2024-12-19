import time

startTime=time.time()

def readfile(filename,part2=False):
    with open(filename) as f:
        inputswitch=False
        register={}
        output=''
        i=0
        for line in f:
            if line =='\n':
                inputswitch=True
                continue
            if inputswitch:
                program=[int(x) for x in line[line.index(':')+2:-1].split(',')]
            else:
                register[line[line.index(' ')+1:line.index(':')]]=int(line[line.index(':')+2:-1])
        print(','.join(str(x) for x in program), register)
        #combo={0:0,1:1,2:2,3:3,4:register['A'],5:register['B'],6:register['C']}
        if not part2:
            while i < len(program):
                combo={0:0,1:1,2:2,3:3,4:register['A'],5:register['B'],6:register['C']}
                opcode=program[i]
                operand=program[i+1]
                if opcode==3:
                    if register['A']!=0:
                        i=operand
                        continue
                elif opcode==0:
                    register['A']//=(2**combo[operand])
                elif opcode==1:
                    register['B']=register['B']^(operand)
                elif opcode==2:
                    register['B']=combo[operand]%8
                elif opcode==4:
                    register['B']=register['B']^register['C']
                elif opcode==5:
                    output+=str(combo[operand]%8)+','
                elif opcode ==6:
                    register['B']=register['A']//(2**combo[operand])
                elif opcode ==7:
                    register['C']=register['A']//(2**combo[operand])

                i+=2
            return(output[:-1])



print(readfile('input.txt'))
#print(readfile('input.txt',True))
print(time.time()-startTime)
