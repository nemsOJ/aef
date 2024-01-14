listOfForbiddenNode=['NodeToCompleteAutomate','']
listOfForbiddenSymbols=['(',')',';','+','*']

def RemoveDuplicates(list):
    newList=[]
    for element in list:                 #remove duplicates
        if element not in newList:
            newList.append(element)
    
    return newList

def TransitionValid(pathList,nodes,symbols):   #verify transition validity 

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
    print("Enter nodes in format : node1,node2,.....,nodeN ")
    print("Write @node for starting nodes")
    print("Write #node for ending nodes")
    print("Write @#node if starting and ending node")
    allNodes = input()

    nodeList=allNodes.split(",")

    for i in range (len(nodeList)):     #check node validity
        if ";" in nodeList[i]:
            print("Error, the node :",nodeList[i],"can't countain ';' character")
            exit()
    
    nodeList=RemoveDuplicates(nodeList)

    for node in nodeList:
        for forbiddenNode in listOfForbiddenNode:
            if node==forbiddenNode:
                print('Error :',forbiddenNode ,'is a forbidden node name')
                exit('Error input node')
    

   
    for node in nodeList:               #counting ending node
       if isFinalNode(node):
            nbEndingNode += 1
    
    if nbEndingNode == 0 :
        print("Error : no final node")   #error if no final node
        exit()

    
    for node in nodeList:               #counting starting node
       if isStartingNode(node):
            nbBeginningNode += 1
    
    
    if nbBeginningNode == 0 :
        print("Error : no starting node")   #error if no initial node
        exit()

    return nodeList

def InputSymbols():      
 
    print("Enter Symbols in format : symbol1,symbol2,....,symbolsN")
    allSymbols = input()

    symbolsList=allSymbols.split(",")

    for i in range (len(symbolsList)):     #check symbolsList validity
        if ";" in symbolsList[i]:
            print("Error, the Symbol :",symbolsList[i],"can't countain ';' character")
            exit()

    symbolsList=RemoveDuplicates(symbolsList)

    for symbol in symbolsList:
        for forbiddenSymbol in listOfForbiddenSymbols:
            if forbiddenSymbol in symbol:
                print("Error, the Symbol :",symbol,"can't countain",forbiddenSymbol,"character")
                exit('Error in input symbol')

    if '' in symbolsList:
        print('Error : empty symbol is not accepted, ε symbo correspond to empty symbol')
        exit('Error in input symbol')

    return symbolsList

def InputTransition(nodes,symbols):   
    
    print("Enter pathList in fromat : ")
    print("startingnode1,symbol1,symbole2,.....,symboleN,arrivalNode1;startingnode2,s1,s2,....,arrivalnode2;......")
    allPath = input()

    pathList=allPath.split(";")

    for i in range(len(pathList)):
        if not TransitionValid(pathList[i],nodes,symbols):
            print("Error :",pathList[i],"is not a valid path")   #############
            exit()
    
    pathList=RemoveDuplicates(pathList)
        
    return pathList
    
def TranslateInputsIntoMatrix(nodes,symbols,allPath):

    M = MatriceOfLists(len(nodes),len(symbols))

    for i in range(len(allPath)):
        pathList=allPath[i].split(",")
        indexStartingNode=index(pathList[0],nodes)
        indexFinalNode=index(pathList[-1],nodes)
              
        symbols=pathList[1:-1]
        symbols=RemoveDuplicates(symbols)    

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



AEF = CreateAEF()

print(AEF[0])
print(AEF[1])
print(AEF[2])
