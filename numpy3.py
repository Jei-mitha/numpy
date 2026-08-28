#traversing string using np.array
import numpy as np
l=tuple([1,2,3,4,5,6,7,8,9,10,11,12])
x=np.array(l)
m='hello python'
n=''
d=''
for i in range(len(x)):
    if(i%2==0):
        n=n+m[i]
    else:
        d=d+m[i]
print("the even place value letters are:",n)
print("the odd place value letters are:",d)

#performing string concatenation
t=np.array([],dtype=int)
for i in range(len(x)):
    x[i]*=i
    t=np.append(t,x[i])
print("the multiplied array is ", t)


