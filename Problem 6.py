series=(1,2,3,4,5,6,7,8,9,10)
cnt1=0
cnt2=0
for x in series:
    if x%2==0:
        cnt1+=1
    else:
        cnt2+=1    
print("The Count Of Even Numbers = " + str(cnt1))
print("The Count Of Odd Numbers = " + str(cnt2))