
print("Father : Rahul(son) we need to visit nearby atm, because cash ended!")
print("Rahul : Ok dad, I know an ATM nearby.\n")

print("Father : Hey Rahul came here i not know how to do like may be machine has different system !")
print("Rahul : Ok dad give me card let i handle these !\n")

print("Machine : Enter your card here !")

real_password = 5174
restart = "yes"

while restart == "yes":

    attempts = 0

    while attempts < 3:
        password = int(input("Machine : Enter your password : "))

        if password != real_password:
            attempts = attempts + 1
            print("Machine : Wrong password, try again!")
        else:
            attempts = attempts + 3
            print("Machine : Wait few seconds for your amount!")

    restart = input("Machine : Do you want to start again? (yes/no): ").lower()

print("Machine : Thank you. Goodbye!")


""""
Output:
/opt/homebrew/bin/python3.14 /Users/jillravaliya/Documents/Python/practice.py 
Father : Rahul(son) we need to visit nearby atm, because cash ended!
Rahul : Ok dad, I know an ATM nearby.

Father : Hey Rahul came here i not know how to do like may be machine has different system !
Rahul : Ok dad give me card let i handle these !

Machine : Enter your card here !
Machine : Enter your password : 1234
Machine : Wrong password, try again!
Machine : Enter your password : 4321
Machine : Wrong password, try again!
Machine : Enter your password : 1122
Machine : Wrong password, try again!
Machine : Do you want to start again? (yes/no): yes
Machine : Enter your password : 5174
Machine : Wait few seconds for your amount!
Machine : Do you want to start again? (yes/no): no
Machine : Thank you. Goodbye!

Process finished with exit code 0

"""

