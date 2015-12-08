line1 = "gryyby" #input("First Line:")
line2 = "prgpbb" #input("Second Line:")
line3 = "bbggpb" #input("Third Line:")
line4 = "gyybbr" #input("Fourth line:")
line5 = "pypbyb" #input("Fifth Line:")
line6 = "byppbb" #input("Sixth Line:")

grid = {"one" => line1, "two" => line2, "three" => line3, "four" => line4, "five" => line5, "six" => line6}

dotnum = 0
dotrow = 1
for dot in grid:
    if dotnum == 5:
        dotrow += 1
    dotnum = (dotnum + 1) % 6
    print(dotrow, dotnum)
    