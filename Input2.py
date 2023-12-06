#a faire :
#gestion des erreur doublon ou input invalid dans inputnodes et inputsymbols
#gestion des ,, dans inputnodes,symbols et transitions
#est ce genant que des node et des symbols est le meme blaze ??c non 
#est ce genant que deux noeuds est le meme blaze #################
# si deux meme symboles enlever les doublons
#gestion des , et ; en fin de saisi 
#ou on gere les doublon ? direct en input ou dans la matrice direct?
#symbol ou noeud vide interdit ??????????? pour reconnaissance language peut poser probleme
#pour l'instant on enleve les doublons et exit si pb
#noeud ou symbols interdits

def PrintMatriceOfLists(M):   #si M n'est pas de bonne nature ? nique en vrai c'est que du visuel le temps de tester
    for i in range(len(M)):
        print(M[i])

def RemoveDuplicates(list):
    temp=list
    list=[]
    for elt in temp:                 #remove duplicates
        if elt not in list:
            list.append(elt)
    
    return list

def TransitionValid(transition,NodesList,SymbolsList):

    list=transition.split(",")

    if list[0] not in NodesList:
        return False
    
    if list[-1] not in NodesList:
        return False
    
    for i in range(len(list)-2):
        if list[i+1] not in SymbolsList:
            return False
        
    return True

def index(elt,list):  

    for i in range(len(list)):
        if elt == list[i]:
            n = i
            return n
        
    if elt not in list:
        exit(54)

def MatriceOfLists(rowsNb,columsNb):

    M=[]
    for i in range(rowsNb):
        row=[]
        for j in range(columsNb):
            row.append([])
        M.append(row)

    return M

def isStartingNode(node):

    if node[0]=='@':
        return True
    else:
        return False

def isFinalNode(node):

    if node[0] == '#':
        return True
    
    if len(node)>1:
        if node[:2]:
            return True
        
    return False

def InputNodes():

    nbfn = 0    #nbfn is number of final nodes  
    nbin = 0    #nbin in number of initial node 
    print("Enter nodes :")
    Nodes = input()

    NodesList=Nodes.split(",")

    for i in range (len(NodesList)):     #check node validity
        if ";" in NodesList[i]:
            print("Error, the node :",NodesList[i],"can't countain ';' character")
            exit()
    
    NodesList=RemoveDuplicates(NodesList)

    node=""
    for j in range(len(NodesList)):   #counting number of final nodes
        node=NodesList[j]
        if node[0] == "#":
            nbfn += 1
    
    if nbfn == 0 :
        print("Error : no final node")   #error if no final node
        exit()

    node=""
    for j in range(len(NodesList)):   #counting number of initial nodes
        node=NodesList[j]
        if node[0] == "@":
            nbin += 1
    
    if nbin == 0 :
        print("Error : no starting node")   #error if no initial node
        exit()

    return NodesList

def InputSymbols():      
 
    print("Enter Symbols :")
    Symbols = input()

    SymbolsList=Symbols.split(",")

    for i in range (len(SymbolsList)):     #check Symbols validity
        if ";" in SymbolsList[i]:
            print("Error, the Symbol :",SymbolsList[i],"can't countain ';' character")
            exit()

    SymbolsList=RemoveDuplicates(SymbolsList)

    return SymbolsList

def InputTransition(NodesList,SymbolsList):    #gerer les a,s,s,s,s,s,s,s,a
    
    print("Enter transitions :")
    Transitions = input()

    TransitionsList=Transitions.split(";")

    for i in range(len(TransitionsList)):
        if not TransitionValid(TransitionsList[i],NodesList,SymbolsList):
            print("Error :",TransitionsList[i],"is not a valid transition")   #############
            exit()
    
    
    
    
    TransitionsList=RemoveDuplicates(TransitionsList)
        #gerer les a,s,s,s,s,s,s,a et supprimer les transition equivalentes ex: a,s,d,a et a,d,s,a  (les bibliotheques seraient utiles)




    return TransitionsList
    
def TranslateInputsIntoMatrix(NodesList,SymbolsList,TransitionsList):

    M = MatriceOfLists(len(NodesList),len(SymbolsList))

    for i in range(len(TransitionsList)):
        transition=TransitionsList[i].split(",")
        isn=index(transition[0],NodesList)
        ifn=index(transition[-1],NodesList)
              
        SList=transition[1:-1]
        SList=RemoveDuplicates(SList)    #a voir avec comment on gere les doublon...

        for j in range(len(SList)):
            x=index(SList[j],SymbolsList)
            M[isn][x].append(ifn)

    return M

def CreateAEF():

    nodes = InputNodes()
    symbols = InputSymbols()
    transitions = InputTransition(nodes,symbols)
    M = TranslateInputsIntoMatrix(nodes,symbols,transitions)

    all_mat=[nodes,symbols,M]

    return all_mat 



AEF = CreateAEF()

print(AEF[0])
print(AEF[1])
print(AEF[2])