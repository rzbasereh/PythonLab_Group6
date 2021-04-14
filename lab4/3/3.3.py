import numpy as np
entry = np.array([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])
y,x = entry.shape
#make a distance matrix that any value showes cummulative distance for that element
#we have seted a big value for (1)elements , so when we want to find minimom distance we can ignore it
dist_all = np.ones((y,x))*x*y*2
for i in range(y):
    for j in range(x):

        #if it is 0 , so go and calculate the distance from 1
        if entry[i,j]==0:
            dist = 0
            for k in range(y):
                for h in range(x):
                    if entry[k,h]==1:
                        # sum all the distances from any (1) element
                        dist += abs(k-i) + abs(h-j)
            #put all the distances for any element in a matrix
            dist_all[i,j] = dist

#find the minimum distance
print(np.where(dist_all==np.min(dist_all)))





