import random
bool = 0
x=random.randint(1,9)
while bool != 1:
    y=int(input("Guess A Number Between 1 And 9 \n"))
    if x == y:
        print ("Congratultions Your Guess Is True!")
        bool = 1   
    else:
        print ("Try Again")