liste = []

def calcul():
    a_min = 1
    b_min = 2
    c_min = 3
    d_min = 4
    resultat_min = (10*a_min+b_min-c_min)*d_min

    permutations([1,2,3,4])

    for data in liste:
        a = data[0]
        b = data[1]
        c = data[2]
        d = data[3]

        resultat = (10*a+b-c)*d
        if resultat < resultat_min:
            resultat_min = resultat
            a_min = a
            b_min = b
            c_min = c
            d_min = d

            print('(',a_min,b_min,'-',c_min,')',d_min,'=',resultat_min)

    return (a_min,b_min,c_min,d_min,resultat_min)

def permutations(start, end=[]):
    if len(start) == 0:
        liste.append(end)
    else:
        for i in range(len(start)):
            permutations(start[:i]+start[i+1:],end+start[i:i+1])

def fact(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f

def permutationsV2(start, end=[],res=[]):
    if len(start) == 0:
        res.append(end)
    else:
        for i in range(len(start)):
            permutationsV2(start[:i]+start[i+1:],end+start[i:i+1],res)
    if len(res)>0 and len(res)==fact(len(res[0])): #res contient le nbtotal de permutations
        return res



print(calcul())