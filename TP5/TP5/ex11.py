def valeursCommunes(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return list(set(output))

print(valeursCommunes([1,8,78,14,2],[8,2,54,78,1,0]))