
def base(a,n,tailleMax):
    out = ""
    for i in range(a,n):
        if(i != a):
            out += "\n"
        if((2*i)/6 == 0):
            out += "_"*(n-i-1+(n-tailleMax))+"X"*(1+2*i)+"_"*(n-i-1+(n-tailleMax))
        else:
            out += "_"*(n-i-1+(n-tailleMax))+"X"*(1+2*i)+"_"*(n-i-1+(n-tailleMax))
    return out

def sapin(b,a,n):
    for i in range(0,b-1):
        print(base(a+i,n+i,n+i-n+i+1))
    print(base(a+b-1,n+b-1,n+b-1))
    for i in range(0,b):
        print("_"*((n+b//2)-1)+"I"*b+"_"*((n+b//2)-2))

print(sapin(4,0,4))