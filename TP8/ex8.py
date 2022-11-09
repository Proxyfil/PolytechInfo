import csv

def point1():
    x=[["Martha",16],["Martin",15],["Martine",18]]
    with open('notes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(x)

def point2():
    import csv
    with open('notes.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def creerCsv(source):
    with open(source, 'r', encoding="utf-8") as f:
        with open('alu.csv', 'w', newline='', encoding="utf-8") as g:
            writer = csv.writer(g)
            for line in f:
                writer.writerow(line.split())

def creeDictionnaire(source):
    d={}
    with open(source, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            d[row[0]]=row[1]
    return d

def productionTotale(d):
    somme=0
    for key in d:
        somme+=int(d[key])
    return somme

def plusGrandProducteur(d):
    max=0
    for key in d:
        if int(d[key])>max:
            max=int(d[key])
            nom=key
    return nom
