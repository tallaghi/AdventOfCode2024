
def runDay(input):
    p1 = 0
    p2 = 0    
    input=input[0]
    print("Part 1")    
    inputArr=[]
    
    length=len(input)
    for i in range(0,length):        
        for j in range(0,int(input[i])):
            if (i+1)%2==0:
                inputArr.append(".")
            else:
                inputArr.append(str(int(i/2)))
    length=len(inputArr)
    lastLastIx=-1
    initialArr=inputArr[:]
    for i in range(0,length):
        if inputArr[i]==".":
            lastIX=0
            ctr=lastLastIx
            while lastIX==0:
                if inputArr[ctr] != ".":
                    lastIX=(length+ctr)
                    lastLastIx=ctr
                else:
                    ctr-=1
            if i<=lastIX:
                inputArr[i],inputArr[ctr]=inputArr[ctr],inputArr[i]
            else:
                break
            #newStr[i],newStr[ctr] = newStr[ctr],newStr[i]
        if i%5000==0:
            print(i/length)

    for i in range(0,length):
        if inputArr[i]!=".":
            p1+=int(inputArr[i])*i

    lastFailed = ""
    for i in range(length-1,-1,-1):
        if initialArr[i]!="." and initialArr[i] != lastFailed:
            size=1
            didSwap=False
            for j in range(i-1,-1,-1):
                if initialArr[i] == initialArr[j]:
                    size+=1
                else:
                    break
            for j in range(0,i):                
                if initialArr[j]==".":
                    jsize=1
                    for k in range(j+1,length):
                        if initialArr[k]==".":
                            jsize+=1                                                
                        else: break
                        if jsize>=size: break
                    if jsize>=size:
                        didSwap=True
                        initialArr[i+1-size:i+1],initialArr[j:j+size]=initialArr[j:j+size],initialArr[i+1-size:i+1]
                        break
            if not didSwap:
                lastFailed=initialArr[i] 
        if (length-i)%5000==0:
            print((length-i)/length)

    for i in range(0,length):
        if initialArr[i]!=".":
            p2+=int(initialArr[i])*i

    print(p1)
    print("Part 2")    
    print(p2)