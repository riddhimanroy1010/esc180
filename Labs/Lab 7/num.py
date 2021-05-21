#Needed for array() and dot()
import numpy as np


#Printing matrices using NumPy:

#Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
#Now print it:
print(M)




#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.dot(M,x)        

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

#To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist() 

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]