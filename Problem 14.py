list = [1,2,3,4,5,6,7,8,9,10]                  
for x in list:
    bool = 1  
    if x==1:
        continue
    for y in range(2,x):
        if x%y == 0:
            bool=0
        y+=1    
    if bool == 1:
        print(x)