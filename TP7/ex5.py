def estPresent(stock):
    fruit = input("Nom du fruit : ")
    if(fruit in stock):
        print(fruit)
    else:
        return "Le fruit n'est pas en stock"

def setStock(stock):
    fruit = input("Nom du fruit : ")
    amount = int(input("Quantité : "))
    if(fruit in stock):
        stock[fruit] += amount
    else:
        stock[fruit] = amount
    return stock

def delStock(stock):
    fruit = input("Nom du fruit : ")
    if(fruit in stock):
        del stock[fruit]
    else:
        print("Le fruit n'est pas en stock")
    return stock
