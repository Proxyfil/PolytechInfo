def sommeChiffres(s):
    output = 0
    for i in s:
        output += int(i)

    return output

print(sommeChiffres("123456789"))