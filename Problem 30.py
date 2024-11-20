def clal_total_price(list1):
    sum=0
    for x in list1:
        sum+=x
    sum+=(sum*(14/100))
    print(sum)    

list1=list(map(int,input().split()))
clal_total_price(list1)    