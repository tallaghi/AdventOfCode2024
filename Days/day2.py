

def runDay(input):
    
    print("Part 1")
    p1 = 0
    p2 = 0
    inputs = [i.replace("\n","").split(" ") for i in input]    
    for i in range(0,len(inputs)):
        if(runInput(inputs[i]) > 0):
            p1+=1
            p2+=1
        else:
            for j in range(0,len(inputs[i])):
                t_list = inputs[i][:j] + inputs[i][j+1:]
                if(runInput(t_list)>0):
                    p2+=1
                    break
    print(p1)
    print("Part 2")        
    print(p2)

def runInput(inputs):
    isSafe = True
    inc = True
    if(int(inputs[0]) > int(inputs[1])):
        inc = False
    for j in range(1,len(inputs)):
        if (inc and int(inputs[j-1]) >= int(inputs[j])) or (not inc and int(inputs[j-1]) <= int(inputs[j])) or (abs(int(inputs[j-1]) - int(inputs[j])) > 3):
            isSafe = False
    if isSafe:
        return 1
    return 0        