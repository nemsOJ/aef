from display_AEF import *
from deterministe_list import *
from CompletAEF import *
from Imput2 import removeDuplicates

def makeComplement(aef) :
    # Creates a complementary AEF of the given one.
    # Takes a 3 dimensional list (corresponding to an AEF).
    # Returns a 3 dimensional list (corresponding to an AEF).

    # Make the given AEF determinist and complete
    aef = makeDeterministAef(aef)
    aef = makeComplete(aef)

    newNodes = []
    nodes = ''
    symbols = ''
    
    # Inverse ending nodes and unending nodes names
    for i in range(len(aef[0])) :
        nodes = aef[0][i]
        symbols = ''

        if nodes[0] == '@' : # Starting nodes
            symbols += '@'
            nodes = nodes[1:]

        if nodes[0] != '#' :  # Unending nodes
            symbols += '#'

        else :  # Ending nodes
            nodes = nodes.replace('#', '', 1)

        newNodes.append(symbols + nodes)

    return [newNodes, aef[1], aef[2]]

def makeMiror(aef) :
    # Creates a miror AEF of the given one.
    # Takes a 3 dimensional list (corresponding to an AEF).
    # Returns a 3 dimensional list (corresponding to an AEF).

    # Make the given AEF determinist and complete
    aef = makeDeterministAef(aef)
    aef = makeComplete(aef)

    newAef = [[], aef[1], []]
    node = ''
    
    # Inverse ending nodes and starting nodes
    for i in range(len(aef[0])) :
        node = aef[0][i]
        if node[0] == '#' : # Ending nodes
            node = "@" + node[1:]
        elif node[0] == '@' and node[1] != '#': # Starting and not ending nodes
            node = "#" + node[1:]
        newAef[0].append(node)

    # Initialise newAef[2] to avoid ".append"
    for i in range(len(aef[2])) :
        newAef[2].append([])
        for j in range(len(aef[2][i])) :
            newAef[2][i].append([])

    # Inverse directions of transitions
    for i in range(len(aef[0])) :
        for j in range(len(aef[2])) :
            for k in range(len(aef[2][j])) :
                for l in range(len(aef[2][j][k])) :
                    if i == aef[2][j][k][l] :
                        newAef[2][i][k].append(j)

    return newAef

def concatenateWordsToMultiplyAef(words) :
    # Merge a list of 2 words and if they are final nodes add a # in front of the merging.
    # Takes a list of words (strings).
    # Returns a string.

    isEndingNode = False
    isBeginningNode = False
    newNode=''

    for i in words:
        isEndingNode = False
        isBeginningNode = False
        if len(i)!=0: # The node has a name
            if i[0]=='@': # Beginning nodes
                i=i[1:]
                isBeginningNode = True
            if i[0]=='#': # Ending nodes
                i=i[1:]
                isEndingNode = True
        newNode += i

    if isEndingNode : # Ending nodes
        newNode='#'+newNode

    if isBeginningNode : # Beginning nodes
        newNode='@'+newNode
    
    return newNode

def mutliplyAef(aef1, aef2) :
    # Create the product of two AEF.
    # Takes a two 3 dimensional list (corresponding to an AEF).
    # Returns a 3 dimensional list (corresponding to an AEF).

    # Make the given AEF determinists and completes
    aef1 = makeDeterministAef(aef1)
    aef1 = makeComplete(aef1)
    aef2 = makeDeterministAef(aef2)
    aef2 = makeComplete(aef2)

    newAef = [[], [], []]

    # Get name of nodes
    for i in aef1[0] :
        for j in aef2[0] :
            newAef[0].append(concatenateWordsToMultiplyAef([i, j]))

    # Get name of communs symbols
    newSymbols = []
    for i in aef1[1] :
        if i in aef2[1] :
            newSymbols.append(i)
    newAef[1] = newSymbols
    
    # Initialise newAef[2] to avoid ".append"
    for i in range(len(newAef[0])) :
        newAef[2].append([])
        for j in range(len(newAef[1])) :
            newAef[2][i].append([])

    # Get transitions
    for i in range(len(newAef[0])) : # For nodes
        for j in range(len(newAef[1])) : # For symboles

            # Translate previous coordinates into old coordinates
            i1 = i // (min(len(aef1[0]), len(aef2[0])) + 1)
            i2 = i % (min(len(aef1[0]), len(aef2[0])) + 1)
            j1 = j % len(aef1[1])
            j2 = j // len(aef1[1])

            # Go though transitions of aef1 and aef2 to add the right nodes
            for k1 in aef1[2][i1][j1] :
                for k2 in aef2[2][i2][j2] :
                    k = k1 * len(newAef[0]) + k2 # Translate old coordinates into previous coordinates
                    newAef[2][i][j].append(k)

    return newAef

def makeWordsDifferents(words) :
    # Change a node name if 2 nodes has the same name.
    # Takes a list of node names (list of strings).
    # Return a list of node names (list of strings).

    isChanged = False # Did we made a change ?

    for i in range(len(words)) :
        for j in range(len(words)) :
            if words[i] == words[j] and i != j :
                words[j] = words[j] + '.1'
                isChanged = True
    
    if isChanged : # Make sure we did not change a node into an other existing node
        words = makeWordsDifferents(words)
    
    return words

def concatenateAef(aef1, aef2) :
    # Concatenate two AEF.
    # Takes two 3 dimensional list (corresponding to an AEF).
    # Returns a 3 dimensional list (corresponding to an AEF).

    # Make the given AEF determinists and completes
    aef1 = makeDeterministAef(aef1)
    aef1 = makeComplete(aef1)
    aef2 = makeDeterministAef(aef2)
    aef2 = makeComplete(aef2)

    newAef = [[], [], []]

    # Get name of nodes
    # From aef1, add them as unending nodes
    for i in aef1[0] :
        if len(i) > 0 :
            if i[0] == '#' :
                i = i[1:]
        if len(i) > 0 :
            if i[:2] == '@#' :
                i = '@' + i[2:]
        newAef[0].append(i)
    # From aef2, add them as unbeginning nodes
    for i in aef2[0] :
        if i[0] == '@' :
            i = i[1:]
        newAef[0].append(i)
    newAef[0] = makeWordsDifferents(newAef[0])

    # Get name of symbols
    for i in aef1[1] :
        newAef[1].append(i)
    for i in aef2[1] :
        newAef[1].append(i)
    newAef[1].append('') # Add the espilon node
    newAef[1] = removeDuplicates(newAef[1])
    
    # Initialise newAef[2] to avoid ".append"
    for i in range(len(newAef[0])) :
        newAef[2].append([])
        for j in range(len(newAef[1])) :
            newAef[2][i].append([])

    # Get transitions

    # Add old transitions
    for i in range(len(aef1[2])) : # From aef1
        for j in range(len(aef1[2][i])) :
            for k in aef1[2][i][j] :
                newAef[2][i][j].append(k)
    for i in range(len(aef2[2])) : # From aef2
        for j in range(len(aef2[2][i])) :
            for k in aef2[2][i][j] :
                newAef[2][len(aef1[0]) + i][j].append(k)

    # Add new transitions (from ending ones of aef1 to begining ones in aef2)
    for i in range(len(aef1[0])) : # From aef1
        if aef1[0][i][0] == '#' or aef1[0][i][:2] == '@#' : # Node is an ending one
            for j in range(len(aef2[0])) : # From aef2
                if aef2[0][j][0] == '@' : # Node is a beginning one
                    newAef[2][i][-1].append(len(aef1[0]) + j)
                    
    return newAef

''' Tests :
aef1 = [["Q0", "Q1"], ['S0', 'S1'], [[[0], []], [[1, 0], []]]]
aef2 = [["1Q0", "1Q1"], ['S0', 'S1'], [[[], [0]], [[1], [0]]]]
display(mutliplyAef(aef1, aef2))
'''