calculator is function and if else:
def add(x,y):
 return x+y
def subtract(x,y):
 return x-y
def multiplication(x,y):
 return x*y
def division(x,y):
 return x/y
print("Select option 1. '+'  2. '-'  3.'*'  4.'/'") 
choice=(input("Enter your choice: "))
if choice in ('1','2','3','4'):
  num1=int(input("Enter 1st number:  "))
  num2=int(input("Enter 2nd number:  "))
  if choice=='1':
      print("The result of addition is:")
      print(num1,"+",num2,"=",add(num1,num2))
  elif choice=='2': 
      print("The result of subtraction is:")
      print(num1,"-",num2,"=",subtract(num1,num2)) 
  elif choice=='3': 
      print("The result of multiplication is:")
      print(num1,"*",num2,"=",multiplication(num1,num2))   
  elif choice=='4': 
      print("The result of division is:")
      print(num1,"/",num2,"=",division(num1,num2)) 
  else:
      print("You put a wrong number")
else:
      print("You put a wrong number")    

only if else-

print("Select option 1. '+'  2. '-'  3.'*'  4.'/'") 
choice=(input("Enter your choice: "))
if choice in ('1','2','3','4'):
  num1=int(input("Enter 1st number:  "))
  num2=int(input("Enter 2nd number:  "))
  if choice=='1':
      a=num1+num2
      print("The result of addition is:")
      print(num1,"+",num2,"=",a)
  elif choice=='2':
      a=num1-num2
      print("The result of subtraction is:")
      print(num1,"-",num2,"=",a) 
  elif choice=='3': 
      a=num1*num2
      print("The result of multiplication is:")
      print(num1,"*",num2,"=",a)   
  elif choice=='4': 
      a=num1/num2
      print("The result of division is:")
      print(num1,"/",num2,"=",a) 
  else:
      print("You put a wrong number")
else:
      print("You put a wrong number")      

using while expext-

print("Select option 1. '+'  2. '-'  3.'*'  4.'/'") 
while True: 
 choice=(input("Enter your choice: "))
 if choice in ('1','2','3','4'):
   try:     
     num1=int(input("Enter 1st number:  "))
     num2=int(input("Enter 2nd number:  "))
   except ValueError:
        print("Invalid input. Please enter a number.")
        continue  
   if choice=='1':
      a=num1+num2
      print("The result of addition is:")
      print(num1,"+",num2,"=",a)
   elif choice=='2':
      a=num1-num2
      print("The result of subtraction is:")
      print(num1,"-",num2,"=",a) 
   elif choice=='3': 
      a=num1*num2
      print("The result of multiplication is:")
      print(num1,"*",num2,"=",a)   
   elif choice=='4': 
      a=num1/num2
      print("The result of division is:")
      print(num1,"/",num2,"=",a) 
   next_calculation = input("Let's do next calculation? (yes/no): ")
   if next_calculation == "no":
          break
else:
      print("You put a wrong number")  

##With while,try except

def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
print("Select operation 1.+ 2.- 3.*")  
while True:
    choice=input("Enter your choice: ")
    if choice in ('1','2','3','4') :
        try:
            num1=int(input("Enter"))
            num2=int(input("Enter"))
        except:
            print("ValueError")
    if choice=='1':        
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice=='2':        
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice=='3':        
        print(num1,"*",num2,"=",multiply(num1,num2))
    else:
        print("stop")
    break     

###Times table-
a=int(input("Enter the number for times table: "))
i=0
while i<=11:
    z=i*a
    print(a,"*",i,"=",z)
    i+=1
           
      
    