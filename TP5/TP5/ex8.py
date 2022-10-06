def premierNb(lis):
    for i in range(len(lis)):
        if(isNb(lis[i])):
            return lis[i]

def isNb(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def listToNumberList(lis):
    output = []
    for i in range(len(lis)):
        if(isNb(lis[i])):
            output.append(int(lis[i]))
    output.sort()
    return output

def mini(lis):
    return listToNumberList(lis)[0]

def maxi(lis):
    return listToNumberList(lis)[-1]

def summ(lis):
    output = 0
    for i in range(len(lis)):
        if(isNb(lis[i])):
            output += int(lis[i])
    return output

print(premierNb(["abs", "pas là",12,"abj",9.5,"absent",17]))