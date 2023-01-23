def saisirMatrice(m, n):
    #On saisit une matrice de m ligne et de n colonnes.
    A=[]
    for i in range(m):
        print("Saisie des éléments de la ligne ", i+1)
        l=[]
        for j in range(n):
            v=eval(input("Saisir l'élément de la colonne"+str(j+1)+" : "))
            l.append(v)
        A.append(l)
    return A

def maxLongueur(A):
    #On renvoie le maximum des longueurs des termes de la matrice A.
    max=0
    m=len(A)
    for i in range(m):
        n=len(A[i])
        for j in range(n):
            longueur=len(str(A[i][j]))
            if longueur>max:
                max=longueur
    return max

def afficherMatrice(A):
    #On affiche une matrice rectangulaire A.
    max=maxLongueur(A)
    ch="{:"+str(max+3)+".2f}"
    m=len(A)
    for i in range(m):
        n=len(A[i])
        for j in range(n):
            print(ch.format(A[i][j]),end=" ")
        print()

def constante(m, n, k):
    output = []
    for i in range(m):
        output.append([k for j in range(n)])
    return output

def suite(m,n):
    low = 0
    output = []
    for i in range(m):
        output.append([j for j in range(low*n, (low+1)*n)])
        low += 1
    return output

def identite(m):
    output = [[0 for i in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            if(i == j):
                output[i][j] = 1
                print(i,j)
    return output

def estRectangulaire(A):
    default = len(A)
    for i in A:
        if(len(i) != default):
            return False
    return True

def rechercher(A,x):
    for i in len(A):
        for j in len(A[i]):
            if(A[i][j]==x):
                return (i,j)
    return (1,-1)

def transposee(A):
    output = []
    for i in range(len(A[0])):
        output.append([A[j][i] for j in range(len(A))])
    return output

def somme(A,B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] += B[i][j]
    return A

def produitScalaire(A,k):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= k
    return A

def produit(A,B):
    output = []
    for i in range(len(A)):
        output.append([])
        for j in range(len(B[0])):
            output[i].append(0)
            for k in range(len(B)):
                output[i][j] += A[i][k]*B[k][j]
    return output

print(produit([[1,2],[3,4],[5,6]],[[2,3,4],[5,6,7]]))
