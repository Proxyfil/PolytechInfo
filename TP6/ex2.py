def parcourir(s):
    print(len(s))
    for i in range(len(s)):
        print("Caractère n°",i," : ",s[i],"code ASCII :",ord(s[i]))

def grec():
    for i in range(945,970):
        print(chr(i),end=" ")
    for i in range(913,938):
        print(chr(i),end=" ")

grec()