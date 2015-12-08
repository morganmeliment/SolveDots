line1 = "gryyby" #input("First Line:")
line2 = "prgpbb" #input("Second Line:")
line3 = "bbggpb" #input("Third Line:")
line4 = "gyybbr" #input("Fourth line:")
line5 = "pypbyb" #input("Fifth Line:")
line6 = "byppbb" #input("Sixth Line:")

grid = {1: line1, 2: line2, 3: line3, 4: line4, 5: line5, 6: line6}

def findsurrounding(row, index):
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
    return finalret

potentialcombos = []

dotnum = 0
dotrow = 0
for row in grid:
    dotrow += 1
    stringrow = list(grid[row])
    for dot in stringrow:
        dotnum = (dotnum % 6) + 1
        surrounding = findsurrounding(dotrow, dotnum)
        for pos in surrounding:
            top = grid[pos[0]]
            print(top)