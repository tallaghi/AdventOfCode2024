
def runDay(input):
    p1 = 0
    p2 = 0
    xLen=0
    yLen=len(input)
    antip1=[]
    antip2=[]
    print("Part 1")    
    iiter=0
    input = [item.replace('\n', '') for item in input]
    for i in input:
        if xLen==0:
            xLen=len(i)
        for j in range(0,xLen):
            if i[j]!=".":
                for k in range(iiter+1,yLen):
                    if  i[j] in input[k]:
                        ixs=[q for q, x in enumerate(input[k]) if x == i[j]]
                        for ix in ixs:
                            #Part1
                            xdiff = j-ix
                            ydiff = k-iiter                            
                            if(ix-xdiff < xLen and ix-xdiff >= 0 and k+ydiff < yLen and k+ydiff >= 0 and (ix-xdiff,k+ydiff) not in antip1):
                                antip1.append((ix-xdiff,k+ydiff))
                            if(j+xdiff < xLen and j+xdiff >= 0 and iiter-ydiff < yLen and iiter-ydiff >= 0 and (j+xdiff,iiter-ydiff) not in antip1):
                                antip1.append((j+xdiff,iiter-ydiff))
                            #Part2
                            bothOB=False
                            iteration=1
                            t_xdiff=0
                            t_ydiff=0
                            if((j,iiter) not in antip2):
                                antip2.append((j,iiter))
                            if((ix,k) not in antip2):
                                antip2.append((ix,k))
                            while(not bothOB):
                                t_xdiff=xdiff*iteration
                                t_ydiff=ydiff*iteration
                                if(ix-t_xdiff < xLen and ix-t_xdiff >= 0 and k+t_ydiff < yLen and k+t_ydiff >= 0 and (ix-t_xdiff,k+t_ydiff) not in antip2):
                                    antip2.append((ix-t_xdiff,k+t_ydiff))
                                if(j+t_xdiff < xLen and j+t_xdiff >= 0 and iiter-t_ydiff < yLen and iiter-t_ydiff >= 0 and (j+t_xdiff,iiter-t_ydiff) not in antip2):
                                    antip2.append((j+t_xdiff,iiter-t_ydiff))
                                if(not(ix-t_xdiff < xLen and ix-t_xdiff >= 0 and k+t_ydiff < yLen and k+t_ydiff >= 0)
                                   and not(j+t_xdiff < xLen and j+t_xdiff >= 0 and iiter-t_ydiff < yLen and iiter-t_ydiff >= 0 )):
                                    bothOB=True
                                iteration+=1

        iiter+=1

    p1+=len(antip1)
    print(p1)
    print("Part 2")    
    p2+=len(antip2) 
    print(p2)
