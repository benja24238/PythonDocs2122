#Ben
#Practice using expression and conditional statements

#An expression is a problem that must be solved
# 5 + 5 is an "arithmetic" expression
x = 5 + 5

#Functions/methods must be resolved as expressions as well
answer = input("What is your name?")

#Comparison expressions resolve as True/False
print( x==10 )
print( 7 > 7 )
print( 7>= 7)

#A conditional statements runs if its condition is True / not False
if answer == "Bob":
    print("Hello, Bob! Welcome back!")
    print("This line also prints if your name is Bob")
elif answer == "Vadim":
    print("Hey! You still owe me money!")
else:
    print("Sorry, I only talk to Bobs")
print("This line isn't inside of the if statement, and prints regardless")

# ^ If checks a condition
# ^ Elif checks a condition if the previous conditions were not True
# ^ You can have as many elif's as you want
# ^ Else runs if no prior conditions were true

age = input("What is your age?")

age=int(age)

if age >= 10:
    print("heres your license")
elif age == 9:
    print("Hahahaha too little uno years")
else:
    print("Too young little one")

