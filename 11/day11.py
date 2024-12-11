def readfile(filename):
    '''
    read file, split by spaces, return length of stoneblink array'''


    with open(filename) as f:

        for line in f:
            stones=line[:-1].split(' ')

        return len(stoneblink(stones,25))



def stoneblink(stones,blinks):
    '''
    for each blink go through the list and change 0 to 1 , replace any even-digited num with its first n/2 digits after appending its last n/2 digits
    else multiple the element by 2024. return the subsequent list
    '''
    for blink in range(blinks):

        numstones=len(stones)
        for i in range(numstones):


            if int(stones[i]) ==0:
                stones[i]='1'
            elif len(stones[i])%2==0:
                stones.append(str(int(stones[i][len(stones[i])//2:])))
                stones[i]=str(int(stones[i][:len(stones[i])//2]))



            else:
                stones[i]=str(int(stones[i])*2024)

    return stones


print(readfile('input11t.txt'))
