#reshape of an array
import numpy as np
n=np.array([1,2,3,4,5,6,7,8,9,23,45,67])
d=n.reshape(3,4)
print(d)
u,l=np.vsplit(d,[2])
print(u,l)
#copy
p=n[1:7].copy()
p[5]=10
print(p)

#sum of the two arrays
k=(100,200,300,400,500,600,700,800)
l=np.array(k)
x=[20,30,40,50,60,70,80,90]
x=np.array(x)
h=np.array([l,x])
for i in range(len(x)):
    h[0,i]=h[0,i]+h[1,i]
print(h,l)

#concatenation
a1=np.array([1,2,3,4])
a2=np.array((5,6,7,8))
b=np.concatenate([a1,a2])
print(b)

#different dimensions
c=np.array([[2,3,4,5,6,7],[1,2,4,6,7,9]])
g=np.array([[7,8,9,5,4,5],[6,8,9,7,6,4]])
print(np.vstack([c,g]))
print(np.hstack([c,g]))
