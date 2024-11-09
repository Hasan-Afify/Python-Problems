str=input("Enter A Name \n")
y=len(str)-1
revstr=[""]
for i in range(y,-1,-1):
    revstr[0]+=str[i]
print(revstr[0])