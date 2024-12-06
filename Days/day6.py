
def runDay(input):
    p2 = 0
    locations = []    
    obstacles=[]
    width=0
    length=len(input)    
    diyLooper = 0
    startingLoc = (0,0)
    for i in [item.replace('\n', '') for item in input]:
        if(width==0):
            width=len(i)
        for j in range(0,len(i)):
            if i[j] == "#":
                obstacles.append((j,diyLooper))
            if i[j] == "^":
                startingLoc = (j,diyLooper)
        diyLooper += 1
    
    print("Part 1")    
    run(startingLoc,obstacles,width, length)

    print("Part 2")           

    ctr = 0
    for l in locations:
        ctr+=1
        if(not l == startingLoc):
            newObstacles = obstacles[:]
            newObstacles.append(l)
            if(run(startingLoc,newObstacles,width,length, False)):
                p2+=1
    
    print(p2)

def run(startingLoc,obstacles, width, length,p1=True):
    locations = []
    locations.append(startingLoc)
    turnCounter=0
    inBounds=True
    startingDirection = "N"
    currentLoc = startingLoc
    while(inBounds):
        if(turnCounter>=5):
            return True
        if startingDirection == "N":
            nextLoc = (currentLoc[0],currentLoc[1]-1)
            if nextLoc in obstacles:
                startingDirection = "E"
                turnCounter+=1
            elif nextLoc[1]<0:
                inBounds=False
            else:
                currentLoc = nextLoc
                if(currentLoc not in locations):
                    locations.append(currentLoc)
                    turnCounter=0
        elif startingDirection == "E":
            nextLoc = (currentLoc[0]+1,currentLoc[1])
            if nextLoc in obstacles:
                startingDirection = "S"
                turnCounter+=1
            elif nextLoc[0]>=width:
                inBounds=False
            else:
                currentLoc = nextLoc
                if(currentLoc not in locations):
                    locations.append(currentLoc)
                    turnCounter=0
        elif startingDirection == "S":
            nextLoc = (currentLoc[0],currentLoc[1]+1)
            if nextLoc in obstacles:
                startingDirection = "W"
                turnCounter+=1
            elif nextLoc[1]>=length:
                inBounds=False
            else:
                currentLoc = nextLoc
                if(currentLoc not in locations):
                    locations.append(currentLoc)
                    turnCounter=0
        elif startingDirection == "W":
            nextLoc = (currentLoc[0]-1,currentLoc[1])
            if nextLoc in obstacles:
                startingDirection = "N"
                turnCounter+=1
            elif nextLoc[0]<=0:
                inBounds=False
            else:
                currentLoc = nextLoc
                if(currentLoc not in locations):
                    locations.append(currentLoc)
                    turnCounter=0
    
    if p1:
        print(len(locations))
    return False