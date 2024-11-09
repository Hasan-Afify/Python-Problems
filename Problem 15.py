Balance=5000
withdraw=int(input("Please Enter The Value That You Want To Withdraw \n"))
if Balance >= withdraw:
    Balance-=withdraw
    print("You Have Successfully Withdraw " + str(withdraw) + "\n" + "Your Balance Now = " + str(Balance))
else:
    print("Your Balance Is less Than The Withdrawal Amount!")