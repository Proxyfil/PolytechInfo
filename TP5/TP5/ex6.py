def modifier(li) :
    for x in range(len(li)) :
        if li[x]%2 == 0 :
            li[x] = li[x] // 2
    return li

def tousImpairs(li) :
    for x in li :
        if x%2 == 0 :
            return False
    return True
