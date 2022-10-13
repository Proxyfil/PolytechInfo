def reduction(chaine):
    out = ""
    for c in chaine:
        if(ord(c) >= 97 and ord(c) <= 122):
            out += chr(ord(c))
        elif(ord(c) >= 65 and ord(c) <= 90):
            out += chr(ord(c) + 32)
    
    return out

def cesar(s,decalage):
    s = reduction(s)
    out = ""
    for c in s:
        out += chr(97+(ord(c)-97 + decalage)%26)
    return out

print(cesar("Bonjour",25))