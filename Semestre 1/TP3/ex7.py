def verification_base(nombre, base):
    """Fonction qui vérifie si un nombre est bien dans la base donnée"""
    nombre = str(nombre)
    for chiffre in nombre:
        if(int(chiffre) >= base):
            return False
    return True

def str_to_int(nombre, base):
    """Fonction qui transforme un nombre de base b en base 10"""
    nombre = list(str(nombre))
    res = 0
    for i in range(0, len(nombre)):
        res += int(nombre.pop()) * base ** i
    return res

def int_to_str(nombre, base):
    """Fonction qui transforme un nombre de base 10 en base b"""
    res = ""
    while nombre > 0:
        res = str(nombre % base) + res
        nombre = nombre // base
    return res

def conversion(nombre, base1, base2):
    """Fonction qui convertit un nombre de base b1 en base b2"""
    if verification_base(nombre, base1):
        return int_to_str(str_to_int(nombre, base1), base2)
    else:
        return "Erreur: le nombre n'est pas dans la base donnée"


print(conversion(6, 10, 2))
print(conversion(11110, 2, 10))
print(conversion(11110, 2, 8))