def RemoveDuplicates(list):
    newList=[]
    for element in list:                 #remove duplicates
        if element not in newList:
            newList.append(element)
    
    return newList

def TransitionValid(pathList,nodes,symbols):

    list=pathList.split(",")

    if list[0] not in nodes:
        return False
    
    if list[-1] not in nodes:
        return False
    
    for i in range(len(list)-2):
        if list[i+1] not in symbols:
            return False
        
    return True

def index(element,list):  

    for i in range(len(list)):
        if element == list[i]:
            n = i
            return n
        
    if element not in list:
        exit(54)

def MatriceOfLists(rowsNb,columsNb):

    emptyPath=[]
    for i in range(rowsNb):
        row=[]
        for j in range(columsNb):
            row.append([])
        emptyPath.append(row)

    return emptyPath

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

    nbEndingNode = 0    #nbEndingNode is number of final nodes  
    nbBeginningNode = 0    #nbBeginningNode in number of initial node 
    print("Enter nodes :")
    allNodes = input()

    nodeList=allNodes.split(",")

    for i in range (len(nodeList)):     #check node validity
        if ";" in nodeList[i]:
            print("Error, the node :",nodeList[i],"can't countain ';' character")
            exit()
    
    nodeList=RemoveDuplicates(nodeList)

    node=""
    for j in range(len(nodeList)):   #counting number of final nodeList
        node=nodeList[j]
        if node[0] == "#":
            nbEndingNode += 1
    
    if nbEndingNode == 0 :
        print("Error : no final node")   #error if no final node
        exit()

    node=""
    for j in range(len(nodeList)):   #counting number of initial nodeList
        node=nodeList[j]
        if node[0] == "@":
            nbBeginningNode += 1
    
    if nbBeginningNode == 0 :
        print("Error : no starting node")   #error if no initial node
        exit()

    return nodeList

def InputSymbols():      
 
    print("Enter Symbols :")
    allSymbols = input()

    symbolsList=allSymbols.split(",")

    for i in range (len(symbolsList)):     #check symbolsList validity
        if ";" in symbolsList[i]:
            print("Error, the Symbol :",symbolsList[i],"can't countain ';' character")
            exit()

    symbolsList=RemoveDuplicates(symbolsList)

    return symbolsList

def InputTransition(nodes,symbols):    #gerer les a,s,s,s,s,s,s,s,a
    
    print("Enter pathList :")
    allPath = input()

    pathList=allPath.split(";")

    for i in range(len(pathList)):
        if not TransitionValid(pathList[i],nodes,symbols):
            print("Error :",pathList[i],"is not a valid transition")   #############
            exit()
    
    pathList=RemoveDuplicates(pathList)
        #gerer les a,s,s,s,s,s,s,a et supprimer les transition equivalentes ex: a,s,d,a et a,d,s,a  (les bibliotheques seraient utiles)

    return pathList
    
def TranslateInputsIntoMatrix(nodes,symbols,allPath):

    M = MatriceOfLists(len(nodes),len(symbols))

    for i in range(len(pathList)):
        pathList=allPath[i].split(",")
        indexStartingNode=index(pathList[0],nodes)
        indexFinalNode=index(pathList[-1],nodes)
              
        symbols=pathList[1:-1]
        symbols=RemoveDuplicates(symbols)    #a voir avec comment on gere les doublon...

        for j in range(len(symbols)):
            x=index(symbols[j],symbols)
            M[indexStartingNode][x].append(indexFinalNode)

    return M

def CreateAEF():

    nodes = InputNodes()
    symbols = InputSymbols()
    transitions = InputTransition(nodes,symbols)
    path = TranslateInputsIntoMatrix(nodes,symbols,transitions)

    aef=[nodes,symbols,path]

    return aef 


'''Test
AEF = CreateAEF()

print(AEF[0])
print(AEF[1])
print(AEF[2])
'''