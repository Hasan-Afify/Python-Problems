cnt=2
x=1
y=1
z=0
for x in range(1,10):
    print("\n")
    if x>5:
        z=x-cnt
        for s in range(1,z+1):
            print("* ",end=" ")
        cnt+=2
    else:
        for y in range(1,x+1):
            print("* ",end=" ")