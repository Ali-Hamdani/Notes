from datetime import datetime
print(dir(datetime))# dir is to see the directory of date time.
# print(help(datetime.date))#help is to get help about anything.
now=datetime.now() # To get the exect time. 
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.microsecond)
# strftime function, We can change the format of every kind of string.
year=now.strftime("%Y")
print(year)
month=now.strftime("%m")
print(month)
day=now.strftime("%d")
print(day)
time=now.strftime("%H:%M:%S")
print(time)
date_time=now.strftime("%m/%d %Y,%H:%M:%S")
print(date_time)
date=now.strftime("%D,%M,%Y")
print(date)
#To change any date or time string into python datetime module.    
moon_landing="7/29/1969"
moon_landing_datetime=datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))
date_string='04 june,2020'
type(date_string)
date_object=datetime.strptime(date_string,"%d %B,%Y")
type(date_object)
print(date_object)
a=now-date_object
print(a)
#Directive                                     #Description                                             #Example
#  %a                                      weekday,short version                                           wed
#  %A                                      Weekday,full version                                         wednesday 
#  %w                                      weedday as a number,0_6,0 is sunday                              3
#  %d                                      Day of month 01-31                                               31
#  %b                                      Month name,short version                                         Dec
#  %B                                      Month name,full version                                       December
#  %m                                      Month as a number 01-12                                          12
#  %y                                      Year,short version,without century                               18
#  %Y                                      Year,full version                                               2018

# inspecct modules
# Basic methods

class Greeter:
    def __init__(self,_name):
        self.name=_name
    def say_hello(self):
        print('Hello {}!'.format(self.name))
    def say_goodbye(self):
        print('Goodbye {}!'.format(self.name))
my_greeter=Greeter('john')
string_var='This is a variable'
numeric_var=453.324
#check available methods
print('\ncheck id,type and methods of an class object')
print("class id:",id(my_greeter))
print("class type:",type(my_greeter))
print("class directory:",dir(my_greeter))

print('\ncheck id,type and methods for a variable containing string value')
print("string_var id:",id(string_var))
print("string_var type:",type(string_var))
print("string_var dir:",dir(string_var))

print('\ncheck id,type and methods for a variable containing numeric value')
print("numeric_var id:",id(numeric_var))
print("numeric_var type:",type(numeric_var))
print("numeric_var attr:",dir(numeric_var))

string_var.islower()


#Inspect methods

import inspect
inspect.getmembers(my_greeter)
 
import os
testvar='Hello'
exp=lambda x,y:x*y
inspect.ismodule(os)
inspect.isfunction(exp)
inspect.isfunction(my_greeter.say_goodbye)
inspect.ismethod(my_greeter.say_goodbye)
def show_name_age(first_name:str,last_name:str,age:int):
    print('{} {} is {} years old'.format(first_name,last_name,age))
sig=inspect.signature(show_name_age)
print(sig.parameters)
spt=inspect.signature(string_var.split)
print(spt.parameters)

