def get(mat, list, sym) :
    # Get elements of chosen coordinate in a 3 dimensional list.
    # mat is a 3 dimensional list. list is the list of chosen knots. sym is the symbol's index (integer).
    # Return a list.

    res = []

    for i in list :

        if i > len(mat) -1 or i < 0 : # Check existing knot
            print('Error type in get')
            exit(1)

        if sym > len(mat[i]) -1 or i < 0 : # Check existing symbol
            print('Error type in get')
            exit(1)

        for k in mat[i][sym] : # Add element to res
            if k not in res :
                res.append(k)

    return res

def EtreDeter(mat) :
    # Check if the given AEF is determinist.
    # mat is a 3 dimensional list.
    # Return a boolean.

    for i in mat :
        for k in i :
            if len(k) > 1 :
                return False

    return True

def RendreDeter(graphe) :
    # Make AEF determinist.
    # graphe is a 3 dimensional list.
    # Return a list.

    if EtreDeter(graphe): # Check if AEF is the given determinist.
        return graphe
    
    # Declaration
    new_graphe=[graphe[0]] # newgraph is the futur determinist graph 
    trad = [[0]] #r ecense new node of the futur determinist graph

    for i in new_graphe :
        for k in i :
            if len(k) != 0 and k not in trad :   # if k is not empty and k is not already a new node we add the node in trad and add a line to the new matrice
                trad.append(k)      
                new_graphe.append([])
                for j in range(len(graphe[2][0])):     # fill the new line of newgraph with the right elements
                    new_graphe[-1].append(get(graphe[2], k, j))

    return [new_graphe, trad]

def concatener(mots) :   #merge a list of word and if a word is a final node add a # in front of the merging
    hash = False
    res=''
    for i in mots:
        
        if len(i)!=0:
            if i[0]=='#':
                hash = True
                i=i[1:]
            res+=i

    if hash :
        res='#'+res
    
    return res


def tradDeter(all_mat) :     # trad the new graph with simple element ( {q0,q1}---->S1   ,   {q1,q2}---->S2,   ....)
    print('all_mat :', all_mat)
    list = RendreDeter(all_mat[2])
    new_graphe = list[0]
    trad = list[1]
    new_nodes=[]
    print('80 new_graphe :', new_graphe)
    for i in range(len(new_graphe)) :  # run through the new graph and remplace element by they index
        for j in range(len(new_graphe[i])) :
            if len(new_graphe[i][j]) > 0 :
                try :
                    new_graphe[i][j] = [trad.index(new_graphe[i][j])]
                except :
                    exit(1)

    for i in range(len(trad)) :  # merge node names if necessary
        mots = []
        for j in range(len(trad[i])) :
            mots.append(all_mat[0][trad[i][j]])
        new_nodes.append(concatener(mots))

    return [new_nodes, all_mat[1], new_graphe]
