"""
Sources: http://www.tutorialspoint.com/python/list_remove.htm
"""

roundscores = []

lineone = "bggppp"
linetwo = "bgyrry"
linethree = "pyprbb"
linefour = "rpprbb"
linefive = "rybybr"
linesix = "rgbrgp"

def isasquare(points):
    squareis = False
    for poinqt in points:
        if points.count(poinqt) > 1:
            squareis = True
    return squareis

def findmovesonboard(line1, line2, line3, line4, line5, line6, findindiv):
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
    
    yellowsquares = []
    bluesquares = []
    greensquares = []
    purplesquares = []
    redsquares = []
    
    def checkup(thedots, thecolor):
        if len(thedots) >= 5:
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
        shud = True
        for dotsx in dotzx:
            if list(grid[dotsx[0]])[dotsx[1] - 1] == ' ':
                shud = False
        if shud == True:
            for valdot in anymove:
                couont = 0
                for aval in dotzx:
                    if aval in valdot[0]:
                        couont += 1
                if couont == len(valdot[0]) and len(valdot[0]) == len(dotzx):
                    shud = False
        if shud == True:
            anymove.append([dotzx, colf])
    
    dotnum = 0
    dotrow = 0
    for row in grid:
        dotrow += 1
        for dot in list(grid[row]):
            if dot != ' ':
                dotnum = (dotnum % 6) + 1
                surrounding = findsurrounding(dotrow, dotnum, dot)
                stringofdots = [[dotrow, dotnum]]
                if findindiv == True:
                    istruemove(stringofdots, dot)
                shape = "single"
                connecting = False
                if len(surrounding) > 0:
                    shape = "double"
                for combodot in surrounding:
                    stringofdots = [[dotrow, dotnum], combodot]
                    istruemove(stringofdots, dot)
                    nextsurrounding = findsurrounding(combodot[0], combodot[1], dot)
                    nextsurrounding.remove([dotrow, dotnum])
                    if len(nextsurrounding) > 0:
                        shape = "triple"
                    for anotherdot in nextsurrounding:
                        stringofdots = [[dotrow, dotnum], combodot, anotherdot]
                        istruemove(stringofdots, dot)
                        nnextsurrounding = findsurrounding(anotherdot[0], anotherdot[1], dot)
                        nnextsurrounding.remove(combodot)
                        if len(nnextsurrounding) >= 1:
                            shape = "quad"
                        for aanotherdot in nnextsurrounding:
                            stringofdots = [[dotrow, dotnum], combodot, anotherdot, aanotherdot]
                            istruemove(stringofdots, dot)
                            nnnextsurrounding = findsurrounding(aanotherdot[0], aanotherdot[1], dot)
                            nnnextsurrounding.remove(anotherdot)
                            if len(nnnextsurrounding) >= 1:
                                shape = "quint"
                            for aaanotherdot in nnnextsurrounding:
                                stringofdots = [[dotrow, dotnum], combodot, anotherdot, aanotherdot, aaanotherdot]
                                istruemove(stringofdots, dot)
                                nnnnextsurrounding = findsurrounding(aaanotherdot[0], aaanotherdot[1], dot)
                                nnnnextsurrounding.remove(aanotherdot)
                                if len(nnnnextsurrounding) >= 1:
                                    shape = "hecta"
                                for aaaanotherdot in nnnnextsurrounding:
                                    stringofdots = [[dotrow, dotnum], combodot, anotherdot, aanotherdot, aaanotherdot, aaaanotherdot]
                                    istruemove(stringofdots, dot)
                                    nnnnnextsurrounding = findsurrounding(aaaanotherdot[0], aaaanotherdot[1], dot)
                                    nnnnnextsurrounding.remove(aaanotherdot)
                                    if len(nnnnnextsurrounding) >= 1:
                                        shape = "sept"
                                    for aaaaanotherdot in nnnnnextsurrounding:
                                        stringofdots = [[dotrow, dotnum], combodot, anotherdot, aanotherdot, aaanotherdot, aaaanotherdot, aaaaanotherdot]
                                        istruemove(stringofdots, dot)
                                        nnnnnnextsurrounding = findsurrounding(aaaaanotherdot[0], aaaaanotherdot[1], dot)
                                        nnnnnnextsurrounding.remove(aaaanotherdot)
                                        if len(nnnnnnextsurrounding) >= 1:
                                            shape = "octa"
            else:
                dotnum = (dotnum % 6) + 1

    potentialmoves = []
    
    for randommove in anymove:
        if len(randommove[0]) >= 5:
            if isasquare(randommove[0]) == True:
                checkup(randommove[0], randommove[1])
            else:
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
    
    return(potentialmoves)

roundonepossiblemoves = findmovesonboard(lineone, linetwo, linethree, linefour, linefive, linesix, True)

def removedots(lineoneq, linetwoq, linethreeq, linefourq, linefiveq, linesixq, possmove):
    gridline = [list(lineoneq), list(linetwoq), list(linethreeq), list(linefourq), list(linefiveq), list(linesixq)]
    pointstoremove = []
    if len(possmove[1]) > 4:
        if isasquare(possmove[1]) == True:
            cvb = 0
            for colodot in list(lineoneq):
                cvb += 1
                if colodot == possmove[0]:
                    pointstoremove.append([1, cvb])
            cvb = 0
            for colodot in list(linetwoq):
                cvb += 1
                if colodot == possmove[0]:
                    pointstoremove.append([2, cvb])
            cvb = 0
            for colodot in list(linethreeq):
                cvb += 1
                if colodot == possmove[0]:
                    pointstoremove.append([3, cvb])
            cvb = 0
            for colodot in list(linefourq):
                cvb += 1
                if colodot == possmove[0]:
                    pointstoremove.append([4, cvb])
            cvb = 0
            for colodot in list(linefiveq):
                cvb += 1
                if colodot == possmove[0]:
                    pointstoremove.append([5, cvb])
            cvb = 0
            for colodot in list(linesixq):
                cvb += 1
                if colodot == possmove[0]:
                    pointstoremove.append([6, cvb])
        else:
            pointstoremove = possmove[1]
    else:
        pointstoremove = possmove[1]
    
    for point in pointstoremove:
        pointsaboveremove = []
        num = point[0]
        while num > 0:
            pointsaboveremove.append([num, point[1]])
            num -= 1
        num = len(pointsaboveremove)
        for pointtwo in pointsaboveremove:
            num -= 1
            if num == 0:
                gridline[0][pointtwo[1] - 1] = " "
            else:
                gridline[pointtwo[0] - 1][pointtwo[1] - 1] = gridline[pointtwo[0] - 2][pointtwo[1] - 1]
    return gridline

for move in roundonepossiblemoves:
    roundonescore = move[2]
    potarry = removedots(lineone, linetwo, linethree, linefour, linefive, linesix, move)
    newpotarry = []
    for line in potarry:
        finstrin = ""
        for letter in line:
            finstrin = finstrin + letter
        newpotarry.append(finstrin)
    roundtwopossiblemoves = findmovesonboard(newpotarry[0], newpotarry[1], newpotarry[2], newpotarry[3], newpotarry[4], newpotarry[5], False)
    highestpossibledotremoval = 0
    bestoutcomefortheround = []
    eachround = [0, 0]
    for movetwo in roundtwopossiblemoves:
        moveresult = movetwo[2] + move[2]
        if highestpossibledotremoval <= moveresult:
            highestpossibledotremoval = moveresult
            if eachround[1] < move[2]:
                bestoutcomefortheround = [move, movetwo]
                eachround = [move[2], movetwo[2]]
    roundscores.append(bestoutcomefortheround)

highestpossibledotremoval = 0
bestoutcomefortheround = []
for moves in roundscores:
    moveresult = moves[0][2] + moves[1][2]
    if highestpossibledotremoval < moveresult:
        highestpossibledotremoval = moveresult
        bestoutcomefortheround = [moves[0], moves[1]]
print(highestpossibledotremoval)
print(bestoutcomefortheround)
































