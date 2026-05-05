#chapter 2
#strings and conditional statements
str1 = "i am the coder"
print(str1[0]) #give the value which has 0 position
print(str1[0:5])#give the value from 0 to 4position

#practice question 1

name = input("enter a name: ")
len = len(name)
print(len)

#conditional statements 
#practise question1

num = int(input("enter number: "))
rem = num % 2
if(rem == 0):
    print("EVEN")
else:
    print("ODD")

# practise question 3 
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a >= b and a >= c):
    print("the largest number is first",a)
elif(b >= c):
    print("the largest number is second",b)
else:
    print("the largest number is third",c)
# practise question3 
x = int(input("enter a number:"))
if(x % 7== 0):
    print("multiple of 7")
else:
    print("not a multiple")