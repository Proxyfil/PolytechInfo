ls = [1, 2, 3]
ks = ls[:]
ks[0], ks[1] = ks[1], ks[0]
print(ls)
print("Identifiant de ls :",id(ls))
print("Identifiant de ks :",id(ks))