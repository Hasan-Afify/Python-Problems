def min_and_max(list1):
    minimum=min(list1)
    maximun=max(list1)
    print("Max Value= "+str(maximun)+" Min Value= "+str(minimum))    

list1=list(map(int,input().split()))
min_and_max(list1)    