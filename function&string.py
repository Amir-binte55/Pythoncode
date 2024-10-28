#basic of py-

a="Hello,World!"
b="  Hello,Anika!"
print(a[::-1])
print(a[2],a[1],a[5])
print(a[1:5],a[6:],a[-4:])
print(a.lower())
print(a.upper())
print(b.strip())
print(b.replace("A","I"))
print(a.split(","))
print(a.split("l"))
y=a+""+b
print(y)
print(len(y))

#vowel or consonent-
x=str(input("Enter Alphabet: "))
vowel=['a','e','i','o','u','A','E','I','O','U']
if x in vowel:
    print("{0} is vowel".format(x))
else:
    print("{0} is consonent".format(x))


#other-

x,y,z="oki","cherry","huju"
print(x)
print(y)
print(z)
a=b=c="hey"
print(a,b,c)
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)
print(x+y+z)
print(x,y,z)
x="Awesome"#global
def show():
    print("My man is "+x)
show()
x=56 #local
print("My age is ",x)
#another-
txt="My  name is Anika"
if "Anika" in txt:
    print("Yes")
else:
    print("no")
print("Anika" in txt)
print("Binte" in txt)

#formatstring

age=int(input("enter "))
name="Anikaa"
txt=f"My age is {age:.2f} & name is {name}"
print("My age is {0}".format(age))
print(txt)
b="Anika"
txt=f"My name is {b}"
print(b)
print("My \"love\"")

#python function-
def myfunc(fname):
 print(fname +"ref")
myfunc("gttt")
myfunc("gfth")
def myfunc(*a):
    print(f"The tuple is {a}")
myfunc("Hello","anika",123)    
def void(food):
    for x in food:
        print(x)
fruit=["Apple","Banana","orange"]
void(fruit)
def anika(*,x):
    print(x)
anika(x=3)    
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#lambda-
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)    
print(mydoubler(11)) 
x=lambda a,b:a*b
print(x(5,6))
x=lambda a:a+10
print(x(4))
x=lambda a,b,c:a+b+c
print(x(1,2,3))