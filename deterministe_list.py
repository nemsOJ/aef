def getElementInAef(path, nodes, symbols) :
    # Get elements of chosen coordinate in a 3 dimensional list.
    # path is a 3 dimensional list. nodes is the list of chosen nodes. symbols is the symbol's index (integer).
    # Return a list.

    newPath = []
    for i in nodes :

        if i > len(path) -1 or i < 0 : # Check existing knot
            print('Error type in getElementInAef _ 1')
            exit(1)

        if symbols > len(path[i]) -1 or i < 0 : # Check existing symbol
            print('Error type in getElementInAef _ 2',symbols)
            exit(1)

        for k in path[i][symbols] : # Add element to newPath
            if k not in newPath :
                newPath.append(k)

    return newPath

def isDeterminist(path) :
    # Check if the given AEF is determinist.
    # aef is a 3 dimensional list.
    # Return a boolean.

    for i in path :
        for k in i :
            if len(k) > 1 :
                return False

    return True

def makeDeterministPath(path):
    newPath = [path[0]]
    indexOfOldNodes = [[0]]

    for i in newPath:
        for k in i:
            if len(k) != 0 and k not in indexOfOldNodes:
                indexOfOldNodes.append(k)
                newPath.append([])
                for j in range(len(path[0])):
                    newPath[-1].append(getElementInAef(path, k, j))

    print("Path Dimensions:", len(path), len(path[0]), len(path))

    return [newPath, indexOfOldNodes]


def concatenateWordsToMakeDeterminist(words) :   #merge a list of word and if a word is a final node add a # in front of the merging
    isEndingNode = False
    newNode=''

    for i in words:
        if len(i)!=0:
            if i[0]=='#':
                isEndingNode = True
                i=i[1:]
            newNode+=i

    if isEndingNode :
        newNode='#'+newNode
    
    return newNode

def makeDeterministAef(aef) :     # trad the new graph with simple element ( {q0,q1}---->S1   ,   {q1,q2}---->S2,   ....)
    oldPathAndIndex = makeDeterministPath(aef[2])
    newPath = oldPathAndIndex[0]
    indexOfOldNodes = oldPathAndIndex[1]
    newNodes=[]
    
    for i in range(len(newPath)) :  # run through the new graph and remplace element by they index
        for j in range(len(newPath[i])) :
            if len(newPath[i][j]) > 0 :
                try :
                    newPath[i][j] = [indexOfOldNodes.index(newPath[i][j])]
                except :
                    exit(1)

    for i in range(len(indexOfOldNodes)) :  # merge node names if necessary
        words = []
        for j in range(len(indexOfOldNodes[i])) :
            words.append(aef[0][indexOfOldNodes[i][j]])
        newNodes.append(concatenateWordsToMakeDeterminist(words))

    return [newNodes, aef[1], newPath]
