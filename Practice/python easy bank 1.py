#Ben p
#EZBank1
import basics

app = basics.newProgram()

user = basics.newUser()

app.currentBalance = 1000

while app.running == True:
    print(app.currentBalance)
    user.choice = input("1,2, or 3")
    if user.choice == ("1"):
        user.deposit = input("How much are you depositing?")
        user.deposit = int(user.deposit)
        app.currentBalance += user.deposit
    elif user.choice == ("2"):
        user.withdraw = input("how much would you like to withdraw?")
        user.withdraw = int(user.withdraw)
        if user.withdraw > app.currentBalance:
            print("You do not have enough money!")
        else:
                app.currentBalance -= user.withdraw
    elif user.choice == ("3"):
        app.running = False
    else:
        print("Your choice was invalid.")
