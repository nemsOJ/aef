
def IsComplete(all_mat):
	#verifie if a graphe is complete
    #all_mat is our graph
    #return a bollean
	
	M = all_mat[2]

	for i in range(len(M)):   # verifie if element in M is empty
		for j in range(len([i])):
			if len(M[i][j])==0:
				return False  #if  a element is empty that's mean graph is not complete
	return True

def MakeComplete(all_mat): #make a graph complete
	#all_mat is our graph
	#return a new graph
    
	NodesList = all_mat[0]
	M = all_mat[2]

	if IsComplete(all_mat):   #if graph is complete do nothing 
		return all_mat

	NodesList.append("NodeToCompleteAutomate")    #add a final node in the node list (representing new node)
	ind=len(NodesList) - 1

	addline=[]
	for k in range(len(M[0])):  #create a new empty line 
		addline.append([])       
	
	M.append(addline)   #add the empty line in M

	for i in range(len(M)):
		for j in range(len(M[i])):    #if a connection doesn't exist connect to NodeToCompleteAutomate
			if len(M[i][j])==0:
				M[i][j].append(ind)

	
	all_mat[0]=NodesList
	all_mat[2]=M

	return [all_mat]


