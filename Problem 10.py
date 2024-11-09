sum=0
cnt=0
Num=int(input("Please Enter The Number That You Want To Calculate Its Sum And Its Average \n"))
while Num != 0:
    sum+=Num
    cnt+=1
    Num=int(input(""))
Avg=sum/cnt
print("Sum = "+str(sum)+" Average = "+str(Avg))