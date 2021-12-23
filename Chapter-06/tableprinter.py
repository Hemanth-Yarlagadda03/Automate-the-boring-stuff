tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
n=len(tableData)
def printtable(tableData):
    colWidths = [0] * n
    for y in range(n):
        for x in tableData[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)
    for x in range(len(tableData[0])) :
        for y in range(n) :
            print(tableData[y][x].rjust(colWidths[y]), end = ' ')
        print()
        

printtable(tableData)