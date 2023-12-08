#we could upgrade list of operations and make simplifications on the coefficients of the systeme

def addParenthesisToSymbols(symbols):

    newSymbols=[]

    for symbol in symbols:
        if len(symbol) > 1 :
            newSymbols.append('('+symbol+')')
        else:
            newSymbols.append(symbol)

    return newSymbols

def systemeOfNodesLanguages(AEF):
    #supposing AEF is determinist
    #supposing symbols are str
    
    nodes=AEF[0]
    symbols=AEF[1]
    symbols=addParenthesisToSymbols(symbols)
    path=AEF[2]
    nbNodes=len(nodes)

    system={}
    for i in range(nbNodes):    #initializing a linear systeme of nbNodes equation of nbNodes parameters
        
        coefSystem={'Cst' : ''}
        for j in range(nbNodes):
            coefSystem['L'+str(j)]=''
        
        system['BL'+str(i)]=coefSystem

    for i in range(len(path)):   #walkthrough path and update system
        for j in range(len(path[i])):
            if len(path[i][j])==1: #supposing AEF is determinist
                system['BL'+str(i)]['L'+str(path[i][j][0])]+=symbols[j]+'+'

    for key, equation in system.items():   #walkthrough system and correcting previous values by deleting '+' and adding '()'
        print(equation)
        for keyCoef, coef in equation.items():
            equation[keyCoef]=coef[:-1]    
            if len(equation[keyCoef]) > 1 and (equation[keyCoef][0] != '(' or equation[keyCoef][-1] != ')'):  #todo only if coef[-1]=='+'
                equation[keyCoef]='('+coef[:-1]+')'

    return system

def makeSubstitution(system,op):  #a ameliorer avec des simplification de formule???? verifier les posibilités de simplification au moment ou on fait l'op

    opLine=op[0]
    opCoefIndex=op[1]

    if opLine==opCoefIndex:
        exit('makeSubstitution1')

    equation0=system['BL'+str(opLine)]
    equation1=system['BL'+str(opCoefIndex)]

    coef=equation0['L'+str(opCoefIndex)]  #coef is the coeficient in front of the parameter that will be substitute 
    equation0['L'+str(opCoefIndex)]=''    #after substitution de line that take substitution do not depend anymore from the value we substitute

    for keyCoefEq1, coefEq1 in equation1.items():
        if coefEq1 != '':
            if equation0[keyCoefEq1] != '':
                equation0[keyCoefEq1]='('+equation0[keyCoefEq1]+'+'+coef+coefEq1+')'
            else :
                equation0[keyCoefEq1]=coef+coefEq1

def noDependanceOfLn(equation):

    for i in range(len(equation)-1):
        if equation['L'+str(i)] != '':
            return False
        
    return True

def makeLemmaOfArden(system,op):

    opLine=op[0]
    opCoefIndex=op[1]
    if opLine!=opCoefIndex :
        exit('makeLemmaOfArden1')
    coefSystem=system['BL'+str(opLine)]

    coef=coefSystem['L'+str(opCoefIndex)]        #coef is the coeficient in front of the parameter that will ardenise + the '*' sign ( aL+b = a*b )
    if len(coef) > 1 and (coef[0] != '(' or coef[-1] != ')'):   #put coef to the right form for being readable
        coef='('+coef+')'+'*'  
    else:
        coef=coef+'*'
    
    coefSystem['L'+str(opCoefIndex)]=''
    done=False          #doing the lemma of arden operation
    for keyCoefEq, coefEq in coefSystem.items():
        if coefEq != '' : 
            coefSystem[keyCoefEq]=coef+coefSystem[keyCoefEq]
            if keyCoefEq == 'Cst':
                done=True 

    if noDependanceOfLn(coefSystem) and not done:
        coefSystem['Cst']=coef+coefSystem['Cst']

def tradAEFToMatrixOfRelations(AEF):

    nodes=AEF[0]
    path=AEF[2]

    matrixOfRelations = []

    # Initialisation of a new 2D matrix that contains zeros
    for i in range(len(nodes)):
        matrixOfRelations.append([0] * len(nodes))
    
    for i in range(len(path)):    #walkthrought the matrix of the AEF
       for j in range(len(path[i])):
            if len(path[i][j])!=0:
                matrixOfRelations[i][path[i][j][0]]=1   #supposing AEF is determinist
     
    return matrixOfRelations
           
def makeOperation(matrixOfRelations,op):
    
    opLine=op[0]
    opCoefIndex=op[1]

    matrixOfRelations[opLine][opCoefIndex]=0
    for i in range(len(matrixOfRelations[opLine])):
        if matrixOfRelations[opCoefIndex][i] == 1:
            matrixOfRelations[opLine][i] = 1

def listOfOperations(matrixOfRelations):

    list=[]

    for i in reversed(range(len(matrixOfRelations))):
        for j in reversed(range(i+1)):
            if matrixOfRelations[j][i]==1:
                list.append([j,i])
            if j != i :
                makeOperation(matrixOfRelations,[j,i])

    return list 

''' Test :
NodeList=['@q0','q1','#q2']
SymbolList=['a','b','c']
M=[[[2],[1],[0]],[[2],[1],[0]],[[0],[1],[2]]]
AEF=[NodeList,SymbolList,M]

S=systemeOfNodesLanguages(AEF)
print(S)
M=tradAEFToMatrixOfRelations(AEF)
print(M)
L=listOfOperations(M)
print(L)


for op in L :
    a=op[0]
    b=op[1]

    if a==b:
        makeLemmaOfArden(S,op)
    else:
        makeSubstitution(S,op)

    print(S)


print(S['BL0']['Cst'])
'''