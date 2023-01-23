def suite(u0,n,r):
    for i in range(n):
        u0 = u0+r

    return u0

def suite2(u0,n,q):
    for i in range(n):
        u0 = u0*q

    return u0

print(suite(-1,3,2))