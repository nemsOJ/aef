
def ChooseWord():    #return a word choosen by user, word can contain ';'

    w = input()

    if ";" in w :
        print("Automate can't recognise string with a ';' caracter")
        exit()

    return w 

def index(elt,list):  #return index of a elt in a list, return -1 if elt is not in list
    
    n = -1

    for i in range(len(list)):
        
        if elt == list[i]:
            n = i
            return n
        
    return n

def Move(M,symbol,initNode,NodeList,SymbolList):    #automate(M) should be determinist/return arrival node after moving or -1 if can't move

    iN=index(initNode,NodeList)        
    iS=index(symbol,SymbolList)

    L=M[iN][iS]                #L is the list containing arrival nodes 

    if len(L)==1:              
        return NodeList[L[0]]  #return arrival node after moving
    if len(L)==0:                    
        return (";")           #return -1 if can't move in symbol path
    if len(L) > 1:
        exit()                 #exit if multiple choice for arrival
    
def ListOfInitialNodes(all_mat):

    nodes=all_mat[0]

    list=[]

    for i in nodes :
        if len(i)!=0:
            if i[0] == '@':
                list.append(i)
    
    return list

def AEFRecogniseW1(WordL,all_mat,firstnode):

    nodes = all_mat[0]
    symbols = all_mat[1]
    M = all_mat[2]

    for i in range(len(WordL)):        #verifying if all caracter of the word is a symbol of aef
        if WordL[i] not in symbols:
            return False

    count=0
    Q=firstnode

    if Q[0] != "#" and len(WordL)==0:    # don't recognise "" if first node of automate is not a finishing node 
        return False

    while( Q != ";" and count != len(WordL)):     #while we can move and we moved less then len(word), we move and pass to next caracter

        L = WordL[count]  #leng(WordL)>0
        Q = Move (M,L,Q,nodes,symbols)
        count += 1

    if Q == ";":        #if we end because we can't move return false
        return False
    
    if Q[0] == "#":     #if we and because count == len(word) verify if Q is a finishing node if yes return true 
        return True
    else:
        return False

def AEFRecogniseWord(all_mat):

    initnodes = ListOfInitialNodes(all_mat)
    print(initnodes)

    word=ChooseWord()   
    WordL=list(word.strip())

    TFlist = []

    for node in initnodes:
        TFlist.append(AEFRecogniseW1(WordL,all_mat,node))

    if len(TFlist)==0:
        print("error AEFRecigniseWord 1")
        exit()
    
    if True in TFlist :
        return True 
    else :
        return False



#partie test 
NodeList=['@fff','1','#2']
SymbolList=['a','e','i','o','u']
M=[[[1],[1],[1],[1],[1]],[[2],[2],[2],[2],[2]],[[2],[2],[2],[],[]]]

AEF=[NodeList,SymbolList,M]

print(M)



print(AEFRecogniseWord(AEF))