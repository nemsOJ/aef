from deterministe_list import*
from AEF_operand import*

def copieList (tab) :
    copy = []
    for i in tab :
        if type(i) == list :
            copy.append(copieList(i))
        else :
            copy.append(i)

    return copy

def isFinalNode(node):

    if node[0] == '#':
        return True
    
    if len(node)>1:
        if node[:2]:
            return True
        
    return False

def isStartingNode(node):

    if node[0]=='@':
        return True
    else:
        return False

def neighbors(node,aef):

    path=aef[2]

    neighbors=[]
    for i in range(len(path[node])):
        neighbors.append(path[node][i])
    
    return neighbors

def notRecogniseEmptyLanguage(aef):

    accessible=[]
    toTreat=[]
    nodes = aef[0]
    for i in range(len(nodes)):
        if isStartingNode(nodes[i]):
            toTreat.append(i)

    while len(toTreat)!=0:
        p=toTreat.pop()
        if isFinalNode(p):
            return False
        else :
            for q in neighbors(p,aef):
                if q not in toTreat : 
                    toTreat.append(q)
        accessible.append(p)
    
    return True      

def AincludeInB(aefA, aefB):

    aefB=makeDeterministAef(aefB)
    aefB=makeComplement(aefB)
    aefC=mutliplyAef(aefA,aefB)

    return notRecogniseEmptyLanguage(aefC)

def isEquivalent(aefA, aefB):
    aefA2 = copieList(aefA)
    aefB2 = copieList(aefB)
    return AincludeInB(aefA, aefB) and AincludeInB(aefB2, aefA2)
