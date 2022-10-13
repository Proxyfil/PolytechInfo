import random

def genere():
    choices = [":","-","(",")"]
    output = ""

    for i in range(10):
        output += random.choice(choices)

    return output

def joue():
    data = genere()
    if(":-)" in data):
        print("Gagné")
    else:
        print("Perdu")

joue()

