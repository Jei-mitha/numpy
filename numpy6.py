import numpy as np
#t=list([1,2,3,4,5,6,])
#y=np.array(t,dtype=int) #evenly spaced array
k=np.array([],dtype=int)
for i in range(5,100,5):
    k=np.append(k,i)
print("the evenly spaced array is :",k)