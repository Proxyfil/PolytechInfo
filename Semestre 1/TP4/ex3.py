def factoriel(n):
    f = 1
    for i in range(2, n+1):
        f = f*i
    return f

def binome(p,n):
    return int(factoriel(n)/(factoriel(p)*factoriel(n-p)))

def main():
    p = -1
    n = int(input("Saisir un entier positif : "))
    while p < 0 or p > n:
        p = int(input("Saisir un entier positif entre 0 et "+str(n)+" : "))
    print("Le coefficient binomial est : ", binome(p,n))

def dev(n):
    texte = "(a+b)^"+str(n)+" = "
    for i in range(0,n):
        texte = texte + str(binome(i,n))+"a^"+str(n-i)+"b^"+str(i)+" + "
    texte = texte[:-3]
    print(texte)

def afficher(n):
    for i in range(0,n+1):
        texte = ""
        for j in range(0,i+1):
            texte += str(binome(j,i)) + " "
        print(texte)


afficher(4)
