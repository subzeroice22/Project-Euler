f = open('largestProductInAGrid_INPUT.txt', 'r')

grid = []
lines = f.readlines()[0:]

for line in lines:
    numLine = [int(x) for x in line.split(' ')]
    grid.append(numLine)
f.close()

def checkHorizontal(gridArg):
    numbers = []
    product = 0
    for line in grid:
        #print(line)
        for x in range(len(line)):
            #print(x)
            try:
                smallChunk = line[x:x+4]

                if(
                
            except:
                break;

#print(grid)

checkHorizontal(grid)
