#On teste les erreurs générées en saisissant 5.0 pour n

n=input("entrer n: ")
#n=int(input("entrer n: "))
f=1
for i in range(n):
    f=f*i
print(n,"!=",f,sep='')