#Data structure of python-

mylist=["apple","banana","cherry","lily","Mangoe"]
newlist=[x for x in mylist if x!="apple"]
print(newlist)
[print(x) if x!="banana" else "orange" for x in mylist]
[print(x.upper()) for x in mylist]
newlist=['hello' for x in mylist]
print(newlist)
[print(x) for x in range(50) if x!=40]

#list

list=["anika",29,"tree",100,"love","buty"]
print(list[-1])
print(len(list))
x=list.pop()
print(list)
print(list[2:5])
del list[3]
print(list)
list.remove("tree")
print(list)
list.append("Guru")
print(list)
list[1]=50
print(list)
list.insert(3,"Hello")
print(list)
if "loo" in list:
    print("Yes")
else:
    print("No")
list1=["kiki",70,"strew",90]
list.extend(list1)
print(list)

list=[23,78,12,45,32,70,122]
list1=["Hall","loop","tut"]
list.sort()
print(list)
list.reverse()
print(list)
print(list[1],list[2],list[3])
list2=list+list1
print(list2)

mylist=["Anika","anni","Robin",345,100,"free"]
for x in mylist:
    print(x)
for i in range(len(mylist)):
    print(mylist[i])
i=0
while i<len(mylist):
    print(mylist[i])
    i+=1

#list comprehension-
mylist=["Anika","anni","Robin","free","apple"]
[print(x) for x in mylist]
[print("hello") for x in mylist]    
newlist=[x for x in mylist if 'a' in x ]
print(newlist)
newlist=[x for x in mylist if x!="apple" ]
print(newlist)
[print(x.upper()) for x in mylist]
[print(x.lower()) for x in mylist]
[print(x) for x in range(10) if x<5]


dict-
dict={"name":"Anika",
      "father name":"MD Amir",
      "Age":29,
      "Gender":"Male",
      }
print(len(dict))  
print(type(dict))
print(dict.keys())
print(dict.values())
if "Age" in dict:
    print(dict["Age"])
dict["Mother name"] ="Taslima" 
dict["name"] ="Binte"   
print(dict)
print(dict.items())
dict.update({"Age":"27"})
print(dict)
dict.pop("Age")
print(dict)
print(dict.clear())

tuple-

tuple1=("apple","orange",123,"hello")
tuple3=("desse",)
print(tuple1)
print(len(tuple1))
print(type(tuple1))
print(tuple1+tuple3)
a=list(tuple1)
print(a)
a.insert(1,"Anika")
print(a)
a[3]="234"
print(a)
a.append("gog")
print(a)
a.remove("orange")
print(a)
tuple2=tuple(a)
print(tuple2)    
if "hello" in a:
    print("yes")
b=set(tuple1) 
print(b)
print(type(b))
x=(True,[1,2,3],("amin","anika"),"Zebra")
y=x*2
print(x)
print(y)
