def comptage(s,suite):
    suite = list(suite)
    output = 0

    for i in s:
        if i in suite:
            output += 1
    
    return output

print(comptage("Hervé et Irène se sont même rencontrés à Noël","eéèëê"))