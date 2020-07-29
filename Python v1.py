print('There are 2 types of languages.Interpreted type, Compiler type.')
print('Line by line checking is called Interpreted mood, Whole checking is called compilation mood')
print('Python is Interpreted language.It is a sensetive language')
print('Data Type')
print("To find data type. we can use type command")
Types_of_data="Text_type,Numeric_type,Boolen_type,Sequence_type,Mapping_type,Set-type,Binary_type"
print(Types_of_data)
Text_type="string"
print(Text_type)
print("String is immutable")
print("The pysical address of the string is {}".format(id(Text_type)))
          # >>Creating strings
          # we creat a string by putting all quotes around text because of programming language. 
          # we need to tell a computer weather the value is a number,string,or somthing else.
print("We can write string with silgle & double quotes")
abubakar='First caliph'
print(abubakar)
          # one can start with double quotes.
          # But you can not start with double quotes and with single quotes.we can not use both at a sametime.
          # It has to be consistant.
          # For Example
          # Because python language will stop running. That is why,i will not run this Example.
          # abubakar="First caliph'
          # print(abubakar)
          # It will show me a error message. Whin i run this program.
abubakar="First caliph"
print(abubakar)
# Syntax and Syntax Error
          # Syntax means the arrangement and order of word in a Syntax.
          # Syntax error means that you did something in an order python was not expecting or you missed something.
          # EOL means end of line
          # Adding a second line to your command.
          # You can use 3 single quotes to write a second or third or as many lines you to add into it.
print("If we want write 2 or more sentances,we must use tripple quotes")
Abubakar='"First caliph. He was a great man. A companion of Hazrat Muhammad(SAW)"'
print(Abubakar)
print("Strying problem hendling")
          # For example
          # Silly_string='He said,"Aren't can't shouldn't wouldn't."'
          # print(Silly_string)
          #  It will show an syntax error=invalid syntax
          # we can correct these difficult syntance by using single tripple quotes( '''      ''')
Silly_string='''He said,"Aren't can't shouldn't wouldn't."'''
print(Silly_string)
          # There is one other another technique to solve this problem by adding backslash
          # For example
Silly_string='He said,"Aren\'t can\'t shouldn\'t wouldn\'t."'
print(Silly_string)  
          # If we use double quotes then we backslash at the start and at the end of double quotes
Silly_string="He said,\"Aren't can't shouldn't wouldn't.\""
print(Silly_string)
# Embedding value in strings continued.....
          #  method 1
myscore=1000
message='My score %s points'
print(message%myscore)
math=82
points='i got %s out of 100 points'
print(points % math)
studyhour=8
daily="I study %s hours everyday"
print(daily %studyhour)
          # method 2
result="I challanged myself to be succesful in a new filed.The field of AI. If i earned %s > %s  monthly i will consider myself successful" 
print(result%(36000,35000))
rs="pakistani curancy %s Rs is equal %s $ US dollars"
r=(35000/150)
print(rs%(35000,r))
lowestrate=("The one could earn the lowest money on freelancing is %s$. which is equal to %sRs" )
e=25*150
print(lowestrate%(25,e))
monthly_estimate="if could get even 5$ work on freelancing in %sdays then i could earn %sRs every month"
q=e*10
print(monthly_estimate%(10,q))
# Multiplying stryings
        #if 10 multiplying 5 the answer is 50. What if 10 multiplying by "a". the python's answer
print(10*'a')
       # The answer will be 10 times a like(aaaaaaaaaaaa)
       # an interesting project
       # in this % means spaces
spaces=(' '*25)
print('%s DHA phase 5'%spaces)
print('%s clifton'%spaces)
print('%s west snoring'%spaces)
print()
print()
print('Dear Sir,')
print()
print('I wish to report that the tiles are missing from the')
print('outside toilt roof')
print('I think it was bad wind the other night that blew them away.')
print()
print('regards')
print('Ali')
print("String changing case.(Using built in function)")
name="pakistani"
name.upper()
name.lower()
Name="PAKISTAN"
Name.title()
Numeric_type="integer,Float,complex_number"
print("Numeric_type")
print("there are 3 types of numeric data")
      # integer,(positive or negative whole number without fractionl part)
      # Float,(any real number with fractional part)
      #complex_number:A number with real and imagenary component represented as x+yj.x and y are flots and j is
      # (square root of -1 called an imaginery number )
Boolen_type='bool'
print(Boolen_type)
print("Boolen")
print("Data built in 1 or 2 values True or False, T and F are always capital.")
      # For Example
boolen1=False
print(bool(boolen1))
print(type(boolen1))
boolen2=True
print(bool(boolen2))
print(type(boolen2))
q=4
w=5
print(bool(q==w))
false_conditons="If these values are passed then it will return False otherwise it always return True(False,None,(),[],{},0,0.0) "
print(false_conditons)
print("Type casting.Changing data types")
float(1)
int(9.4)
str(23)
bool(0)
bool(1)
Sequence_type="array,list,tuple,range"
print(Sequence_type)
print("Array")
      # Array is a container which can hold a fix number of items and these items should be of the same type.Most of the data structures
      # make use of arrays to implement their algorithms.Each item stored in array called Element. Location of the Element has numerical index.
      # Array is not in python so to use that array we have to import it.Array is homogenios.
      # from array import*
      # arrayname=(typecode,[initializers])
from  array import*
array1=array('i',[12,54,678,89,90,454,3434,678,9090])
print(array1)
print(type(array1))
array1.insert(1,60)
print(array1)
array1.remove(89)
print(array1)
print(array1.index(3434))
print(array1)
for x in array1:
	print(x)
array1.append(56567)
print(array1)
print(array1[0])
print(array1[4])
print(array1[-1])
     # Array is mutable.Array can not be divided by any number but if we import array from numpy then we can divide it.
from numpy import array
arr=array([11,22,33,44,55,66,77])
print(arr)
di=arr/2
print(di)
print("list")
print('List is mutable')
print(' List statments are as follow')
list_a=['python','is','great','23','454','5656']
print(list_a)
print("the physical address of list_a is {}".format(id(list_a)))
list_a.append('python is great')
print(list_a)
print("the physical address of list_a st_a is {}".format(id(list_a)))
list_a.insert(2,"I love you.")
print(list_a)
list_a[2]='5656565656'
print(list_a)
list_a.remove('23')
print(list_a)
print(list_a.index('454'))
del list_a[1]
print(list_a)
list_a[-1]=222
print(list_a)
# Getting value from the list
print(list_a[0])
# slicing, 
print(list_a[0:3:2]) 
fruits=['apple','mangos','grappes','pottaos','1','mangos']
print(fruits)
print(fruits.index('1'))
print(fruits.count('mangos'))
print(fruits.index('grappes'))
print(fruits.count('pottaos'))
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)
fruits.pop()
print(fruits)
fruits.pop()
print(fruits)
print(" using list as a stack.means last in first out.")
stack=[1,2,3,4,5]
print(stack)
stack.append('34')
print(stack)
stack.append('32')
print(stack)
stack.append('75')
print(stack)
stack.append('33423')
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
# List comprehension
print('List comprehension')
square=[]
for x in range(10):
    square.append(x)
    print(square)

square=[]
for i in range(4,8):
    square.append(i)
    print(square)
cheeta_speed_in_Km=[]
for x in range(0,110,10):
    cheeta_speed_in_Km.append(x)
    print(cheeta_speed_in_Km)
combs=[]
for x in [1,2,3]:
    for y in [3,2,1]:
        if x !=y:
            combs.append((x,y))
            print(combs)
# Nasted list comprehension 
print('Nasted list comprehension ')
matrix=[
[1,2,3],
[4,5,6],
[7,8,9]
]
print(matrix)
print("list transpose")
print(list(zip(*matrix)))

print('using list as queues(first come first out). using list as a queue is not efficent so that is why we use collection.deque')
from collections import deque
line=deque(['ali','usman','umair','atif'])
print(line)
line.append('sdfs')
print(line)
line.append('sdfwersdffs')
print(line)
line.append('scvsfdfs')
print(line)
line.append('sdfsdffs')
print(line)
line.popleft()
print(line)
line.popleft()
print(line)
line.popleft()
print(line)
line.popleft()
print(line)
# Tuple
print('tuple')
tuple_a=(12,45,678,90)
print(tuple_a)
print(type(tuple_a))
tuple_b=23,6,3,27
print(tuple_b)
print(type(tuple_b))
# dictionary in a list
dic={'Hafiz':'Because of remembering quran','Syed':'Family Name','Ali':'Personal Name','Hamdani':'Family Origin'}
a=[]
a.append(dic)
print(a)
Dic={1:"Hello",2:"How are you",3:"What do you want?",4:"Where are you from?"}
s=[]
s.append(Dic)
print(s)
print(a[0]['Hafiz'])
print(a[0]['Syed'])
print(a[0]['Ali'])
print(a[0]['Hamdani'])
print(s[0][1])
print(s[0][2])
print(s[0][3])
print(s[0][4])
# tuple is immutable but it can store mutable objects like list.
# Packing & unpacking concept
x=2,4,6
a,b,c=x
print(a)
print(b)
print(c)
Mapping_type='Dictionary'
print(Mapping_type)
print("A Dictionary has pairs each pair has two comments one=key & two=value")
Dic={1:"Zoya",2:"Darakshan",3:"Zeenat"}
print(Dic)
print(type(Dic))
tel={'mark':'facebook','jack':'Twitter','Bill':'Microfoft','guido':'python'}
print(tel)
tel['markoni']='radio'
print(tel)
print(['mark'in tel])
print(['jack'in tel])
print(['azeem'in tel])
e={'Name':'Shams','children':['Humairah','Abdul','Rahman']}
print(e['children'][0])
print(e['children'][1])
print(e['children'][2])
Set_type="set,frozenset"
print(Set_type)
set_x={"apple","banna","cheery","mango","graps"}
set_y={"apple","banna","allu","piaz"}
set_operation="union,intersection,difference","symetric_difference"
print(set_operation)
print(set_x|set_y,"union")
print(set_x&set_y,"intersection")
print(set_x-set_y,"difference")
print(set_y-set_x,"difference")
print(set_y^set_x,"symetric_difference")
frozen_set='frozenset changes mutables objects into immutable'
print(frozen_set)
la=["asdd","sdfsdf","dfsdf","sdfsdf"]
print(la)
print(type(la))
frozen_seta=frozenset(la)
print(frozen_seta)
print(type(frozen_seta))
Binary_type='bytes,byte_array'
print(Binary_type)
bytes_a=('The bytes method returns an immutable bytes objects initialized with the given size and data')
print(bytes_a)
st='python is great'
ar=bytes(st,'utf-8')
print(ar)
size=50
da=bytes(size)
print(da)
bytes_array=('The bytesarray  method returns an mutable bytes objects initialized with the given size and data')
print(bytes_array)
arr=bytearray(st,'utf-8')
print(arr)
arr[14]=64
print(arr)
# https://ykode.id/under-the-bonnet-representing-characters-and-strings-ff7cec26ee3c
memoryview_a=('The memoryview method returns a memory view object of the given object of the given argument.')
mv=memoryview(arr)
print(mv[0])
print(mv[0:5])
# Loops, for loop & while loop
ar=[1,3,4,6,45,34,23,324,57]
for e in ar:
    if e==324:
        break
for i in ar:
    if i==23:
        continue
    print(i)
for a in range(5):
    print("Ali")
for a in range(5):
    print(a,"Ali")
for n in range(2,10,3):
    print(n)
for n in range(10,1,-2):
    print(n)
print("for loop on List")
cities=['karachi','multan','quetta']
for city in cities:
    print(f"The city under consideration is {city}")
for num in [11,22,33,44,55]:
    print(num)
print("for loop on string")
for char in 'country':
    print(char)
print('for loop on Tuple')
country='Pakistan','America','I love you'
for a in country:
    print(a)
for number in range(10):
    if number%3==1:
        break
    print(number)
for n in range(10):
    if n%3==2:
        break
    print(n)
for i in [5,9,11,12]:
    if i%2==0:
        break
    print(i)
for num in range(10):
    if num==7 or num==4:
        continue
    print(num)
    for i in range(4,123):
    if i<99:
         print(i,"Love")
    elif i==99:
        continue
    elif i<120: 
        print(i,"Love")
    else:
        break
print("Nasted for loop")
for a in range(5):
    print("Inner loop begins")
    for char in "china":
        print(a,char)
Tablenumber=int(input("Enter table number"))
for a in range(1,11):
    print(f"{Tablenumber}*{a}={Tablenumber *a}")
tables=int(input("Enter table"))
for table in range (2,tables+1):
    for num in range (1,11):
        print(f"{table}*{num}={table *num}")
students= {'Names':'Zaid','calss':'AI','program':'piaic','Ag':44}
for values in students.values():
    print(values)
for key in students.keys():
    print(key)
print("While Loop")
a=0
while a<=10:
    print(a,"This is while loopprinting")
    a+=1
a=10
while a>=10 and a<=15:
    print("What?")
    a+=1
flag=True
favfoods=[]
while flag:
    userinput=input("Enter your favourite foods")
    if userinput=='q':
        flag=False
    else:
        favfoods.append(userinput)
Print("Functions, Functions are a way to achieve the modularity reuseability in code")
# Parameter less function 
# To use a function,we need to call its name.
# Parameter less function 
def add():
    num1=int(input("Enter a number"))
    num2=int(input("Enter a number"))
    print(num1+num2)
add()
# Parameterised function & Positional argument
def add (num1,num2):
    print(num1+num2)
# Arguments
add(12,34)
print("To check the signature.We press shift+tab ")
# Passing information keyword arguments 
def fullname(first,middle,last):
    print(first , middle , last)
fullname("syed","ali","hamdani")
# Key-word argument
def fullname(first,middle,last):
    print(first , middle , last)
fullname(middle="husain",last="khan",first="ali")
# Key-word argument,Key-word argument must come at last
def fullname(first,middle,last):
    print(first , middle , last)
fullname("syed","Ali",last="Hamdani")
# Default value parameters
def add(num1=0,num2=1):
    print(num1+num2)
add()
add(2,4)
def fullname(first,last,middle=""):
    print(first , middle , last)
fullname('syed','hamdani','ali')
fullname('syed','hamdani')
def display_nums(first,second,*opt_nums):
    print(first)
    print(second)
    print(opt_nums)
display_nums(23,45,4545,3434,676,34,342342,78787,34234,)
def pizzaorder(size,flavour,*toppings):
  print(size)
  print(flavour)
  print(toppings)
pizzaorder(23,"Oange","red","sesdf","sdsd")
def pizzaorder(size,flavour,*toppings):
    print(f"your order for piza size{size}, and {flavour} and toppings {toppings} are ready" )#This line has syntex error
pizzaorder(23,"Oange","red","sesdf","sdsd")
def add(val1,val2):
    ans=val1 + val2
    return(ans)
result=add(2,4)
result
def add(val1,val2):
    ans=val1+val2
    return ans, "Hello Function"
result =add(2,4)
result
def math(a,b):
    return ((a+b),(a-b))
result=math(23,13)
result
# Using function as variable which they really are
def add(num1,num2):
    return (num1+num2)
def sub(num1,num2):
    return(num1-num2)
def mul(num1,num2):
    return(num1*num2)
def divid(num1,num2):
    return(num1/num2)
result=add(23,45),sub(12,45),mul(54,21),divid(53,234)
result
# Functions local and globle varibles
def behappy():
    name="Mr.A"# Local varaibles
    print(f"{name} is very happy today")
behappy()
anothername="Mr.B"
def sad():
    print(f"{anothername} is very sad today")
sad()
# Functions within functions
def commissioncalc(sales):
    if sales>100:
        return sales*100
    elif sales>50:
        return sales*50
    elif sales>20:
        return sales*20
    else:
        return 0
def salarycalc(basic,sales):
    grosssalary=basic + commissioncalc(sales)
    print(f"your gross salary is {grosssalary}")
salarycalc(5000,80)   
# Object oranted programing
class Car():
    def __init__(self,make,model,year): #Attributes are variables in programming
        self.make=make
        self.model=model
        self.year=year
        self.battery="200amp" #Default attribut
    def descriptionCar(self):
        print(f"The make of car is {self.make}")
        print(f"The model of car is {self.model}")
        print(f"The year of car is {self.year}")
    def move(self):
        print(f"{self.make} is moving with speed")
    def applyingbreak(self):
        print(f"{self.model} has applied the break")
    def desbattery(self):
        print(f"The battery of car is {self.battery}")
    def setbatterysize(self,newsize):
        self.battery=newsize
    def getbatterysize(self):
        print(f"The size of your car's battery is {self.battery}")
# creating objects of class
car1=Car("Honda","civic",2019)
car2=Car("Suzuki","cultus","2015")
car1.make
car1.model
car1.year
car1.descriptionCar()
car1.move()
car1.applyingbreak()
car2.make
car2.model
car2.year
car2.descriptionCar()
car2.move()
car2.applyingbreak()
# Changing attributes value
car1.battery
car2.battery
car2.battery="300amp"
car2.battery
car1.battery
car1.getbatterysize()
car1.setbatterysize("500amp")
car1.getbatterysize()
class Car():
    def __init__(self,make,model,year): #Attributes are variables in programming
        self.make=make
        self.model=model
        self.year=year
        self.battery="200amp" #Default attribut
    def descriptionCar(self):
        print("The make of car is" self.make)
        print("The model of car is",self.model)
        print("The year of car is" ,self.year)
    def move(self):
        print(self.make, "is moving with speed")
    def applyingbreak(self):
        print(self.model," has applied the break")
    def desbattery(self):
        print("The battery of car is", self.battery)
    def setbatterysize(self,newsize):
        self.battery=newsize
    def getbatterysize(self):
        print("The size of your car's battery is",self.battery)
car1=Car("Honda","civic",2019)
car2=Car("Suzuki","cultus","2015")
car1.make
car1.model
car1.year
car1.descriptionCar()
car1.move()
car1.applyingbreak()
car2.make
car2.model
car2.year
car2.descriptionCar()
car2.move()
car2.applyingbreak()
# Changing attributes value
car1.battery
car2.battery
car2.battery="300amp"
car2.battery
car1.battery
car1.getbatterysize()
car1.setbatterysize("500amp")
car1.getbatterysize()
# MOdule
# %load maths.py  (%load maths.py)
def add(a,b):
    return a+b
def sub(a,b):
    return(a-b)
import maths as m
m.add(1,4)
m.sub(23,4)
# Data files
with open ("file_name.txt","r") as file:
    content=file.read()
    print(content)
with open ("name.txt","w") as file:
file.write("This is testing")
with open ("file_name.txt","a") as file:
file.write("aoe me a gia")
with open ("ao_gia.txt","w+") as file:
    file.write("You can do what you are interested in")
    file.seek(0)
    print(file.read())
with open ("name.txt","r+") as file:
    file.write("me jet gia")
    file.seek(0)
    print(file.read())
# CSv
import csv
with open ("abc.csv") as file:
    contents=csv.reader(file)
    for content in contents:
        print(content)
with open ("abc.csv","w",newline="") as file: #in subline text we don't need to write ,newline=""
    contents=csv.writer(file)
    contents.writerow(["2020","sdsa","sfge"])
with open ("abc.csv","a",newline="") as file:
     contents=csv.writer(file)
     contents.writerow(["2021","34324","sdfssdg"])
# Json ( java script object notation)
import json
# Writting data in list form
with open ("jsonfile.json","w") as file:
    json.dump([11,22,33,44,55],file)
with open ("jsonfile.json","r") as file:
    content=json.load(file)
    print(content)
with open ("jsonfile.json","a") as file:
    json.dump([66,77,88],file)
# writting data dictionary in json file
customer_29876={"firstname":"David","last name":"Elliott","address":"4803 wellesley St."}
with open("jsondic.json","w") as f:
    json.dump(customer_29876,f)
with open("jsondic.json","r") as f:
    content=json.load(f)
    print(content)
# Exception
# It is arun time error of user mistake.
a=[]
try:
    5/0
except:
    print("Exception caught")
else:
    print("No Exception")
finally:
    print("finally will always run")
import datetime
print(dir(datetime))# dir is to see the directory of date time.
# print(help(datetime.date))#help is to get help about anything.
gir=datetime.date(1991,12,13)# To creat a date 
print(gir)
# We can access the year , month, day saperately.
print(gir.year)
print(gir.month)
print(gir.day)
# There is a function named timedelta.It is used to increase or decrease the date.
dt=datetime.timedelta(100)# 100 is a number of days.positive (+) number will increase the date & Negative (-) number will decrease the date
print(gir+dt)
# Now we use date,time, and datetime all 3 together.
lounch_date=datetime.date(2017,03,30)
lounch_time=datetime.time(22,27,0)
lonch_datetime=datetime.datetime(2017,03,30,22,27,0)
print(lounch_date)
print(lounch_time)
print(lonch_datetime)
# We can access the year , month, day saperately.It is the same in time and datetime function
print(lounch_time.hour)
print(lounch_time.minute)
print(lounch_time.second)
print(lonch_datetime.year)
print(lonch_datetime.month)
print(lonch_datetime.day)
print(lonch_datetime.hour)
print(lonch_datetime.minute)
print(lonch_datetime.second)
# To access the current date
now=datetime.datetime.today()#This will show the exect date and time we run the code.it will also show the microseconds.
print(now)
print(now.microsecond)
now1=datetime.date.today()
print(now1)
now2=datetime.time()
print(now2)
To convet the string datetime into date time object. There is python old version problem, I will deal it later.
 moon_landing="7/29/1969"
 moon_landing_datetime=datetime.datetime.strptime(moon_landing, "%m/%d/%y")
 print(moon_landing_datetime)
 print(type(moon_landing_datetime))