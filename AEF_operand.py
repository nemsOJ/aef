from display_AEF import *
from deterministe_list import *
from CompletAEF import *
from Imput2 import RemoveDuplicates

def complement(all_mat) :
    # Creates a complementary AEF of the given one.
    # Takes a 3 dimensional list (corresponding to an AEF).
    # Returns a 3 dimensional list (corresponding to an AEF).

    # Make the given AEF determinist and complete
    all_mat = tradDeter(all_mat)
    all_mat = MakeComplete(all_mat)

    new_nodes = []
    nodes = ''
    sym = ''
    
    # Inverse ending nodes and unending nodes names
    for i in range(len(all_mat[0])) :
        nodes = all_mat[0][i]
        sym = ''

        if nodes[0] == '@' : # Starting nodes
            sym += '@'
            nodes = nodes[1:]

        if nodes[0] != '#' :  # Unending nodes
            sym += '#'

        else :  # Ending nodes
            nodes = nodes.replace('#', '', 1)

        new_nodes.append(sym + nodes)

    return [new_nodes, all_mat[1], all_mat[2]]

def miror(all_mat) :
    # Creates a miror AEF of the given one.
    # Takes a 3 dimensional list (corresponding to an AEF).
    # Returns a 3 dimensional list (corresponding to an AEF).

    # Make the given AEF determinist and complete
    all_mat = tradDeter(all_mat)
    all_mat = MakeComplete(all_mat)

    new_all_mat = [[], all_mat[1], []]
    node = ''
    
    # Inverse ending nodes and starting nodes
    for i in range(len(all_mat[0])) :
        node = all_mat[0][i]
        if node[0] == '#' : # Ending nodes
            node = "@" + node[1:]
        elif node[0] == '@' and node[1] != '#': # Starting and not ending nodes
            node = "#" + node[1:]
        new_all_mat[0].append(node)

    # Initialise new_all_mat[2] to avoid ".append"
    for i in range(len(all_mat[2])) :
        new_all_mat[2].append([])
        for j in range(len(all_mat[2][i])) :
            new_all_mat[2][i].append([])

    # Inverse directions of transitions
    for i in range(len(all_mat[0])) :
        for j in range(len(all_mat[2])) :
            for k in range(len(all_mat[2][j])) :
                for l in range(len(all_mat[2][j][k])) :
                    if i == all_mat[2][j][k][l] :
                        new_all_mat[2][i][k].append(j)

    return new_all_mat

def concatener_mult(mots) :
    # Merge a list of 2 words and if they are final nodes add a # in front of the merging.
    # Takes a list of words (strings).
    # Returns a string.

    hash = False
    aro = False
    res=''

    for i in mots:
        hash = False
        aro = False
        if len(i)!=0: # The node has a name
            if i[0]=='@': # Beginning nodes
                i=i[1:]
                aro = True
            if i[0]=='#': # Ending nodes
                i=i[1:]
                hash = True
        res += i

    if hash : # Ending nodes
        res='#'+res

    if aro : # Beginning nodes
        res='@'+res
    
    return res

def mult(all_mat_1, all_mat_2) :
    # Create the product of two AEF.
    # Takes a two 3 dimensional list (corresponding to an AEF).
    # Returns a 3 dimensional list (corresponding to an AEF).

    # Make the given AEF determinists and completes
    all_mat_1 = tradDeter(all_mat_1)
    all_mat_1 = MakeComplete(all_mat_1)
    all_mat_2 = tradDeter(all_mat_2)
    all_mat_2 = MakeComplete(all_mat_2)

    new_all_mat = [[], [], []]

    # Get name of nodes
    for i in all_mat_1[0] :
        for j in all_mat_2[0] :
            new_all_mat[0].append(concatener_mult([i, j]))

    # Get name of communs symbols
    new_sym = []
    for i in all_mat_1[1] :
        if i in all_mat_2[1] :
            new_sym.append(i)
    new_all_mat[1] = new_sym
    
    # Initialise new_all_mat[2] to avoid ".append"
    for i in range(len(new_all_mat[0])) :
        new_all_mat[2].append([])
        for j in range(len(new_all_mat[1])) :
            new_all_mat[2][i].append([])

    # Get transitions
    for i in range(len(new_all_mat[0])) : # For nodes
        for j in range(len(new_all_mat[1])) : # For symboles

            # Translate previous coordinates into old coordinates
            i1 = i // (min(len(all_mat_1[0]), len(all_mat_2[0])) + 1)
            i2 = i % (min(len(all_mat_1[0]), len(all_mat_2[0])) + 1)
            j1 = j % len(all_mat_1[1])
            j2 = j // len(all_mat_1[1])

            # Go though transitions of all_mat_1 and all_mat_2 to add the right nodes
            for k1 in all_mat_1[2][i1][j1] :
                for k2 in all_mat_2[2][i2][j2] :
                    k = k1 * len(new_all_mat[0]) + k2 # Translate old coordinates into previous coordinates
                    new_all_mat[2][i][j].append(k)

    return new_all_mat

def make_diff_cont(mots) :
    # Change a node name if 2 nodes has the same name.
    # Takes a list of node names (list of strings).
    # Return a list of node names (list of strings).

    change = False # Did we made a change ?

    for i in range(len(mots)) :
        for j in range(len(mots)) :
            if mots[i] == mots[j] and i != j :
                mots[j] = mots[j] + '.1'
                change = True
    
    if change : # Make sure we did not change a node into an other existing node
        mots = make_diff_cont(mots)
    
    return mots

def concatener_AEF(all_mat_1, all_mat_2) :
    # Concatenate two AEF.
    # Takes two 3 dimensional list (corresponding to an AEF).
    # Returns a 3 dimensional list (corresponding to an AEF).

    # Make the given AEF determinists and completes
    all_mat_1 = tradDeter(all_mat_1)
    all_mat_1 = MakeComplete(all_mat_1)
    all_mat_2 = tradDeter(all_mat_2)
    all_mat_2 = MakeComplete(all_mat_2)

    new_all_mat = [[], [], []]

    # Get name of nodes
    # From all_mat_1, add them as unending nodes
    for i in all_mat_1[0] :
        if len(i) > 0 :
            if i[0] == '#' :
                i = i[1:]
        if len(i) > 0 :
            if i[:2] == '@#' :
                i = '@' + i[2:]
        new_all_mat[0].append(i)
    # From all_mat_2, add them as unbeginning nodes
    for i in all_mat_2[0] :
        if i[0] == '@' :
            i = i[1:]
        new_all_mat[0].append(i)
    new_all_mat[0] = make_diff_cont(new_all_mat[0])

    # Get name of symbols
    for i in all_mat_1[1] :
        new_all_mat[1].append(i)
    for i in all_mat_2[1] :
        new_all_mat[1].append(i)
    new_all_mat[1].append('') # Add the espilon node
    new_all_mat[1] = RemoveDuplicates(new_all_mat[1])
    
    # Initialise new_all_mat[2] to avoid ".append"
    for i in range(len(new_all_mat[0])) :
        new_all_mat[2].append([])
        for j in range(len(new_all_mat[1])) :
            new_all_mat[2][i].append([])

    # Get transitions

    # Add old transitions
    for i in range(len(all_mat_1[2])) : # From all_mat_1
        for j in range(len(all_mat_1[2][i])) :
            for k in all_mat_1[2][i][j] :
                new_all_mat[2][i][j].append(k)
    for i in range(len(all_mat_2[2])) : # From all_mat_2
        for j in range(len(all_mat_2[2][i])) :
            for k in all_mat_2[2][i][j] :
                new_all_mat[2][len(all_mat_1[0]) + i][j].append(k)

    # Add new transitions (from ending ones of all_mat_1 to begining ones in all_mat_2)
    for i in range(len(all_mat_1[0])) : # From all_mat_1
        if all_mat_1[0][i][0] == '#' or all_mat_1[0][i][:2] == '@#' : # Node is an ending one
            for j in range(len(all_mat_2[0])) : # From all_mat_2
                if all_mat_2[0][j][0] == '@' : # Node is a beginning one
                    new_all_mat[2][i][-1].append(len(all_mat_1[0]) + j)
                    
    return new_all_mat

all_mat_1 = [["Q0", "Q1"], ['S0', 'S1'], [[[0], []], [[1, 0], []]]]
all_mat_2 = [["1Q0", "1Q1"], ['S0', 'S1'], [[[], [0]], [[1], [0]]]]
display(mult(all_mat_1, all_mat_2))