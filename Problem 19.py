n=0
sum=0
n=int(input("Please Enter A Number \n"))
while n!=0:
    sum+=n%10
    n//=10
print(sum)