import math
def runDay(input):
    p1 = 0
    p2 = 0
    directions=[]
    updates=[]
    invalid=[]
    for i in input:
        i=i.replace("\n","")
        if "|" in i:
            directions.append(i.split("|"))
        elif "," in i:
            updates.append(i.split(","))
        
    for u in updates:
        if is_valid(u,directions):
            p1+=int(u[int((len(u)-1)/2)])
        else:
            valid = False
            newyou = u
            while(not valid):
                newyou=is_valid_mod(newyou,directions)
                if(is_valid(newyou,directions)):
                    valid = True
                    p2+=int(newyou[int((len(newyou)-1)/2)])
    
    

    print("Part 1")
    print(p1)
    print("Part 2")           
    print(p2)

def search_nested_array(array, target):
    return [(i, j) for i, sub_array in enumerate(array) for j, element in enumerate(sub_array) if element == target]

def is_valid(u,directions):
    for c in u: #nt
        loc = search_nested_array(directions,c)
        for l in loc:
            if l[1] == 0 and directions[l[0]][1] in u and u.index(c) > u.index(directions[l[0]][1]):
                return False
    return True

def is_valid_mod(u,directions):
    for c in u: #nt
        loc = search_nested_array(directions,c)
        for l in loc:
            if l[1] == 0 and directions[l[0]][1] in u and u.index(c) > u.index(directions[l[0]][1]):
                t = u[:u.index(directions[l[0]][1])] + [c] + [directions[l[0]][1]] + u[u.index(directions[l[0]][1])+1:u.index(c)]+  u[u.index(c)+1:]
                return t
    return u