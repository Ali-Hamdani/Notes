// First Exercise
pragma solidity  ^0.5.0;
contract First{
    function showMessage()public view returns(string memory){
        return "Hello World";
    }
}


// Second Exercise
 pragma solidity ^0.5.0;
 contract Second{
     uint8 internal age1=18;
     uint8 private age2=22;
     uint8 public age3=44;
     uint8 internal constant age4=18;
     uint8 private constant age5=22;
     uint8 public constant age6=44;
     function getage() public view returns(uint8,uint8,uint8,uint8,uint8,uint8){
         return(age1,age2,age3,age4,age5,age6);
     }
     function updateage() public returns(uint8,uint8,uint8,uint8,uint8,uint8){
         age1+=1;
         age2+=1;
         age3+=1;
         return (age1,age2,age3,age4,age5,age6);
     }
 }
 //  variables defined in contract outside the function are called state variable or 
    // storage variables
    //  Qualifiers internal ,private and public.By default every variable is internal
    // variable.internal variable is accessable in contract and also in its child 
    // contract.It is also accessable through function.
    //  private is only accessable in contract.It can be accessable through function.
    //  public variables are publicly accessable inside and outside the contract.
    //  constant keyword will make your variable immutable


//Third Exercise
 pragma solidity ^0.5.0;
 contract Third{
     uint age=44;
     function getage1() public returns(uint){
         return age;
     }
     function getage2() external returns(uint){
         return age;
     }
     function getage3() internal returns(uint){
         return age;
     }
     function getage4() private returns(uint){
         return age;
     }
 }


//   Forth Exercise
  pragma solidity ^0.5.0;
 contract Forth{
     uint8 age=33;
     int8  temperature=-5;
     uint height=60;
     int interestrate=-1;
     string name="ALi";
     bool haveBAdegree=false;
     uint256 counter;
     function Datatypes() public returns(uint8,int8,uint,int,string memory,bool,uint256){
         counter=55;
         return (age,temperature,height,interestrate,name,haveBAdegree,counter);
     }
     
 }


// Fifth Exercise
 pragma solidity ^0.5.0;
contract Fifth{
    int age=45;
    function getage()public view returns(int){
        return age;
    }
    function getage1()public pure returns(int){
        return 5;
    }
    function getage2()public payable{
        // No logic needed
    }
    function receivepayment()public payable{
        // msg.value contains ether from sender
        // We can store value in state variable
        // mybalance+=msg.value;
    }
}


// Sixth Exercise
pragma solidity ^0.5.0;
contract Sixth{
    uint age=56;
    function dosomework()public view{
        
    }
// View is a functional behaviourl qualifiers.It can excess 
// state variable but can not change it. 
    function getage()public view returns(uint){
        uint a=age*2;
        dosomework();
        return age;
    }
    function dosomething()public pure{
        
    }
// View is a functional behaviourl qualifiers.It can not excess 
// state variable and also can not change it. 
    function getok()public pure returns(int){
        dosomething();
        int b=2;
        return b;
    }
    function domework()public pure{
        
    }
// View is a functional behaviourl qualifiers.It can excess 
// state variable but can not change it. 
    function getage1()public view returns(uint){
        uint c=age*2;
        domework();
        return age;
    }
}


// Seventh Exercise
 pragma solidity ^0.5.0;
 contract Seventh{
     function receivepayment() public payable{
         
     }
     function getbalance() public view returns(uint256){
         return address(this).balance;
     }
 }
