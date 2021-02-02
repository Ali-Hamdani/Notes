#Question NO:
def increment_score(score,bonus,points=1):
    if bonus==True:
        points=points*2
    score=score+points
    return score
points=5
increment_score(10,0,)
#Question NO:3
def update_score(current,value):
    current+=value
    return current
update_score(45,2)
#Question NO:4
def get_balance():
    #Return the current balance of the bank account
    return balance
 #Question NO:5
numlist=[0,1,2,3,4]
print(5 in numlist)
# False
#Question NO:6
def checktype(value):
    datatype=type(value)
    return datatype
print(checktype(True))
print(checktype(1.0))
print(checktype(1))
print(checktype("True"))
#<class 'bool'>
#<class 'float'>
#<class 'int'>
#<class 'str'>
--------------
#Question NO:7
average_balance=(total_deposits/number_of_customers)
average_balance=float(total_deposits/number_of_customers)
​#Question NO:8
num1=eval(input("please enter the first number:"))
num2=eval(input("please enter the second number:"))
if num1==num2:
    print("The two numbers are equal.")
    if num1<=num2:
        print("Number 1 is less than number 2.")
# The print statement at line 04 will only print if the two numbers 
# are equal.   YES
 
#The print statement at line 06 will only print if num1 is greater 
# than num2    NO
#Question NO:9
alph="abcdefghijklmnopqrstuvwxyz"
print(alph[3:15])
print(alph[3:15:3])
print(alph[3:15:-3]) #The answer of this is empty
print(alph[15:3:-3])
print(alph[15:3])    #The answer of this is empty

#Result
# defghijklmno
# dgjm

# pmjg

#Question NO:11
def get_discount(minor,senior):
    discount=0.1
    if not (minor and senior):
        discount=0
    return discount
get_discount(2,3)
#Question NO:12
a='config1'
print(a)
b=a
a+='config2'
print(a)
print(b)
# What is displayed after the first print?              config1
# What is displayed after the second print?             config1config2
# What is displayed after the after the third print?          config1

#Question NO:14
0 or 5        #--------------->5
bool(0)       #-------------->False
None is None  #--------------->True
-5<0<5        #--------------->True

#Question NO:15
x=4
while x>=1:
    if x%4==0:
        print("party")
    elif x-2 <0:
        print("cake")
    elif x/3 ==0:
        print("greeting")
    else:
        print("birthday")
    x=x-1
# party
# birthday
# birthday
# cake
#Question NO:17
age=input('Enter your age:')
year=input('Enter the four digit year')
born=eval(year)-eval(age) # the eval built in function is used that means age and year are string.
#we can not pass any other data type in eval.eval accept only string data type.
message="you were born in" +str(born)
print(message)
# What data type is age in line 01?     str
# What data type is age in line 03?     int
# What data type is age in line 04?     str

#Question NO:18
list_1=[1,2]
list_2=[3,4]
list_3=list_1+list_2
list_4=list_3*3
print(list_4)
#[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

#Question NO:19
# A. colors[1:2]

#Question NO:20
def safe_divide(numerator,denominator):
    if numerator is None or denominator is None:
        print("A required value is missing")
    elif denominator==0:
        print("The denominator is zero.")
    else:
        return numerator/denominator
safe_divide(0,0)
#Question NO:21
def time_table ():
    for col in range (2,13):
        for row in range (2,13):
            print(row*col,end=" ")
            print( )
time_table()        
#Question NO:22
num=int(input("Enter a number with 1 or 2 digits:"))
digits="0"
if num>-10 and num <10:
    digits="1"
elif num>-100 and num <100:
    digits="2"
else:
    digits="more than 2 digits"
print(digits)
#Question NO:24
numlist=[1,2,3,4,5]
alphalist=["a","b","c","d","e"]
if numlist==alphalist:
    print("The values in numlist are equal to alphalist")
else:
    print("The values in numlist are not equal to alphalist")
#Question NO:26
def search(item,term):
    for i in range(len(item)):
        if item[i]==term:
            print("{0} was found in the list.".format(term))
            break
        else:
            print("{0} was not found in the list.".format(term))
a=[1,2,3,4,5,6,7]
search(a,6)
#Question NO:25
from random import randint
target =randint(1,10)
chance=1
print("Guess an integer from 1 to 10.You will have 3 chances.")
while chance<=3:
    guess=int(input("Guess an integer:"))
    if guess > target:
        print("Guess is too high")
    elif guess<target:
        print("guess is too low")
    else:
        print("guess is just right")
        break
    chance+=1    
#Question NO:27
#Each salary in the list is updated based on in crease.Employees making.
#$150,000 or more will not get a raise.
# Salary list is populated from employee database,code not shown.
for index in salary_list:
    if salary_list[index]>=150000:
        continue
    salary_list[index]=(salary_list[index]*1.03)+500
#Question NO:28
import sys
try:
    file_in_open("in.txt","r")
    file_out=open("out.txt","w+")
except IOError:
    print('cannot open',file_name)
else:
    i=1
for line in file_in:
    print(line.rstrip())
    file_out.write("line"+str(i)+":"+line)
    i=i+1
    file_in.close()
    file_out.close()
    # No change is needed

#Question NO:29
import math
# default motion for happy clown
power=True
move=0
while(power):
    if move==0:
        turnvalue=math.pi/move#causes a runtime error due to division by zero
        move+=5
        else:
            turnvalue=0
            move=0
#which error exist in this  code
#Question NO:30
while True:
    try:
        x=int(input("Please enter a number:"))
        break
        except valueError:
            print("Not a valid number.Try again...")
#Question NO:31
employee_pay=[15000,120000,35000,45000]
count=0
sum=0
for index in range(len(employee_pay)+1):
    count+=1
    sum+=employee_pay[index]
    average=sum/count
    print("the total pay roll is:,sum")
print("The total payroll is:",sum)
print("The average salary is:",average)
#Question NO:32
#The number is a multiple of 5.
#The lowest number is 5
#The highest number is 100
#Which two code segments will meet the requirements?
from random import randrange
prit(randrange(5,105,5))

from random import randrange
print(randint(1,20)*5)
#Question NO:33
random.randrange(0.0,1.0)
#Question NO:34
name=input("What is your name")
score=0
count=0
sum=0
while (score!=-1):
    score=int(input("Enter your score:(-1 to end)"))
    if score==-1:
        break
        sum+=score
        count+=1
        average=sum/count
        print("{ },your average score is:{ }"%(name,average))
#Question NO:39
def print_table(file):
    data=open(file,'r')
    for record in data:
        fields=record.split(",")
        print("{10:0},{1:5:1f},{2:7:2f}",format(fields[0],eval(fields[1]),eval(fields[2])))

