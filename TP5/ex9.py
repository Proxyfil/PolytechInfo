from random import randint
ls = [randint(-10, 10) for i in range(20)]

def sortList(ls):
    for i in ls:
        if len(ls) > 0:
            for i in range(len(ls)):
                for j in range(len(ls)-1):
                    if ls[j] > ls[j+1]:
                        ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls