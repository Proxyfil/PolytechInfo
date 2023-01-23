from audioop import add


def additionBinaire():
    a = input("Entrez le premier nombre binaire : ")
    b = input("Entrez le deuxième nombre binaire : ")
    a = int(a, 2)
    b = int(b, 2)
    c = a + b
    c = bin(c)
    print("Le résultat est : ", c[2:])

additionBinaire()