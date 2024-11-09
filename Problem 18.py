username="Hasan"
Password=123456
user=input("Please Enter Your UserName \n")
Pass=int(input("Please Enter Your PassWord \n"))
while username==user and Password==Pass:
    print("Successfull Login")
    break
else:
    print("Invalid Username Or Password")