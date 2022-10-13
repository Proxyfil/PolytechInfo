from math import log, log10

def test_pH():
    concentration = float(input("Entrez la concentration des ions : "))
    if concentration < 10**-14 or concentration > 10**-1:
        print("Concentration invalide")
    else:
        pH = -log10(concentration)
        print("pH = ", format(pH, ".2f"))
        if(pH < 6.5):
            print("Acide")
        elif(pH > 7.5):
            print("Base")
        else:
            print("Neutre")

test_pH()
