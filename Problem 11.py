f0=0
f1=1
print(str(f0) + " " + str(f1),end=" ")
for x in range(2,13):
    x=f0+f1
    print(x,end=" ")
    f0=f1
    f1=x