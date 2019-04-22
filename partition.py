import math

import numpy
import numpy as np


def algorithm(D, t):

    racesAppearancesHT = {}
    for person in D:
        for key,value in person.items():
            if key == 'race':
                if value not in racesAppearancesHT:
                    racesAppearancesHT.update({value:1})
                else:
                    newValue = racesAppearancesHT[value] + 1
                    racesAppearancesHT.update({value: newValue})

    numOfRaces = racesAppearancesHT.__len__()

    racesAppearancesLST = []
    racesAppearancesLST.append(['keepingPlace', 0]) #counting in the atricle start in 1
    for raceName, raceAppearances in racesAppearancesHT.items():
        racesAppearancesLST.append([raceName, raceAppearances])


    Y = numpy.zeros((t+1, numOfRaces + 1))
    for i in range(1, t + 1):
        for j in range(1,numOfRaces + 1):
            modulo = racesAppearancesLST[j][1]%t
            if(i <= modulo):
                Y[i, j] = math.ceil(racesAppearancesLST[j][1]/t)
            else:
                Y[i, j] = math.trunc(racesAppearancesLST[j][1]/t)



    permutations = numpy.zeros((numOfRaces+1, t+1))

    for j in range(1,numOfRaces + 1):
        lst = [0]
        permutation = np.random.permutation(t)
        permutation += 1
        lst.extend(permutation)
        permutations[j] = lst


    #print(numOfraces)
    X = numpy.zeros((t+1, numOfRaces + 1))
    for i in range(1, t + 1):
        for j in range(1, numOfRaces + 1):
            X[i][j] = Y[int(permutations[j][i])][j]
    #print(sum(X[1]))

    racesArray = []
    racesArray.append("keepingPlace")
    for j in range(1,numOfRaces + 1):
        peopleFromThisRace = []
        for person in D:
            if(person.get('race') == racesAppearancesLST[j][0] ):
                peopleFromThisRace.append(person)

        racesArray.append(peopleFromThisRace)

    clusters =[]
    clusters.append("keepingPlace")
    for i in range(1,t+1):
        cluster = []
        for j in range(1,numOfRaces + 1):
            numOfPeopleInThisCluster = X[i][j]
            for k in range(int(numOfPeopleInThisCluster)):
                peopleToAdd = racesArray[j].pop()
                cluster.append(peopleToAdd)
                
        clusters.append(cluster)
    
    
    
    #tot_rec = 0
    for i in range(1,len(clusters)):
    #    tot_rec = tot_rec + len(clusters[i])
    #   print(len(clusters[i]))
    llis=[]
    
    for i in range(1,t):
        c=0
        for j in X[i]:
            if(j==0):
                c=c+1
        llis.append(c)
    print("l = ",6-max(llis))
    #print(X[1])
    #print(X[50])
    #print(X[100])
    #print(X[500])

    return clusters