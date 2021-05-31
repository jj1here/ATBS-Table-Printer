tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data) :

    colWidth = []

    for i in data :
        word = ""
        for j in i :
            if len(j) > len(word) :
                word = j
        colWidth.append(len(word))
    table = []
    for i in range(len(data)) :
        temp = []
        for j in data[i] :
            temp.append(j.rjust(colWidth[i]))
        table.append(temp)

    final = []
    for i in range(len(table[0])) :
        temp = []
        for j in range(len(table)) :
            temp.append(table[j][i])
        print(" ".join(temp))


# print(tableData)
printTable(tableData)





