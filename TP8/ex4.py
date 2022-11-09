def resultat(s):
    output = s.split(":")[1].replace("\n","").replace(" ","")
    return output.lower()

def repartir(source, admis, ajournes, defaillants):
    deffile = open(defaillants, 'w', encoding='utf-8')
    ajofile = open(ajournes, 'w', encoding="utf-8")
    adfile = open(admis, 'w', encoding="utf-8")

    with open(source, 'r', encoding="utf8") as f:
        for line in f:
            print(line)
            if resultat(line) in ["défaillant","defaillant"]:
                deffile.write(line)
            elif float(resultat(line)) < 10:
                ajofile.write(line)
            else:
                adfile.write(line)

repartir("notes.txt", "admis.txt", "ajournes.txt", "defaillants.txt")