'''
1 for snake
-1 for water
0 for gun

'''


import random
computer=random.choice([-1,0,1])
choices = input("enter first letter of your choice : ")
if(choices=="w"or choices=="s"or choices=="g"):
    Dict = {"w":-1,"s":1,"g":0}
    reverseDict = {-1:"water",1:"snake",0:"gun"}
    you=Dict[choices]

    print(f"you chose :{reverseDict[you]}")
    print(f"computer chose : {reverseDict[computer]}")

    if(computer == you):
        print("it's a draw")
    else:
        if(computer==-1 and you==1):
            print("you win !")
        elif(computer==1 and you==-1):
            print("comuter win !")
        elif(computer==1 and you==0):
            print("you win !")
        elif(computer==-1 and you==0):
            print("computer win !")
        elif(computer==0 and you==1):
            print("computer win !")
        elif(computer==0 and you==-1):
            print("you win !")
        else:
            print("something went wrong !")
else:
    print("enter correct choice !")