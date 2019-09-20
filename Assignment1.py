#Dillon Thompson 25 queen solver
#Group: Dillon Thompson, Cameron Jewell, Ethan Smyth, Naeem Ghossein
import random
import copy
#this will hold te state of the board
state = []

#this function gets the score
#my score function is based on the idea that
#every conflicting queen increments the score.
def getScore(n, state):
    score = 0
    #going through the current state
    for i in range(n):
        for j in range(n):
            #this gets any conflicts between queens in diagonal of each other.
            getDiag = abs(state[i] - state[j])
            if i != j:
                if getDiag == abs(i - j) or state[i] == state[j]:
                    score += 1
    return int(score/2)

    #this is my function for getting the neighbors for the current queen.
    #the neighbors of a queen are considered to be the indexes of the column she is in.
def getNeighbors(n, q):
    #declare array to hold queens neighbors
    neighbors = []
    #iterate through the current state
    for i in range(1,n + 1):
        #as long as it's not the same index as the current queen, add it to neighbors
        if i != q:
            neighbors.append(i)
    return neighbors

#this method solves the board using the random hillclimbing method
#everytime it gets stuck, it starts over at a random point and tries again.
def solver(n):
    state = []
    #building the board
    i = 1
    while i <= n:
        state.append(i)
        i += 1
    #get the score of the initial state
    score = getScore(n, state)
    #loop through until the score is 0
    while score != 0:
        #start my hillclimber at 0
        j = 0
        #begin looping through the queens
        while j < n:
            #check the current queens neighbors for a state
            #with a better score and move there if one exists
            for k in getNeighbors(n, state[j]):
                #copy of the current state
                tempState = copy.copy(state)
                #set the copy to a new state
                tempState[j] = k
                #get the score of the new state
                tempScore = getScore(n, tempState)
                #change the state and score to it if
                #it has a lower score
                if tempScore <= score:
                    state = tempState
                    score = tempScore
            #reset j to a random point
            j = random.randint(0, n)
    #print the results and the score
    print(state, score)

solver(25)
