def apparitions(s1,s2):
    output = []
    for i in range(len(s1)):
        if(s2 == s1[i:i+len(s2)]):
            output.append(i)

    return output

def soulignement(s1,s2):
    data = apparitions(s1,s2)
    output = list(" "*len(s1))
    last = 0

    for i in data:
        for j in range(i,i+len(s2)):
            output[j] = "-"

    print(s1)
    print("".join(output))
    return True


soulignement("Le mot texte apparaït deux fois dans ce texte.","texte")
