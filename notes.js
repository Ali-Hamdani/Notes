//Alert can be used by 2 ways.window.aleart or alert.Alert only work in browser.
window.alert("hi")
alert("555")
//Alert command will not run on node js.To check the installation of node.js use command (node -v) in 
//cmd.To use javascript directly in node.js in cmd.Use these command in cmd.
/*
node
> var a=5;
undefined
>a
5  
To come out from node use command .exit */
console.log("kugjhghkhhg");
console.log("How are you? What are you doing?")
console.log("What happend?")
/* To see the console.log in  google crom browser use inspect & then see console. html file of 
console.log will only show in console tab. OR we can see javascript js file in node.js.In cmd
,first go to the location where the file is.type    node filename.js  */
 document.write("324234234")
 document.write("sdfsdfsdfsdfsdfsd")
 document.write("fjgkhghgkjhdfkjghdhg")
 /* We don't use document.write("") because it intrepte the html file. Its data will show before the
 html text*/
   /*var  is keyword to creat variable. nationality is variable name/identifier. = is assignment operator.
 Pakistan is a value.*/
 var nationality="Pakistan";
 var age=25;
 var isfeepaid=true;
 var weight=60.55;
 console.log(nationality);
 console.log(isfeepaid);
 console.log(weight);
 console.log(age);
 //alert will not run on node js
 alert(nationality)
 alert(age)
 alert(isfeepaid)
 alert(weight)
 age=55; // age is updated
 console.log(age)
 //Undefined & null values
 var width;//not initalizate so undefined
 var na="dfdf";
 na=undefined;
 console.log(width)
 console.log(na)
 // null variable
 var me=null;
 var wo="dfdfdfd";
 wo=null;
 console.log(me)
 console.log(wo)
 //Variable for String
 var Name="Mark";
 var message="It is alright";
 console.log(Name)
 console.log(message)
 Name="john"; //Name is updated
 console.log(Name)
 console.log(message)
 // Variable for numbers
 age=34; // Updated agian 
 var count=56;
 var sum=3+5
 var j=6;
 var b=9;
 var c=j+b;
 console.log(age)
 console.log(count)
 console.log(sum)
 console.log(j)
 console.log(b)
 console.log(c)
 //Variable for booleans
 var isfeepaid=true;
 var exampassed=false;
 console.log(isfeepaid);
 console.log(exampassed);
 /*Javascript data types are dynamic.Javasvript has dynamic types.This means that the same variable can 
be used to hold different data types.*/
var age=34;
console.log(age);
age="Hello";
console.log(age)
age=true;
console.log(age)
//typeof
var Name="Hello";
var isfeepaid=false;
console.log(typeof age)
console.log(typeof Name)
console.log(typeof isfeepaid)
alert(typeof age)
alert(typeof Name)
alert(typeof isfeepaid)
 //Statement and Expressions
 //Each line below is a statement.
 var j=4;                           //Statement 1
 var b=2;                           //Statement 2
 var c=0;                           //Statement 3
 c=j+b;                             //Statement 4
 alert(j)                           //Statement 5
 console.log(c);                    //Statement 6
 //Expression
 /*An expression is a combination of values variables.Function calls and operator,which computes to a 
 value. The computation is called an evaluation.
 a+b;
 4/3
 var a=5;
 a*4;
 "john" " "+"Doe";*/

//Arithmetic Operators
var j=4;
var b=2;
var c=j+b;
var d=j-b;
var e=j*b;
var f=j/b;
var g=j%b;
var h=j**b;
console.log(c);
console.log(d);
console.log(e);
console.log(f);
console.log(g);
console.log(h);
//Assignment Operators
//Example;                                           //Same as
j+=5;                                                 j=j+5;
j-=5;                                                 j=j-5;
j*=5;                                                 j=j*5;
j/=5;                                                 j=j/5;
j%=5;                                                 j=j%5;
j**=5;                                                j=j**5;
 /*BODMAS
 B  Brackets first
 O  orders(i.e. Powers ans square roots,etc)
DM  Division and Multiplication(left_to_right)
AS  Addition and Subtraction(left_to.right)*/
//Concatenating
var j="6"+2;
var b=3+"6";
var c="Hello"+2;
var d =2+"Hello";
var e="Hello"+3+4;
var f=3+4+"Hello"
var g="Hello"+(3+4);
console.log(j)
console.log(b)
console.log(c)
console.log(d)
console.log(e)
console.log(f)
console.log(g)
var Name=prompt("What is your name?");
console.log(Name)
// Default value
var age=prompt("What is your age?","29");
console.log(age)
var newage=age+334;
console.log(newage)

//  Comparision operators
var j="5";
var b=5;
console.log(j==b)
console.log(j===b)
console.log(j!=b)
console.log(j>b);
console.log(j<b)
console.log(j>=b)

console.log(j<=b)
// Logical operators
// &&(AND).In this if there is only one side is false && operator will return false.
console.log(true&&true)
console.log(false&&true)
console.log(true&&false)
console.log(false&&false)
var j=34
var b=j>32&&j<45
console.log(b)
var c=j<3&&j>30
console.log(c)
var d=j<3434&&j>98
console.log(d)
var e=j<32&&j>37
console.log(e)
// ||(or).In this if there is only one side is true || operator will return true.
console.log(true||true)
console.log(false||true)
console.log(true||false)
console.log(false||false)
var j=60;
var b=j<50||j>70
console.log(b)
c=80
var d=c<50||c>70;
console.log(d)
var j=5;
var b=6;
var c=j<10||j>20;
console.log(c)
// !(NOT).This operator will change true into false and false into true.
console.log(!true)
console.log(!false)
j=60
var b=!(j<50);
console.log(b)
var c=80;
var d=!(c>50);
console.log(d)
var j=60
var b=j>100;
var c=!b;
var d=!(j>100);
var e=!true;
console.log("A="+j)
console.log("B="+b)
console.log("c="+c)
console.log("D="+d)
console.log("E="+e)
console.log(!1)
console.log(!0)
console.log(!!1)
console.log(!!0)
var j=6;
var b=!j;
var c=!!j;
console.log("A="+j)
console.log("b="+b)
console.log("c="+c)

//  For Loop
for (i=0;i<3;i++){
  console.log(i)
}
// ---------------------------
console.log("Started new loop")
for (i=9;i<=12;i++){
  console.log(i)
}
// ---------------------------
console.log("Started new loop")
console.log("Infinite loop")
// for ( ; ; ){console.log("what")}
console.log("new loop")
var j=3;
for(i=1;i<=10;i++){
  console.log(j+"X"+i+"="+(j*i))
}
d=parseInt(prompt("Enter any number"))
for (i=1;i<=10;i++){
  console.log(d+"X"+i+"="+(d*i))
}
// Break
for (var i=0;i<6;i++){
  if(i===4){break;}
  console.log("This is i value"+" "+i)
}
// Continue
for (i=0;i<7;i++){
  if(i===4){continue;}
  console.log(i)
}
// Figureing out prime number
num=parseInt(prompt("Enter any number"));
for(var i=2;i<num;i++){
  var result=num%i;
  if(result===0){
      console.log("Number"+" "+num+" "+"is not a prime number")
      break;}
      else{console.log("Number"+" "+num+" "+"is prime")}
}
// Nested for loop
for (var i=0;i<3;i++){
  for (var j=0;j<2;j++){
      console.log("I="+i+"J="+j);
  }
}
var foods=["Pizza","Burger","Snacks"];
for (var i=0;i<foods.length;i++){
    console.log(foods)
}
var foods=[4,78,54,5,6]
for (var i=0;i<foods.length;i++){
    console.log(foods[i])
}
var arr=[]
for (var i=0;i<5;i++){
    arr[i]=i*4;
}
for (var j=0;j<arr.length;j++){
    console.log(arr[j])
}
//  Array
var arr1=["Hello","world","Bye"];
var arr2=[29,38,16,22];
var arr3=[true,false,true,false,true,false];
var arr4=[33.4,55.2,232.1,565.4]
var arr5=[{name:"john"},{name:"jason"}];
var arr6=[74,"Hello",true,{name:"john"}];
console.log(arr1)
console.log(arr2)
console.log(arr3)
console.log(arr4)
console.log(arr5)
console.log(arr6)
// Accessing array elements
var foods=["Pizza","Burger","Snacks"];
console.log(foods)
console.log(foods[0])
console.log(foods[1])
console.log(foods[2])
// If we try to access the element which does not exist.The result will be undefined.
console.log(foods[5])
console.log(foods[9])
// Store result in variable or show output directly
console.log(foods)
var j=foods[0];b=foods[1];c=foods[2];
console.log(j);console.log(b);console.log(c)
console.log(foods)
// Add or replacing element using index
var fastfoods=[];
fastfoods[0]="Aluwalanan"
fastfoods[1]="pakora"
fastfoods[2]="Samosa"
console.log(fastfoods)
// Replacing existing elements
fastfoods[0]="Sandwich"
fastfoods[1]="French Fries"
console.log(fastfoods)
// Length of array
console.log(foods)
console.log(foods.length)
console.log(fastfoods)
console.log(fastfoods.length)
j=[]
console.log(j)
console.log(j.length)
// Adding element by push function
foods.push("Jalabi")
foods.push("Roti")
foods.push("Pakora")
foods.push("Salan")
foods.push(prompt("Enter the first food item"))
foods.push(prompt("Enter the second food item"))
foods.push(prompt("Enter the third food item"))
console.log(foods)
// Stack(Last in first out)
var drinks=[ ];
drinks.push("cola")
drinks.push("oring juice")
drinks.push("pepsi")
drinks.push("water")
console.log(drinks)
drinks.pop()
drinks.pop()
drinks.pop()
console.log(drinks)
// Queue (First in first out)
var sweets=[];
sweets.push("rasgula")
sweets.push("barfi")
sweets.push("gulabjamun")
console.log(sweets)
sweets.shift()
sweets.shift()
sweets.shift()
console.log(sweets)
// ---------------------------------------------
var j=[1,2,3,4,5,6,7,8,9,10]
input=parseInt(prompt("Enter a number to find in array"))
for(i=0;i<j.length;i++){
    if (j[i]===input){
        console.log("Input number is found at index"+" "+i)
    }
}
// Adding element without deleting or replacing in Array,first is index ,second is number of deleteing 
// elements
var foods=["Pizza","Burger","Snacks"];
console.log(foods)
foods.splice(1,0,"Sandwich");
console.log(foods);
foods.splice(0,0,"sharbt")
console.log(foods)
foods.splice(3,0,"yes")
console.log(foods)
// Slicing the array emements
var ar=foods.slice(1,3);
console.log(foods)
console.log(ar)
var ad=foods.slice(0,2)
console.log(ad)
var ae=foods.slice(2,4)
console.log(ae)
// Some extra function of array,I will learn it later.Like   filter,find,indexof,lastindexof,map,reverse
// sort
at=foods.indexOf("Pizza")
console.log(at)
aaf=foods.filter()
console.log(aaf)
var str="Hello World";
console.log(str.length)
//  INdexing
var j=str[0]
var b=str[1]
var c=str[2]
var d=str[3]
var e=str[4]
console.log(j)
console.log(b)
console.log(c)
console.log(d)
console.log(e)
// Slicing
var q=str.slice(0,2)
console.log(q)
var w=str.slice(0,1)
var e=str.slice(3,6)
var r=str.slice(5,8)
console.log(w)
console.log(e)
console.log(r)
// Escape Character
var d="Hello\nworld"
// to chande line
var e="Hello\tworld"
// to Horizonta space
console.log(d)
console.log(e)
// String Functins
var food="SANDWHICH"
var updatfood=food.toLowerCase()
console.log(food)
console.log(updatfood)
var updatededfood=updatfood.toUpperCase()
console.log(updatededfood)
var food="Pizza"
var input="Pizza"
if (food.toUpperCase===input.toUpperCase){
   console.log("Match")
}else{
   console.log("not match")
}
var a="To be, or|not,to be";
// Indexof
var b=a.indexOf("be")
console.log(b)
var c=a.indexOf("e")
console.log(c)
var d=a.indexOf("n")
console.log(d)
var e=a.indexOf("be",10)
console.log(e)
var f=a.indexOf("to")
console.log(f)
var g=a.indexOf("To")
console.log(g)
var h=a.indexOf("o",2)
console.log(h)
var i=a.indexOf("o",7)
console.log(i)
// charat
var b=a.charAt(0)
console.log(b)
var c=a.charAt(3)
console.log(c)
var d=a.charAt(7)
console.log(d)
var f=a.charAt(4)
console.log(f)
// replace
var b=a.replace("be","hello")
console.log(b)
var c=a.replace("to","yes")
console.log(c)
var d=a.replace("to","up")
console.log(d)
var b=a.replace(/be/g,"hi")//To replace all the same character in string
console.log(b)
var c=a.replace(/o/g,"Yet")
console.log(c)
var d=a.replace(/e/g,"P")
console.log(d)
var b=a.replace(/to/i,"er")//To replace the initial to. i stands for initial
console.log(b)
var c=a.replace(/be/i,"gr")
console.log(c)
var d=a.replace(/o/i,"up")
console.log(d)
var b=a.replace(/to/gi,"he")
console.log(b)
var c=a.replace(/be/gi,"hee")
console.log(c)
// split
var b=a.split(" ")//To split string with space
console.log(b) 
var c=a.split(",")
console.log(c)
var d=a.split("|")
console.log(d)
//  Math
var a=Math.round(4.7)
console.log(a)
var b=Math.round(4.1)
console.log(b)
var c=Math.round(4.5)
console.log(c)
var d=Math.round(-4.1)
console.log(d)
var f=Math.round(-4.7)
console.log(f)
var e=Math.round(-4.5)
console.log(e)
var g=Math.round(5)
// Math.ceil().It is on upper side
var a=Math.ceil(4.7)
console.log(a)
var b=Math.ceil(4.1)
console.log(b)
var c=Math.ceil(-4.7)
console.log(c)
var d=Math.ceil(-4.1)
console.log(d)
// Math.floor().It is on lower side
var a=Math.floor(4.7)
console.log(a)
var b=Math.floor(4.1)
console.log(b)
var c=Math.floor(-4.1)
console.log(c)
var d=Math.floor(-4.7)
console.log(d)
// Math.random
var num1=Math.random()
var num2=(num1*6)+1
var dice=Math.floor(num2)
console.log(num1)
console.log(num2)
console.log(dice)
var a=Math.random()
console.log("A="+a)
var Num1=a*6;
console.log("Num1="+Num1)
var Num2=Num1+1;
console.log("Num2="+Num2)
var Num3=Math.floor(Num2)
console.log("Num3="+Num3)
// Controlling the length of decimals
var average=(15+23+39)/3
var ave=average.toFixed(3)
console.log(average)
console.log(ave)
var w=100/3
var q=w.toFixed(4)
console.log(w)
console.log(q)
// There are few more functions to learn
/*Math.pow(), Math.sqrt(), Math.abs(), Math.sin(), Math.cos(),
Math.min(),Math.max(),Math.exp(),Math.log()*/
//  Date
// There are 4 ways to creat a new date object
// var date1=new Date()//To write recent date
// console.log(date1)
// var date2=new Date(year,month,day,hours,minutes,seconds,milliseconds)
// console.log(date2)
// var date3=new Date(milliseconds)
// console.log(date3)
// var date4=new Date(date String)
// console.log(date4)
var date1=new Date()
console.log(date1)
var date2=new Date(1991,12,13,14,34,56,300)
console.log(date2)
var date3=new Date(34523464561353)
console.log(date3)
var date4=new Date("January 12 2019 10:15:45")
console.log(date4)
var a=new Date("February 12 2020 12:34:45")
console.log(a)
var b=new Date("March 29 2021 14:56:13")
console.log(b)
var c=new Date("April 3 1994 14:45:56")
console.log(c)
var d = new Date("May 28 2024 11:56:34")
console.log(d)
var f=new Date("June 15 2020 23:34:56")
console.log(f)
var g=new Date("July 15 2020 23:34:56")
console.log(g)
var h=new Date("August 15 2020 23:34:56")
console.log(h)
var i=new Date("September 15 2020 23:34:56")
console.log(i)
var j=new Date("October 15 2020 23:34:56")
console.log(j)
var k=new Date("November 15 2020 23:34:56")
console.log(k)
var l=new Date("December 15 2020 23:34:56")
console.log(l)
var m=new Date("1932 11 24")
console.log(m)
var n=new Date("2015/09/11")
console.log(n)
var o=new Date("2019/07//13 10:15:35")
console.log(o)
// unix time
var dte=new Date()
a=dte.getTime()
console.log(a)
// Epoch time
ad=new Date(0)
console.log(ad)
// Retraving the date components
var date =new Date("June 14 2022 10:30:25")
a=date.getFullYear()
b=date.getMonth()
c=date.getDay()
d=date.getHours()
f=date.getMinutes()
g=date.getSeconds()
h=date.getMilliseconds()
i=date.getTime()
console.log(a)
console.log(b)
console.log(c)
console.log(d)
console.log(f)
console.log(g)
console.log(h)
console.log(i)
// Modifyig the Date
var date=new Date("June 14 2019 10:45:25");
console.log(date)
date.setFullYear(2017)
console.log(date)
date.setMonth(02)
console.log(date)
date.setHours(14)
console.log(date)
// Converting Day of week to Text
var dayslist=["Sun","Mon","Tue","Wed","Tue","Fri","Sat"];
var date =new Date("June 14 2019 10:45:25");
var day=date.getDay()
var nameofday=dayslist[day]
console.log(dayslist) 
console.log(date)
console.log(day)
console.log(nameofday)
// calculate Time difference
var d1=new Date ("June 14 2019 10:45:23")
var d2=new Date ("July 11 2020 12:45:23")
var timediff=d2.getTime()-d1.getTime()
console.log(timediff+"Millisec")
var timeinday=24*60*60*1000
console.log("Time in day="+" "+timeinday+"Milliseconds")
var daysdiff=timediff/timeinday
console.log(daysdiff)
//  Recursive Function
// A recursive function is a function that calls itself.
function factorial(n){
  if (n<=1){//Recursive function will stop when this condition match.
      return 1;
  }else{return n*factorial(n-1);//calling itself
  }
}
a=factorial(0.6666);
console.log(a)