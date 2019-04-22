import collections

# Python code to remove duplicate elements 
def RemDup(lis): 
	final_list = [] 
	for i in lis: 
		if i not in final_list and i!=' ?': 
			final_list.append(i) 
	return final_list

#Hierarchical hash tables
HHTCountry={1 : {" North America" : [" United-States"," Puerto-Rico"," Canada",
" Outlying-US(Guam-USVI-etc)"," Cuba"," Honduras"," Jamaica"," Mexico"," Dominican-Republic"," Haiti",
" Guatemala"," Nicaragua"," El-Salvador"," Trinadad&Tobago"], 
" South America" : [" Ecuador"," Peru"," Columbia"], 
" Europe" : [" England"," Germany"," Greece"," Italy"," Poland"," Portugal"," Ireland", 
" France"," Hungary"," Scotland"," Yugoslavia"," Holand-Netherlands"],
" Asia" : [" India"," Japan"," South"," China"," Iran"," Philippines"," Vietnam",
" Laos", " Taiwan"," Thailand"," Hong"," Cambodia"]},
2 : {" *" : [" North America"," South America"," Asia"," Europe"]}}

HHTWorkclass={1 : {" Charity" : [" Without-pay"], " Unemployed" : [" Never-worked"], 
" Entrepreneur" : [" Private"," Self-emp-not-inc", " Self-emp-inc"],
" Central-gov" : [" Federal-gov"," State-gov"], " Territory-gov" : [" Local-gov"]},
2 : {" Non-gov" : [" Charity"," Unemployed"," Entrepreneur"],
    " gov" : [" Central-gov"," Territory-gov"]},
3 : {" *" : [" Non-gov"," gov"]}}

HHTMarital={1 : {" Married" : [" Married-civ-spouse"," Separated"," Married-spouse-absent"," Married-AF-spouse"],
" Unmarried" : [" Divorced"," Never-married"," Widowed"]},
2 : { " *" : [" Married"," Unmarried"]}}

HHTSex={1 : {" *" : [" Male"," Female"]}}

def generalizeCountry(data):
    Ulis=[]
    for i in data:
        if i["nativeCountry"] in Ulis:
            continue
        else:        
            Ulis.append(i["nativeCountry"])
    i=1
    while(len(Ulis)>1):
        for j in HHTCountry[i]:
            for k in Ulis:
                if k in HHTCountry[i][j]:
                    Ulis[Ulis.index(k)]=j
            Ulis=RemDup(Ulis)
        i=i+1
    gDataCoun=Ulis[0]
    return gDataCoun

def generalizeWorkclass(data):
    Ulis=[]
    for i in data:
        if i["workclass"] in Ulis:
            continue
        else:        
            Ulis.append(i["workclass"])
    i=1
    Ulis=RemDup(Ulis)
    while(len(Ulis)>1):
        for j in HHTWorkclass[i]:
            for k in Ulis:
                if k in HHTWorkclass[i][j]:
                    Ulis[Ulis.index(k)]=j
                    
            Ulis=RemDup(Ulis)
        i=i+1
    gDataWorkclass=Ulis[0]
    return gDataWorkclass

def generalizeMaritalStat(data):
    Ulis=[]
    for i in data:
        if i["maritalStatus"] in Ulis:
            continue
        else:        
            Ulis.append(i["maritalStatus"])
    i=1
    Ulis=RemDup(Ulis)
    while(len(Ulis)>1):
        for j in HHTMarital[i]:
            for k in Ulis:
                if k in HHTMarital[i][j]:
                    Ulis[Ulis.index(k)]=j
            Ulis=RemDup(Ulis)
        i=i+1
    gMaritalStat=Ulis[0]
    return gMaritalStat

def generalizeSex(data):
    Ulis=[]
    for i in data:
        if i["sex"] in Ulis:
            continue
        else:        
            Ulis.append(i["sex"])
    i=1
    Ulis=RemDup(Ulis)
    while(len(Ulis)>1):
        for j in HHTSex[i]:
            for k in Ulis:
                if k in HHTSex[i][j]:
                    Ulis[Ulis.index(k)]=j
            Ulis=RemDup(Ulis)
        i=i+1
    gDataSex=Ulis[0]
    return gDataSex