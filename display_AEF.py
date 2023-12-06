all_matrice = [['#verouiller', '#deverouiller'], ['pousser', 'jeton'], [[[], [1, 0]], [[0], [1]]]]

def display(all_matrice) :
    # Display the AEF in the terminal.
    # Takes a 3 dimensionnal list.

    print('Voici les noeuds de l\'AEF :')
    for i in all_matrice[0] :
        print(i)
    print()

    print('Voici les symboles de l\'AEF :')
    for j in all_matrice[1] :
        print(j)
    print()

    print('Voici liens de l\'AEF:')
    for i in range(len(all_matrice[0])) :
        for j in range(len(all_matrice[1])) :
            for k in range(len(all_matrice[2][i][j])) :
                print(all_matrice[0][i], '->', all_matrice[1][j], '->', all_matrice[0][int(all_matrice[2][i][j][k])])

def display_int(all_matrice) :
    # Display the AEF in the terminal with the index.
    # Takes a 3 dimensionnal list.
    
    for i in range(len(all_matrice[2])) :
        for j in range(len(all_matrice[2][i])) :
            for k in range(len(all_matrice[2][i][j])) :
                print(i, '->', j, '->', all_matrice[2][i][j][k])

# display(all_matrice)