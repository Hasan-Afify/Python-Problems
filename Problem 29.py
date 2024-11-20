def upper(list1):
    string=""
    for i in range(len(list1)):             
            string="".join(list1[i])
            string=string.upper()
            list1[i]=list(string)   
    print(list1)

list1=list((input().split()))
upper(list1)