def moyenne(l):
    total = 0
    for i in l:
        if(i == 'ABI'):
            return "défaillant"
        elif(i == 'ABJ'):
            total += 0
        else:
            total += int(i)
    return total/len(l)

def moyennesEtudiants(d):
    tuples = []
    for i in list(d.keys()):
        moy = moyenne(d[i])
        if(moy != "défaillant"):
            tuples.append((i, round(moy, 2)))
        else:
            tuples.append((i, moy))
    return tuples

print(moyennesEtudiants({"Barthet" : [14, 7, 12], "Chapuis": [18, 16, 17], "Rey" :
["ABJ", 15, 13], "Varlet":[12, 8, "ABI"], "Frémont":[6, 14, 11]}))