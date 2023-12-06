def displayAef(aef) :
    # Display the AEF in the terminal.
    # Takes a 3 dimensionnal list.

    print('Voici les noeuds de l\'AEF :')
    for i in aef[0] :
        print(i)
    print()

    print('Voici les symboles de l\'AEF :')
    for j in aef[1] :
        print(j)
    print()

    print('Voici liens de l\'AEF:')
    for i in range(len(aef[0])) :
        for j in range(len(aef[1])) :
            for k in range(len(aef[2][i][j])) :
                print(aef[0][i], '->', aef[1][j], '->', aef[0][int(aef[2][i][j][k])])

def displayAefWithIndex(aef) :
    # Display the AEF in the terminal with the index.
    # Takes a 3 dimensionnal list.
    
    for i in range(len(aef[2])) :
        for j in range(len(aef[2][i])) :
            for k in range(len(aef[2][i][j])) :
                print(i, '->', j, '->', aef[2][i][j][k])

'''Test
aef = [['#verouiller', '#deverouiller'], ['pousser', 'jeton'], [[[], [1, 0]], [[0], [1]]]]
displayAef(aef)
'''