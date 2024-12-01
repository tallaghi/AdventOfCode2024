def runDay(input):
    
    print("Part 1")
    difference = 0
    input = [i.replace("\n","").split("   ") for i in input]
    l = []
    r = []
    for i in input:
        l.append(int(i[0]))
        r.append(int(i[1]))
    l.sort()
    r.sort()
    for i in range(0,len(l)):
        difference += abs(l[i]-r[i])
    print(difference)
    print("Part 2")
    similarity = 0
    for i in l:
        similarity += (i * r.count(i))
    print(similarity)