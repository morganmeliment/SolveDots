"""
Sources: http://www.tutorialspoint.com/python/list_remove.htm
"""
line1 = "gyrrry" #input("First Line:")
line2 = "rggyyg" #input("Second Line:")
line3 = "rypyyg" #input("Third Line:")
line4 = "rrpyyb" #input("Fourth line:")
line5 = "ygrrrg" #input("Fifth Line:")
line6 = "ppypgg" #input("Sixth Line:")

grid = {1: line1, 2: line2, 3: line3, 4: line4, 5: line5, 6: line6}

def findsurrounding(row, index, color):
    finalret = []
    if row > 1:
        finalret.append([row - 1, index])
    else:
        finalret.append([])
    if row < 6:
        finalret.append([row + 1, index])
    else:
        finalret.append([])
    if index > 1:
        finalret.append([row, index - 1])
    else:
        finalret.append([])
    if index < 6:
        finalret.append([row, index + 1])
    else:
        finalret.append([])
    top = ""
    right = ""
    bottom = ""
    left = ""
    itera = 0
    selfpotentialcombos = []
    for pos in finalret:
        itera += 1
        if itera == 1:
            if pos != []:
                top = list(grid[pos[0]])[pos[1] - 1]
        elif itera == 2:
            if pos != []:
                bottom = list(grid[pos[0]])[pos[1] - 1]
        elif itera == 3:
            if pos != []:
                left = list(grid[pos[0]])[pos[1] - 1]
        elif itera == 4:
            if pos != []:
                right = list(grid[pos[0]])[pos[1] - 1]
    if top == color:
        selfpotentialcombos.append([row - 1, index])
    if right == color:
        selfpotentialcombos.append([row, index + 1])
    if bottom == color:
        selfpotentialcombos.append([row + 1, index])
    if left == color:
        selfpotentialcombos.append([row, index - 1])
    return selfpotentialcombos

squares = []
connectedshapes = []
longlines = []

dotnum = 0
dotrow = 0
for row in grid:
    dotrow += 1
    for dot in list(grid[row]):
        dotnum = (dotnum % 6) + 1
        surrounding = findsurrounding(dotrow, dotnum, dot)
        stringofdots = []
        shape = "single"
        if len(surrounding) > 0:
            shape = "double"
        for combodot in surrounding:
            stringofdots = [[dotrow, dotnum], combodot]
            nextsurrounding = findsurrounding(combodot[0], combodot[1], dot)
            nextsurrounding.remove([dotrow, dotnum])
            if len(nextsurrounding) > 0:
                    shape = "triple"
            for anotherdot in nextsurrounding:
                stringofdots = [[dotrow, dotnum], combodot, anotherdot]
                nnextsurrounding = findsurrounding(anotherdot[0], anotherdot[1], dot)
                nnextsurrounding.remove(combodot)
                if len(nnextsurrounding) >= 1:
                    shape = "quad"
                    for aanotherdot in nnextsurrounding:
                        nnnextsurrounding = findsurrounding(aanotherdot[0], aanotherdot[1], dot)
                        nnnextsurrounding.remove(anotherdot)
                        if nnnextsurrounding.count([dotrow, dotnum]) >= 1:
                            shape = "square"
                            stringofdots = [[dotrow, dotnum], combodot, anotherdot, aanotherdot]
                            canapp = True
                            for sd in squares:
                                yount = 0
                                for sx in sd:
                                    for sa in stringofdots:
                                        if sx == sa:
                                            yount += 1
                                if yount == 4:
                                    canapp = False
                            if canapp == True:
                                squares.append(stringofdots)
print(squares)








































