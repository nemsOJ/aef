def readAefFile(fileName):
    # Open a file (named by 'fileName'), read it and translate the inside informations into a list.
    # Takes a string (fileName).
    # Return a list if all went well. Return -1 if the function could not open the chosen file.

    # Declaration
    try: # Check if the file can be opened
        file = open(fileName, "r")
    except OSError:
        print ("Nous n'avons pas pu ouvrir votre fichier.\nVeuillez vérifier que vous avez bien sélectionné le nom du fichier existant.")
        return -1
    lines = file.readlines()
    aef = []

    # Create 2 lists (one for knot's names (aef[0]), one for symbol's names (aef[1])) in one (aef)
    for k in range (2):
        lines[k] = lines[k][:-1] # Delete '\n' character
        try :
            aef[k] = lines[k].split(";")
        except :
            aef.append(lines[k].split(";"))
        
    # Add the list of path (aef[2]) to the list (aef)
    for k in range (2, len(lines)): # For each knot (line (after the second one) in the file)
        lines[k] = lines[k][:-1] # Delete '\n' character

        path = lines[k].split(";")
        for i in path :
            elementsInPath = i.split(",")

            try : # Checking if an element of the list exist (memory space allocated), add one (memory space) if not
                aef[2]
            except :
                aef.append([])

            try : # Checking if an element of the list exist (memory space allocated), add one (memory space) if not
                aef[2][k - 2]
            except :
                aef[2].append([])

            isTheMemoryAllocated = False
            while(not isTheMemoryAllocated): # Checking if an element of the list exist (memory space allocated), add one (memory space) while it's not
                try :
                    aef[2][k - 2][int(elementsInPath[0])].append(int(elementsInPath[1])) # Add path
                    isTheMemoryAllocated = True
                except :
                    aef[2][k - 2].append([])

    return aef

def check_indices(aef) :
    # Check if the AEF is right.
    # Takes a 3 dimensionnal list.
    # Return -1 if an error has occure or 0 if the AEF is right.

    nbNodes = len(aef[0])
    nbSymbols = len(aef[1])

    # Check if the number of node is the same at the beginning and at the end of your file
    if len(aef[2]) > nbNodes :
        print('Le nombre de noeud n\'est pas le même au début et à la fin de votre fichier.')
        return -1

    for i in aef[2] :
        
        # Check if the number of symbols is not the same at the beginning and at the end of your file
        if len(i) > nbSymbols :
            print('Le nombre de symboles n\'est pas le même au début et à la fin de votre fichier.')
            return -1
        
        for k in i :

            # Check if your nodes goes to another which exist
            for j in k :
                if int(j) > nbNodes :
                    print('Un de vos noeuds va dans dans un noeud qui n\'existe pas.')
                    return -1
    
    return 0

''' Test :
aef = readAefFile(input('Select the file name your going to use :'))

if aef == -1 :
    exit(1)

print(aef)
'''