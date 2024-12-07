import itertools
def runDay(input):
    p1 = 0
    p2 = 0
    print("Part 1 * Part 2")    

    ctr=0
    for i in [item.replace('\n', '') for item in input]:
        ctr+=1
        if ctr%50==0:
            print(ctr)
        t_split=i.split(": ")
        total=int(t_split[0])
        nums=[int(x) for x in t_split[1].split(" ")]
        #P1
        ops=["+","*"]
        combos=list(itertools.product(ops, repeat=len(nums)-1))
        if(total%(nums[len(nums)-1])!=0):
            combos=[i for i in combos if i[-1]!="*"]
        for combo in combos:                
            #print(combo)
            if(calculateCombo(nums, combo)==total):
                p1+=total
                break
        #P2
        ops=["+","*","||"]
        combos=list(itertools.product(ops, repeat=len(nums)-1))
        if(total%(nums[len(nums)-1])!=0):
            combos=[i for i in combos if i[-1]!="*"]
        for combo in combos:
            if(calculateCombo(nums, combo)==total):
                p2+=total
                break

    print(p1)          
    print(p2)

def calculateCombo(nums, combo):
    t_tot=nums[0]
    for j in range(1,len(nums)):
        if(combo[j-1]=="*"):
            t_tot*=nums[j]
        elif(combo[j-1]=="+"):
            t_tot+=nums[j]
        elif(combo[j-1]=="||"):
            t_tot=int(str(t_tot)+str(nums[j]))
    return t_tot