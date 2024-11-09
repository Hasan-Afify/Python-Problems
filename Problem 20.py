str=input("Enter A Word \n")
y=len(str)-1
revstr=[""]
for i in range(y,-1,-1):
    revstr[0]+=str[i]
if revstr[0]==str:
    print("The Word Is Palindorme")
else:
    print("The Word Is Not a Palindorme")