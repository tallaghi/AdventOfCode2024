
def runDay(input):
    p1 = 0
    p2 = 0    
    
    print("Part 1")    
    input = [[int(c) for c in item.replace('\n', '')] for item in input]    
    xLen=len(input[0])
    yLen=len(input)
    for i in range(0,yLen):
        for j in range(0,xLen):
            if input[i][j] == 0:
                hitPeaks=[]
                ctr=findPeak(i,j,1,input,xLen,yLen,hitPeaks,True)
                p1+=ctr
                ctr=findPeak(i,j,1,input,xLen,yLen,hitPeaks,False)
                p2+=ctr
                    
    print(p1)
    print("Part 2")    
    print(p2)


def findPeak(i, j, lf, input,xLen,yLen,hitPeaks,p1):    
    currentCoord=(j,i)
    ctr=0
    if lf==10:
        print(currentCoord)
        if p1:
            if currentCoord not in hitPeaks:            
                hitPeaks.append(currentCoord)
                return ctr+1
            else:
                return ctr
        else:
            return ctr+1
    #up
    if(i-1>=0 and input[i-1][j]==lf):
        currentCoord=(j,i-1)
        ctr+=findPeak(i-1,j,lf+1,input,xLen,yLen,hitPeaks,p1)
    #right
    if(j+1<xLen and input[i][j+1]==lf):
        currentCoord=(j+1,i)
        ctr+=findPeak(i,j+1,lf+1,input,xLen,yLen,hitPeaks,p1)
    #down
    if(i+1<yLen and input[i+1][j]==lf):
        currentCoord=(j,i+1)
        ctr+=findPeak(i+1,j,lf+1,input,xLen,yLen,hitPeaks,p1)
    #left
    if(j-1>=0 and input[i][j-1]==lf):
        currentCoord=(j-1,i)
        ctr+=findPeak(i,j-1,lf+1,input,xLen,yLen,hitPeaks,p1)
    
    return ctr