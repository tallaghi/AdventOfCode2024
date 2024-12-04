
def runDay(input):
    p1 = 0
    p2 = 0
    matrix = []    
    for i in input:
        i=i.replace("\n","")
        matrix.append([j for j in i])

    x = len(matrix)
    y = len(matrix[0])

    ans = []
    for i in range(x):
        for j in range(y):
            numMatches = findWord(matrix, i, j, "XMAS")
            if numMatches > 0:
                ans.append((i, j, numMatches))
                p1+=numMatches

    print("Part 1")
    print(p1)
    print("Part 2")           

    for i in range(1,x-1):
        for j in range(1,y-1):            
            if matrix[i][j] == "A":
                topLeft = matrix[i-1][j-1]
                topRight = matrix[i-1][j+1]
                botLeft = matrix[i+1][j-1]
                botRight = matrix[i+1][j+1]
                ltr = topLeft + "A" + botRight
                rtl = botLeft + "A" + topRight
                if(ltr == "MAS" or ltr == "SAM") and (rtl == "MAS" or rtl == "SAM"):
                    p2+=1
    print(p2)


def findWord(matrix, row, col, word):
    y = len(matrix)
    x = len(matrix[0])
    numMatches = 0
    if matrix[row][col] != word[0]:
        return False

    lenWord = len(word)

    dirX = [-1, -1, -1, 0, 0, 1, 1, 1]
    dirY = [-1, 0, 1, -1, 1, -1, 0, 1]
    for dir in range(8):
        currX, currY = row + dirX[dir], col + dirY[dir]
        k = 1
        while k < lenWord:
            if currX >= y or currX < 0 or currY >= x or currY < 0:
                break
            if matrix[currX][currY] != word[k]:
                break
            currX += dirX[dir]
            currY += dirY[dir]
            k += 1
        if k == lenWord:
            numMatches += 1

    return numMatches