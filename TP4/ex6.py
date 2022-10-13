import math

def main():
    n = int(input("Saisir un entier naturel : "))
    x = int(input("Saisir un entier positif : ")) 
    us = x
    vs = 1
    ux = us
    vx = vs
    print("U0 : ", ux, "V0 : ", vx)
    for i in range(0,n):
        ux = (us+vs)/2
        vx = (2*us*vs)/(us+vs)
        us = ux
        vs = vx

        print("Ux : ", ux, "Vx : ", vx)
    print("Root(x) : ", math.sqrt(x))



    
main()
