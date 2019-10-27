import random
import math
import matplotlib.pyplot as plt
import numpy as np
import copy
#group: Dillon Thompson, Cameron, Naeem, Ethyn Smith


#read in file function
def read():
    data = np.loadtxt('A.txt')
    return data.tolist()

#pick initial ctrs
def centers(data):
    ctr1 = []
    ctr2 = []
    ctr3 = []

    #pick from already existing data point
    #and makue sure they are not the same points
    ctr1 = random.choice(data)
    ctr2 = random.choice(data)
    ctr3 = random.choice(data)
    if ctr2 == ctr1 or ctr2 == ctr3:
        ctr2 = random.choice(data)
    if ctr3 == ctr1 or ctr3 == ctr2:
        ctr3 = random.choice(data)
    return [ctr1, ctr2, ctr3]

#put data into groups with respective ctrs
def grouping(data, ctrs):
    cntr1 = ctrs[0]
    cntr2 = ctrs[1]
    cntr3 = ctrs[2]
    g1 = []
    g2 = []
    g3 = []

    #get distances
    for pt in data:
        #distance formual
        d1 = np.sqrt((cntr1[0] - pt[0])**2 + (cntr1[1] - pt[1])**2)
        d2 = np.sqrt((cntr2[0] - pt[0])**2 + (cntr2[1] - pt[1])**2)
        d3 = np.sqrt((cntr3[0] - pt[0])**2 + (cntr3[1] - pt[1])**2)
        #min of distacnces
        closest = min(d1, d2, d3)
        #group by closest one to respective center
        if closest == d1:
            g1.append(pt)
        if closest == d2:
            g2.append(pt)
        if closest == d3:
            g3.append(pt)
    return [g1, g2, g3]

#function for picking new centers
def newctrs(grps):
    #the new ctrs to be returned
    newctrs = []
    #these will store the points of the new ctrs
    x = 0
    y = 0

    #go through groups and get the average of all the points
    for grp in grps:
        for pt in grp:
            x += pt[0]
            y += pt[1]
        y = y / len(grp)
        x = x / len(grp)

        #add the new points to the ctrs list
        newctrs.append([x, y])
    return newctrs

#plot function from group mate
def plot(groups, centers):
    # colors for groups
    colors = ["red", "blue", "green"]
    x = 0

    for group in groups:
        for point in group:
            plt.scatter(point[0], point[1], c=colors[x])
        x += 1

    # plot centers in black
    for cent in centers:
        plt.scatter(cent[0], cent[1], c="black")

    plt.show()

#actual k-means algorithm.
def kmeans():
    data = read()
    ctrs = centers(data)
    grps = grouping(data, ctrs)

    prvctrs = [-1, -1, -1]
    #move centers while they're not equal to the previous ones
    while ctrs != prvctrs:
        prvctrs = copy.copy(ctrs)
        ctrs = newctrs(grps)
        grps = grouping(data, ctrs)
    plot(grps, ctrs)

if __name__ == "__main__":
    kmeans()
