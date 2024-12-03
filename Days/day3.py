import re

def runDay(input):
    p1 = 0
    p2 = 0
    combinedStr = ""
    for i in input:
        combinedStr+=i
    print("Part 1")
    pairs = re.findall("mul\((\d+),(\d+)+\)",combinedStr)
    for p in pairs:
        p1+=(int(p[0])*int(p[1]))
    
    print(p1)
    print("Part 2")        
    do=[]
    dont=[]
    for m in re.finditer("don't\(\)",combinedStr):
        if(len(do) == 0):
            do.append((0,4))
        dont.append(m.span())
    for m in re.finditer("do\(\)",combinedStr):
        do.append(m.span())
    
    doranges = []
    for i in range(0,len(do)):
        dontIter=0
        while(do[i][0]>dont[dontIter][0]):
            dontIter+=1
            if(dontIter>len(dont)-1):
                dontIter=-1
                break
        if dontIter==-1:
            doranges.append((do[i][0],len(combinedStr)))
        else:
            doranges.append((do[i][0],dont[dontIter][0]))

    finditeriter = 0
    for m in re.finditer("mul\((\d+),(\d+)+\)",combinedStr):      
        loc =m.span()[0]
        if any(lower <= loc <= upper for (lower, upper) in doranges):            
            p2+=(int(pairs[finditeriter][0])*int(pairs[finditeriter][1]))
        finditeriter+=1

    print(p2)
 