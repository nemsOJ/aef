from SimplifyRE import*
from worldReconnaissance import*


#partie test 
NodeList=['@0','1','2','3','4','5','#6','7','#8']
SymbolList=['p','y','t','h','o','n','<','3']
M=[[[1],[],[],[],[],[],[],[]],[[],[2],[],[],[],[],[],[]],[[],[],[3],[],[],[],[],[]],[[],[],[],[4],[],[],[],[]],[[],[],[],[],[5],[],[],[]],[[],[],[],[],[],[6],[],[]],[[],[],[],[],[],[],[7],[]],[[],[],[],[],[],[],[],[8]],[[],[],[],[],[],[],[7],[]]]
AEF=[NodeList,SymbolList,M]

'''
r0=0
for i in range(len(M)):
    for j in range(len(SymbolList)):
        r0=random.randint(1, 3)
        if r0 == 1 :
            M[i][j].append(random.randint(0,5))
'''


def isFinalNode(node):

    if node[0] == '#':
        return True
    
    if len(node)>1:
        if node[:2]== '@#':
            return True
        
    return False

def addParenthesisToSymbols(symbols):

    new_list=[]

    for symbol in symbols:
        if len(symbol) > 1 :
            new_list.append('('+symbol+')')
        else:
            new_list.append(symbol)

    return new_list

def systemeOfNodesLanguages(AEF):
    #supposing AEF is determinist
    #supposing symbols are str
    
    nodes=AEF[0]
    symbols=AEF[1]
    symbols=addParenthesisToSymbols(symbols)
    mat=AEF[2]
    L=len(nodes)

    S={}
    for i in range(L):    #initializing a linear systeme of L equation of L parameters
        
        B={'Cst' : ''}
        if isFinalNode(nodes[i]):
            B['Cst']='εε'
        for j in range(L):
            B['L'+str(j)]=''
        
        S['BL'+str(i)]=B


    for i in range(len(mat)):   #walkthrough mat and update S
        for j in range(len(mat[i])):
            if len(mat[i][j])==1: #supposing AEF is determinist
                S['BL'+str(i)]['L'+str(mat[i][j][0])]+=symbols[j]+'+'

          
         
    for key, BL in S.items():   #walkthrough S and correcting previous values by deleting '+' and adding '()'
        for key_BL, elt in BL.items():
            BL[key_BL]=elt[:-1]    
            if len(BL[key_BL]) > 1 and (BL[key_BL][0] != '(' or BL[key_BL][-1] != ')'):  #todo only if elt[-1]=='+'
                BL[key_BL]='('+elt[:-1]+')'

    return S

def makeSubstitution(S,op):  

    a=op[0]
    b=op[1]
    if a==b:
        exit('makeSubstitution1')

    B0=S['BL'+str(a)]
    B1=S['BL'+str(b)]

    coef=B0['L'+str(b)]  #coef is the coeficient in front of the parameter that will be substitute 
    B0['L'+str(b)]=''    #after substitution de line that take substitution do not depend anymore from the value we substitute

    for key_B1, item in B1.items():
        if item != '':
            if B0[key_B1] != '':
                B0[key_B1]='('+B0[key_B1]+'+'+coef+item+')'
            else :
                B0[key_B1]=coef+item

def noDependanceOfLn(BL):

    for i in range(len(BL)-1):
        if BL['L'+str(i)] != '':
            return False
        
    return True

def makeLemmaOfArden(S,op):

    a=op[0]
    b=op[1]
    if a!=b :
        exit('Error : makeLemmaOfArden1')
    B=S['BL'+str(a)]

    coef=B['L'+str(b)]        #coef is the coeficient in front of the parameter that will ardenise + the '*' sign ( aL+b = a*b )
    if len(coef) > 1 and (coef[0] != '(' or coef[-1] != ')'):   #put coef to the right form for being readable
        coef='('+coef+')'+'*'  
    else:
        coef=coef+'*'
    
    B['L'+str(b)]=''
    done=False          #doing the lemma of arden operation
    for key_B, item in B.items():
        if item != '' : 
            B[key_B]=coef+B[key_B]
            if key_B == 'Cst':
                done=True 

    if noDependanceOfLn(B) and not done:
        B['Cst']=coef+B['Cst']

def tradAEFToMatrixOfRelations(AEF):

    nodes=AEF[0]
    mat=AEF[2]

    matrixOfRelations = []

    # Initialisation of a new 2D matrix that contains zeros
    for i in range(len(nodes)):
        temp = [0] * len(nodes) 
        matrixOfRelations.append(temp)
    
    for i in range(len(mat)):    #walkthrought the matrix of the AEF
       for j in range(len(mat[i])):
            if len(mat[i][j])!=0:
                matrixOfRelations[i][mat[i][j][0]]=1   #supposing AEF is determinist
     
    return matrixOfRelations
           
def makeOperation(M,op):
    
    a=op[0]
    b=op[1]

    M[a][b]=0
    for i in range(len(M[a])):
        if M[b][i] == 1:
            M[a][i] = 1

def listOfOperations(M):

    list=[]

    for i in reversed(range(len(M))):
        for j in reversed(range(i+1)):
            if M[j][i]==1:
                list.append([j,i])
                makeOperation(M,[j,i])

    return list 

def regularExpression(AEF):

    Systeme=systemeOfNodesLanguages(AEF)
    matrixOfRelations=tradAEFToMatrixOfRelations(AEF)
    listOfOp= listOfOperations(matrixOfRelations)

    for operation in listOfOp:
        a=operation[0]
        b=operation[1]

        if a==b:
            makeLemmaOfArden(Systeme,operation)
        else:
            makeSubstitution(Systeme,operation)

    RE=Systeme['BL0']['Cst']
    #RE=simplifyRE(RE,AEF)

    return RE

def language(AEF):

    regularEx = regularExpression(AEF)

    language= regularEx.replace('(','{').replace(')','}').replace('+','U')

    return language


print(regularExpression(AEF))