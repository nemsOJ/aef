'''
Translate a file content into a matrice.

The file has to be in the following form :
knot number 0; knot number 1; ...
symbol number 0; symbol number 1; ...
(Arrow comming from the knot number 0) number of the symbol, number of the arrival knot; number of the symbol, number of the arrival knot; ...
(Arrow comming from the knot number 1) number of ...
...

Exemple of file :
verouiller;deverouiller
pousser;jeton
1,1;1,0
0,0;1,1

The form of the returned matrice :
[
    [[name of the knot number 0], [name of the knot number 1], ...],
    [[name of the symbol number 0], [name of the symbol number 1], ...],
    [
        [
            [arrivals knots comming from the knot number 0 by the symbol number 0],
            [arrivals knots comming from the knot number 0 by the symbol number 1], ...
        ], [
            [arrivals knots comming from the knot number 1 by the symbol number 0],
            [arrivals knots comming from the knot number 1 by the symbol number 1], ...
        ]
    ], ...
]

Matrice created with the exemple file given :
[
    ['verouiller', 'deverouiller']],
    ['pousser', 'jeton'],
    [
        [
            [],
            ['1', '0']
        ], [
            ['0'],
            ['1']
        ]
    ]
]

If the file is not in the asked form, the matrice should be fill with blanks.
If the given file does not exist or the user dos not have the right to read the given file, a message error should be shown.
'''

def read_file(file_name):
    # Open a file (named by 'file_name'), read it and translate the inside informations into a list.
    # Takes a string (file_name).
    # Return a list if all went well. Return -1 if the function could not open the chosen file.

    # Declaration
    try: # Check if the file can be opened
        file = open(file_name, "r")
    except OSError:
        print ("Nous n'avons pas pu ouvrir votre fichier.\nVeuillez vérifier que vous avez bien sélectionné le nom du fichier existant.")
        return -1
    lines = file.readlines()
    all_matrice = []

    # Create 2 lists (one for knot's names (all_matrice[0]), one for symbol's names (all_matrice[1])) in one (all_matrice)
    for k in range (2):
        lines[k] = lines[k][:-1] # Delete '\n' character
        try :
            all_matrice[k] = lines[k].split(";")
        except :
            all_matrice.append(lines[k].split(";"))
        
    # Add the list of arrows (all_matrice[2]) to the list (all_matrice)
    for k in range (2, len(lines)): # For each knot (line (after the second one) in the file)
        lines[k] = lines[k][:-1] # Delete '\n' character

        arrows = lines[k].split(";")
        for i in arrows :
            arrow = i.split(",")

            try :
                all_matrice[2]
            except :
                all_matrice.append([])

            try :
                all_matrice[2][k - 2]
            except :
                all_matrice[2].append([])

            oki = True
            while(oki):
                try :
                    all_matrice[2][k - 2][int(arrow[0])].append(int(arrow[1]))
                    oki = False
                except :
                    all_matrice[2][k - 2].append([])

    return all_matrice

def check_indices(all_matrice) :
    # Check if the AEF is right.
    # Takes a 3 dimensionnal list.
    # Return -1 if an error has occure or 0 if the AEF is right.

    nb_node = len(all_matrice[0])
    nb_symbols = len(all_matrice[1])

    # Check if the number of node is the same at the beginning and at the end of your file
    if len(all_matrice[2]) > nb_node :
        print('Le nombre de noeud n\'est pas le même au début et à la fin de votre fichier.')
        return -1

    for i in all_matrice[2] :
        
        # Check if the number of symbols is not the same at the beginning and at the end of your file
        if len(i) > nb_symbols :
            print('Le nombre de symboles n\'est pas le même au début et à la fin de votre fichier.')
            return -1
        
        for k in i :

            # Check if your nodes goes to another whith exist
            for j in k :
                if int(j) > nb_node :
                    print('Un de vos noeuds va dans dans un noeud qui n\'existe pas.')
                    return -1
    
    return 0

def main():
    # Exemple d'éxecution

    M = read_file(input('Veuillez sélectionner le nom du fichier souhaité\n'))

    if M == -1 :
        return 1
    
    if check_indices(M) == -1 :
        return 1
    
    # Initialise
    knots = M[0]
    symbols = M[1]
    mat = M[2]

    # Display results
    print(M)
    print('List of knots :', knots)
    print('List of symbols :', symbols)
    print('List of mat :', mat)

    return 0

main()