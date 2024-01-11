def isAccessible(aef, nodeIndex, checkedNodes) :
    # Check if the given an aef is accessible.
    # Takes (aef :) a 3 dimensional list (corresponding to an AEF), (nodeIndex :) an int corresponding to the index of the node to be checked, and (checkedNodes :) a list of in corresponding to indexes of already checked nodes.
    # Returns 0 if the given aef is not accessible. Retuns more than 0 if the given aef is accessible.

    # Initialise
    nodes = aef[0]
    symbols = aef[1]
    paths = aef[2]
    res = 0

    if (nodes[nodeIndex][0] == '@') : # The chosen node is a beginning one
        return 1
    
    for i in checkedNodes : # The node has already been checked
        if nodeIndex == i :
            return 0
    
    for i in range(len(nodes)) : # For each node that arrive in nodeIndex
        if i != nodeIndex :
            for j in range(len(symbols)) :
                for k in paths[i][j] :
                    if k == nodeIndex :
                        checkedNodes.append(nodeIndex)
                        res += isAccessible(aef, i, checkedNodes) # Recall the function

    return res

def isCoAccessible(aef, nodeIndex, checkedNodes) :
    # Check if the given aef is co-accessible.
    # Takes (aef :) a 3 dimensional list (corresponding to an AEF), (nodeIndex :) an int corresponding to the index of the node to be checked, and (checkedNodes :) a list of in corresponding to indexes of already checked nodes.
    # Returns 0 if the given aef is not co-accessible. Retuns more than 0 if the given aef is co-accessible.

    # Initialise
    nodes = aef[0]
    symbols = aef[1]
    paths = aef[2]
    res = 0

    if (nodes[nodeIndex][0] == '#' or nodes[nodeIndex][:2] == "@#") : # The chosen node is an ending one
        return 1
    
    for i in checkedNodes : # The node has already been checked
        if nodeIndex == i :
            return 0
    
    for i in range(len(symbols)) : # For each arrivals nodes of nodeIndex
        for j in paths[nodeIndex][i] :
            if j != nodeIndex :
                checkedNodes.append(nodeIndex)
                res += isCoAccessible(aef, j, checkedNodes) # Recall the function

    return res

def removeElt(list, index) :
    # Creates a list without a chosen element.
    # Takes (list :) a list, and (index :) an int corresponding to the index of an element in the list.
    # Returns a list.

    if (index < 0 or index > len(list)) : # Returns the givent list, in case the index is not right
        return list

    # Delete the chosen element
    if len(list) >= 2 :
        list.pop(index)
        newList = list
    else :
        newList = [] # Keep the type of newList

    return newList

def deleteNode(aef, nodeIndex) :
    # Delete a node from an AEF.
    # Takes (aef :) a 3 dimensional list (corresponding to an AEF), and (nodeIndex :) an int corresponding to the index of the node to be deleted.
    # Returns a 3 dimensional list (corresponding to an AEF).

    # Initialise
    nodes = aef[0]
    symbols = aef[1]
    paths = aef[2]

    # Create a new AEF without the chosen node
    newNodes = removeElt(nodes, nodeIndex)
    newPaths = removeElt(paths, nodeIndex)

    # Delete the old node from arrivals nodes
    for i in range(len(newNodes)) :
        for j in range(len(symbols)) : # For each arrivals nodes from nodeIndex
            for k in range(len(newPaths[i][j])) :
                if newPaths[i][j][k] == nodeIndex :
                    newPaths[i][j] = removeElt(newPaths[i][j], k)
                elif newPaths[i][j][k] > nodeIndex : # Change index of nodes, if their index is superior to nodeIndex
                    newPaths[i][j][k] -= 1

    return [newNodes, symbols, newPaths]

def makePruned(aef) :
    # Make the given aef pruned.
    # Takes (aef :) a 3 dimensional list (corresponding to an AEF).
    # Returns a 3 dimensional list (corresponding to an pruned AEF).

    # Initialise
    nodes = aef[0]
    symbols = aef[1]
    paths = aef[2]
    newAef = [nodes, symbols, paths]
    nodeIndex = 0

    while nodeIndex != len(newAef[0]) :
        if (isCoAccessible(aef, nodeIndex, []) == 0) :
            newAef = deleteNode(aef, nodeIndex)
            nodeIndex -= 1
        nodeIndex += 1
    
    nodeIndex = 0
    while nodeIndex != len(newAef[0]) :
        if (isAccessible(aef, nodeIndex, []) == 0) :
            newAef = deleteNode(aef, nodeIndex)
            nodeIndex -= 1
        nodeIndex += 1

    return newAef
