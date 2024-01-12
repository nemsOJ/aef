from deterministe_list import*
from AEF_operand import*

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

    aefB2=makeDeterministAef(aefB)
    aefB2=makeComplement(aefB2)
    aefC=mutliplyAef(aefA,aefB2)

    return notRecogniseEmptyLanguage(aefC)


def isEquivalent(aefA, aefB):
    
    return AincludeInB(aefA, aefB) and AincludeInB(aefB, aefA)