# if Statement
# if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block). The else clause is optional.

# Syntax:
# if condition:
#     statement(s)

age=18
if age>=18:
    print("Your age is",age,"and you are eligible to vote")

print(age>=18) # True

# else statement
# The else statement is an optional statement and there could be at most only one else statement following if.
age=16

if age>=18:
    print("Your age is",age,"and you are eligible to vote")
else:
    print("Your age is",age,"and you are not eligible to vote")

# elif statement
# The elif statement is used to check another condition if the initial condition is false.

age=17

if age<13:
    print(age,"You are a kid")
elif age<18:
    print(f"{age} age then You are a teenager")
else:
    print("You are an adult")

# Nested if statement
# We can have if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming.
# number is even,odd,positive,negative

num =int(input("enter a number:"))
if num>0:
    print(num,"is positive")
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
else:
    if num==0:
        print(num,"is zero")
    else:
        print(num,"is negative")

# useCases of Practical Applications
# Determine a year is a leap year or not using nested statements
year = int(input("Enter a year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")
