# for loop
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

# SYNTAX: for variable in sequence:
#           code block

print(range(5))
for i in range(1,6): # i is the variable and range(1,6) is the sequence, i will iterate from 1 to 5
    print(i)

print(range(1,10,2))
# for loop with multiple variables
for i in range(1,10):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
for i in range(10,1,-1):
    print(i)
print("\n")


# String iteration
# We can iterate over a string using a for loop
str1="Hello"
for i in str1:
    print(i)


