def div(C):
    numOfUniqueValues = 0

    uniqueValuesHT = {}
    for person in C:
        country = person['nativeCountry']
        if(country not in uniqueValuesHT):
            uniqueValuesHT.update({country:1})

    return uniqueValuesHT.__len__()

    # in the article this parameter called 'm' (numOfCountries)
    numOfCountries = uniqueValuesHT.__len__()



# check if the parameter l is bigger than the diversity in the DB
def diversityInputIsLegal(D, l):
    if (div(D) < l):
        print('Input diversity parameter is illegal')
        return #f
    else:
        return #t


def getMinDiversityFromGroupOfClusters(C):
    # getting the lowest diversity among all clusters
    # todo: do it using reduce function
    minDiversity = div(C[1])

    for i in range(2,C.__len__()):
        cDiversity = div(C[i])
        if (minDiversity > cDiversity):
            minDiversity = cDiversity

    return minDiversity
