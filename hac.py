import matplotlib.pyplot as plt
import numpy as np
import copy
#group: Dillon Thompson, Cameron Jewell, Naeem Ghossein, Ethyn Smith

#read in file function
def read():
    data = np.loadtxt('B.txt')
    data = data.tolist()
    label = 1
    for i in range(len(data)):
        data[i].append(label)
        label += 1
    return data

#group data
def groups(data):
    grps = []
    for pt in data:
        if pt[2] not in grps:
            grps.append(pt[2])
    return grps

#cluster data points
def cluster(data):
    minimum = 9999999999
    #loop through and get the distance
    #between each point
    for i in data:
        for j in data:
            if i[2] != j[2]:
                dist = np.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2)
                if dist < minimum:
                    pt1 = i
                    pt2 = j
                    minimum = dist
    #update vlaues to actually cluster the closest points
    updatevalues(data, pt1[2], pt2[2])
    
#function for updating all the values  
def updatevalues(data, pt1, pt2):
    for pt in data:
        if pt[2] == pt1:
            pt[2] = pt2

def countClusters(data):
    grps = []
    count = 0
    for pt in data:
        if pt[2] not in grps:
            grps.append(pt[2])
            count += 1
    return count

#plot function from group mate
def plot(data):
    group = groups(data)

    for point in data:
        if point[2] == group[0]:
            plt.scatter(point[0], point[1], c="red")
        elif point[2] == group[1]:
            plt.scatter(point[0], point[1], c="blue")

    plt.show()
#actual hac algorithm
def hac():
    data = read()
    while countClusters(data) > 2:
        cluster(data)
    plot(data)

if __name__ == "__main__":
    hac()
    # read()
