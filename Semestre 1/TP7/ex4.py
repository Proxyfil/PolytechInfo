def memesLettres(s1,s2):
    return set(s1) == set(s2)

print(memesLettres("abdccd","caabddd"))
print(memesLettres("bcd","caabddd"))