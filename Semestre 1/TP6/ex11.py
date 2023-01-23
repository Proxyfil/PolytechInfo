def memesLettres(s1,s2):
    for i in s1:
        if(i not in s2):
            return False
    for i in s2:
        if(i not in s1):
            return False
    return True

print(memesLettres("bcd","caabddd"))