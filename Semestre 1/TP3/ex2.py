def termeSuite1(m,n):
    u = m
    for i in range(1,n+1):
        u = u**2-5
    return u

def sommeTermes(n,x):
    u = x
    res = x
    for i in range(0,n):
        u = 3/u
        res += u
    return res
    

print(termeSuite1(4,3))