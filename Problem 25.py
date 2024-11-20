def max_elem(list1):
    cmp=len(list1[0])
    maximum=list1[0]
    for x in list1:
        if len(x)>cmp:
            maximum=x 
    print(maximum)

list1=list((input().split()))
max_elem(list1)