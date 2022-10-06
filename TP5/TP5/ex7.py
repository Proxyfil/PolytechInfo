import random

def creer(n):
    return [random.randint(0,20) for i in range(n)]

def apparitions(x, lis):
    output = []
    for i in range(len(lis)):
        if(lis[i] == x):
            output.append(i)
    return output