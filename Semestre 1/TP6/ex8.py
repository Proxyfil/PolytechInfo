def addresse(prenom,nom):
    return prenom.lower()+"."+nom.lower()+"@etu.univ-tours.fr"

def prenom_nom(s):
    s = s.replace("@etu.univ-tours.fr","")
    if(s.find(".") == -1):
        return None
    s = s.split(".")
    return s[0].capitalize()+" "+s[1].capitalize()

print(prenom_nom("jean.dupont@etu.univ-tours.fr"))