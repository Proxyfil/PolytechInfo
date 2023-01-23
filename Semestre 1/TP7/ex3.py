def listeSansDoublons(l):
    d = {}
    return sorted(list(set(l)))

def valeurCommunes(l1,l2):
    l1 = listeSansDoublons(l1)
    l2 = listeSansDoublons(l2)
    return [i for i in l1 if i in l2]
    

print(valeurCommunes([1,5,7,7,9,3,12,75,1,54,8],[1,12,54,22,879,3478,43,879,1]))