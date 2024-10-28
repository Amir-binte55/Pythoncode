#Write a Python program to swap the values of two variables without using a temporary variable-
#using a temporary variable
x=5
y=15
temp=x
x=y
y=temp
print(x)
print(y)

#Without using a temporary variable

x=input("Enter the value of x: ")
y=input("Enter the value of y: ")
x,y=y,x
print("x=",x)
print("y=",y)

#Write a Python program that takes an integer as input and prints whether it is even or odd.

n=int(input("Enter a number: "))
if (n % 2 ) == 0 :
  print("The number {0} is even".format(n))
else:
    print("The number {0} is odd".format(n))

#Write a Python function to reverse a given string and return the reversed string.

x="Anika"
print(x[-1],x[-2],x[-3],x[-4],x[-5]) or print(x[::-1])

#Given a list of integers, write a Python program to convert each element of the list to a string.

list_string = [1, 12, 15, 21, 131]
output = [str(x) for x in list_string]
print(output)
 
#Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.

x=float(input("Enter the celsius temperature: "))
y=x*(9/5) + 32
print("The Fahrenheit is {} ".format(y))

