def createAnonDataFile(data,gos,gow,goc,goms):
    f=open("anonimizedData.txt","a+")
    
    for i in data:
        i['sex']=gos
        i['maritalStatus']=goms
        i['workclass']=gow
        i['country']=goc
        i['relationship']=' *'
        i['income']=' *'
        
    for i in data:
        for j in i.values():
            f.write(j)
        f.write("\n")
            
    f.close()