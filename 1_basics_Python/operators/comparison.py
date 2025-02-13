# Comparison operators
# ==, !=, >, <, >=, <=  are comparison operators
# They are used to compare two values
a=10
b=20
c=10
print(f"{a}=={b} is {a==b}")
print(f"{a}=={c} is {a==c}")


str1 = "Hello"
sty2="Hello"
str2="hello"
print(f"{str1}=={sty2} is {str1==sty2}")
print(f"{str1}=={str2} is {str1==str2}\n")

# != is not equal to
str1 = "Hello"
sty2="Hello"
str2="hello"
print(f"{str1}!={sty2} is {str1!=sty2}")
print(f"{str1}!={str2} is {str1!=str2}")

# > is greater than
a=45

b=20
print(f"{a}>{b} is {a>b}")

# < is less than

print(f"{a}<{b} is {a<b}\n")

# >= is greater than or equal to
print(f"{a}>={b} is {a>=b}")
c=45
# <= is less than or equal to
print(f"{a}<={b} is {a<=b}")
print(f"{c}<={a} is {c<=a}")