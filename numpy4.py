#sum of numbers in an array
import numpy as np
a=np.array([1,3,5,7,9,11,13,15,17,19])
s=0
for i in range(len(a)):
    s+=a[i]
print("the sum of arrays in the numpy is:",s)

#maximum and minimum numbers in an array
m=a[0]
d=a[0]
for i in range(len(a)):
    if(a[i]>m):
        m=a[i]
    elif(a[i]<d):
        d=a[i]
print("the maximum number in the array is:",m)
print("the minimum number in the array is:",d)

