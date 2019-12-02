import sarsa
import expectedsarsa
import qlearning
import numpy as np
import random as randy
import copy as cp
import matplotlib.pyplot as plt

#running 20 times
runs = 20
#arrays for sarsa information
sarsas = {}
sarsaAvg = []
sarsaVar = []
#arrays for expected sarsa information
Esarsas = {}
EsarsaAvg = []
EsarsaVar = []
#arrays for q-learning information
qls = {}
qlsAvg = []
qlsVar = []

#put all steps into a dictionary
for i in range(runs):
    index = 0
    for j in sarsa.run():
        index += 1
        if sarsas.__contains__(index):
            sarsas.get(index).append(j)
        else:
            sarsas[index] = [j]
    for j in expectedsarsa.run():
        index += 1
        if Esarsas.__contains__(index):
            Esarsas.get(index).append(j)
        else:
            Esarsas[index] = [j]
    for j in qlearning.run():
        index += 1
        if qls.__contains__(index):
            qls.get(index).append(j)
        else:
            qls[index] = [j]
    print('Run ', i + 1, ' is complete')
# print(sarsas)
# print(Esarsas)
# print(qls)

for episode in sarsas:
    sarsaAvg.append(np.average(sarsas[episode]))
    sarsaVar.append(np.var(sarsas[episode]))
for episode in Esarsas:
    EsarsaAvg.append(np.average(Esarsas[episode]))
    EsarsaVar.append(np.var(Esarsas[episode]))
for episode in qls:
    qlsAvg.append(np.average(qls[episode]))
    qlsVar.append(np.var(qls[episode]))

x_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fig, (mean, var) = plt.subplots(2, 1, sharex=True)
mean.plot(x_axis, sarsaAvg, c='orange', label='sarsa')
mean.plot(x_axis, EsarsaAvg, c='blue', label='Esarsa')
mean.plot(x_axis, qlsAvg, c='black', label='Qlearning')
mean.set_title('Mean')

var.plot(x_axis, sarsaVar, c='orange', label='sarsa')
var.plot(x_axis, EsarsaVar, c='blue', label='Esarsa')
var.plot(x_axis, qlsVar, c='black', label='Qlearning')
var.set_title('Variance')

plt.legend(loc='upper right')
plt.show()
