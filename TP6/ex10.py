def listeMots(s):
    for i in [",",".",";","!","?"]:
        s = s.replace(i,"")
    return s.split(" ")

def nbMots(s):
    return len(listeMots(s))

def motsLesPlusLongs(s):
    maxi = 0
    lsMaxi = []
    for i in listeMots(s):
        if(len(i) > maxi):
            maxi = len(i)

    for i in listeMots(s):
        if(len(i) == maxi):
            lsMaxi.append(i)

    return lsMaxi

print(motsLesPlusLongs("Ceci est une phrase à tester."))