def trad(chaine):
    out = []
    for c in chaine:
        out.append(ord(c))
    return out

def correspondance(chaine):
    for c in chaine:
        print([c, ord(c)])

print(correspondance("bonjour"))