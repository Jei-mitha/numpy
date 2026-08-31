import numpy as np

l = [1,2,3,4,5,5,4,7,6,2,1,4]
x = np.array(l, dtype=int)

visited = np.array([], dtype=int) #set()
for i in range(len(x)):
    if x[i] not in visited:
        c = 0
        for j in range(len(x)):
            if x[i] == x[j]:
                c += 1
        print("The frequency of", x[i], "is:", c)
        visited = np.append(visited, x[i])#.add(x[i])
