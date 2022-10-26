import math

def binome(n, p):
    if p == n:
        return 1
    elif p == 0:
        return 1
    elif 0<=p<=n:
        return binome(n-1, p-1) + binome(n-1, p)

print(binome(5, 2))
print(math.factorial(5)/(math.factorial(2)*math.factorial(5-2)))