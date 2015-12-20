"""
Sources: http://www.tutorialspoint.com/python/list_remove.htm
"""

line1 = "grpggg" #input("First Line:")
line2 = "rbrpry" #input("Second Line:")
line3 = "gppgyp" #input("Third Line:")
line4 = "bpggpr" #input("Fourth line:")
line5 = "bpbgry" #input("Fifth Line:")
line6 = "pypyyb" #input("Sixth Line:")

grid = {1: line1, 2: line2, 3: line3, 4: line4, 5: line5, 6: line6}

reccomendedmove = "undecided"

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

def isasquare(points):
    squareis = False
    if len(points) >= 4:
        for poinqt in points:
            newliste = []
            for poind in points:
                newliste.append(poind)
            newliste.remove(poinqt)
            for otherpoint in newliste:
                if otherpoint == poinqt:
                    squareis = True
    return squareis

yellowsquares = []
bluesquares = []
greensquares = []
purplesquares = []
redsquares = []

def checkup(thedots, thecolor):
    canapp = True
    if thecolor == "y":
        colorarray = yellowsquares
    if thecolor == "g":
        colorarray = greensquares
    if thecolor == "b":
        colorarray = bluesquares
    if thecolor == "r":
        colorarray = redsquares
    if thecolor == "p":
        colorarray = purplesquares
    for sd in colorarray:
        yount = 0
        for sx in sd:
            for sa in thedots:
                if sx == sa:
                    yount += 1
        if yount == len(thedots):
            canapp = False
    if canapp == True:
        colorarray.append(thedots)

anymove = []

def istruemove(dotzx, colf):
    if [dotzx, colf] not in anymove:
        anymove.append([dotzx, colf])

dotnum = 0
dotrow = 0
for row in grid:
    dotrow += 1
    for dot in list(grid[row]):
        dotnum = (dotnum % 6) + 1
        surrounding = findsurrounding(dotrow, dotnum, dot)
        stringofdots = [[dotrow, dotnum]]
        shape = "single"
        connecting = False
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
                    stringofdots = [[dotrow, dotnum], combodot, anotherdot, aanotherdot]
                    nnnextsurrounding = findsurrounding(aanotherdot[0], aanotherdot[1], dot)
                    nnnextsurrounding.remove(anotherdot)
                    if len(nnnextsurrounding) >= 1:
                        shape = "quint"
                    for aaanotherdot in nnnextsurrounding:
                        stringofdots = [[dotrow, dotnum], combodot, anotherdot, aanotherdot, aaanotherdot]
                        nnnnextsurrounding = findsurrounding(aaanotherdot[0], aaanotherdot[1], dot)
                        nnnnextsurrounding.remove(aanotherdot)
                        if len(nnnnextsurrounding) >= 1:
                            shape = "hecta"
                        for aaaanotherdot in nnnnextsurrounding:
                            stringofdots = [[dotrow, dotnum], combodot, anotherdot, aanotherdot, aaanotherdot, aaaanotherdot]
                            nnnnnextsurrounding = findsurrounding(aaaanotherdot[0], aaaanotherdot[1], dot)
                            nnnnnextsurrounding.remove(aaanotherdot)
                            if len(nnnnnextsurrounding) >= 1:
                                shape = "sept"
                            for aaaaanotherdot in nnnnnextsurrounding:
                                stringofdots = [[dotrow, dotnum], combodot, anotherdot, aanotherdot, aaanotherdot, aaaanotherdot, aaaaanotherdot]
                                nnnnnnextsurrounding = findsurrounding(aaaaanotherdot[0], aaaaanotherdot[1], dot)
                                nnnnnnextsurrounding.remove(aaaanotherdot)
                                if len(nnnnnnextsurrounding) >= 1:
                                    shape = "octa"

potentialmoves = []

for randommove in anymove:
    if len(randommove[0]) >= 5:
        #if isasquare(randommove[0]) == True:
       #     checkup(randommove[0], randommove[1])
       # else:
        potentialmoves.append([randommove[1], randommove[0], len(randommove[0])])
    else:
        potentialmoves.append([randommove[1], randommove[0], len(randommove[0])])

amntofyellowdots = 0
amntofgreendots = 0
amntofreddots = 0
amntofbluedots = 0
amntofpurpledots = 0

for linezq in grid:
    for dot12 in list(grid[linezq]):
        if dot12 == "y":
            amntofyellowdots += 1
        if dot12 == "g":
            amntofgreendots += 1
        if dot12 == "b":
            amntofbluedots += 1
        if dot12 == "r":
            amntofreddots += 1
        if dot12 == "p":
            amntofpurpledots += 1

for ysq in yellowsquares:
    potentialmoves.append(["y", ysq, amntofyellowdots])
for gsq in greensquares:
    potentialmoves.append(["g", gsq, amntofgreendots])
for bsq in bluesquares:
    potentialmoves.append(["b", bsq, amntofbluedots])
for psq in purplesquares:
    potentialmoves.append(["p", psq, amntofpurpledots])
for rsq in redsquares:
    potentialmoves.append(["r", rsq, amntofreddots])
    
highestpossibledotremoval = 0
bestoutcomefortheround = []
for move in potentialmoves:
    movecolor = move[0]
    moveposition = move[1]
    moveresult = move[2]
    if highestpossibledotremoval < moveresult:
        highestpossibledotremoval = moveresult
        bestoutcomefortheround = move

print(highestpossibledotremoval)
print(potentialmoves)







































