
def IsComplete(aef):
	#verifie if a graphe is complete
    #aef is our graph
    #return a bollean
	
	path = aef[2]

	for i in range(len(path)):   # verifie if element in path is empty
		for j in range(len([i])):
			if len(path[i][j])==0:
				return False  #if  a element is empty that's mean graph is not complete
	return True

def MakeComplete(aef): #make a graph complete
	#aef is our graph
	#return a new graph
    
	NodesList = aef[0]
	path = aef[2]

	if IsComplete(aef):   #if graph is complete do nothing 
		return aef

	NodesList.append("NodeToCompleteAutomate")    #add a final node in the node list (representing new node)
	ind=len(NodesList) - 1

	addline=[]
	for k in range(len(path[0])):  #create a new empty line 
		addline.append([])       
	
	path.append(addline)   #add the empty line in path

	for i in range(len(path)):
		for j in range(len(path[i])):    #if a connection doesn't exist connect to NodeToCompleteAutomate
			if len(path[i][j])==0:
				path[i][j].append(ind)

	
	aef[0]=NodesList
	aef[2]=path

	return aef
