def valid_email(list1):
    bool1=0
    for x in list1:  
        if '@' in x and 'gmail.com' in x :
            bool1=1
    if bool1:
        print("Valid Email")
    else:    
        print("Invalid Email") 
list1=list((input().split()))
valid_email(list1)