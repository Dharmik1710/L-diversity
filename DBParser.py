def makeListOfDictionaries():
    data = []
    f=open("adult.data", "r")
    if f.mode == 'r':
        arrayOfStrings = f.readlines()
        for line in arrayOfStrings:
            v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15 = line.split(',')
            Person = {'age': v1,
                      'workclass': v2,
                      'fnlwgt': v3,
                      'education': v4,
                      'educationNum': v5,
                      'maritalStatus': v6,
                      'occupation': v7,
                      'relationship': v8,
                      'race': v9,
                      'sex': v10,
                      'capitalGain': v11,
                      'capitalLoss': v12,
                      'hoursPerWeek': v13,
                      'nativeCountry': v14,
                      'salaryPerYear': v15,}
            data.append(Person)
    f.close()
    return data