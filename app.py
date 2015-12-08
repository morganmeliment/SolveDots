line1 = "gryyby" #input("First Line:")
line2 = "prgpbb" #input("Second Line:")
line3 = "bbggpb" #input("Third Line:")
line4 = "gyybbr" #input("Fourth line:")
line5 = "pypbyb" #input("Fifth Line:")
line6 = "byppbb" #input("Sixth Line:")

grid = {1: line1, 2: line2, 3: line3, 4: line4, 5: line5, 6: line6}

def findsurrounding(row, index):
    return [[row - 1, index - 1], [row - 1, index], [row - 1, index + 1], [row, index - 1], [row, index], [row, index + 1], [row + 1, index - 1], [row + 1, index], [row + 1, index + 1]]

dotnum = 0
dotrow = 0
for row in grid:
    dotrow += 1
    stringrow = list(grid[row])
    for dot in stringrow:
        dotnum = (dotnum % 6) + 1
        print(dotrow, dotnum)