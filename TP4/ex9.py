def multiplicationBinaire():
    a = input("Entrez un nombre binaire: ")
    b = input("Entrez un nombre binaire: ")
    a = int(a, 2)
    b = int(b, 2)
    c = a * b
    c = bin(c)
    print(c[:2])

multiplicationBinaire()