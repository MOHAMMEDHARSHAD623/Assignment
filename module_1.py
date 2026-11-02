# print("hello warrior ")

# (#)this is used for command in one line
""" this is used for multi line command this is also called  as documnet string"""

# name = "arshu"
# num = 1234

# print(type(name)) #it used to check which type is this
# print(type(num))

# print(id(name))  #it used to check in which memory location the value stored
# print(id(num))

# print(len(name)) #it is used to check the length of the value


#----------------------------------------------------------------------
# name = "arshad"
# roll_num = 23280120
# course = "AI & DS"

# print("my name is" ,name,"my roll number is",roll_num,"\n and I took",course,"course")
"""the last printing method was sometimes make hard bcz of many commas and etc...
so we going to use formatted string """
# print(f"My name is {name}. My roll number is {roll_num} \n I taken {course} course")

"""------------------ARITHMATIC OPERATOR--------------------------"""
#--------------------------------------SUM-----------------------------------------
# a = 'har'
# b = 'shad'         #adding two string is know as string concatination

# print(a+b)

# c = 55         #we can't sum int and string but int to int &  strng to strg  can
# d = 5
# print(c+d)          

#---------------------------------------SUB----------------------------------------

# a = 33
# b = 22   #we can't sub the int and string only int to int can sub

# print(a-b)

#---------------------------------------MULTI-------------------------------------

# a = 15
# b = 2   #in this we  can multiple the int to int and string to in but strg to  strg can't

# print(a*b)

# c = 'ars'
# d = 3    #when we  multiple strg to int we get repeatation of string till the int number of times
# print(c*d)

#-------------------------------------DIV--------------------------------------------

# a = 300
# b = 2

# print(a/b)

#------------------------------------MOD-----------------------------------------------
# a = 100
# b = 2  #this method gives reminder as output it was mostly used in to check even or odd

# print(a%b)

#------------------------------------FLOOR DIV-----------------------------------------
# a = 100   #it gives coseint  as output
# b = 2

# print(a//b)

#-------------------------------------EXPO--------------------------------------------
# a = 100
# b = 2 #it gives output  but squaring or cubing value

# print(a**b)

#--------------------------------------------------------------------------------------
"""-----------------COMPARISON  OPERATOR------------------------------------- 
they are......  == equal to equal to
!= not equal to
> greater than
< less than
>= greater  than equal to    
<=  less than equal to """
#compartion operator will return only boolean value

"""-----------------------ASSIGNMENT OPERATOR-------------------
=  equal to
+= plus equal to
-= minus  equal to
*= multiple equal to
/= divide  equal to
%= modules equal to
//= floor equal to
**= expo equal to  """
#it will  operats and assign to a value given

"""-------------LOGICAL OPERATOR-------------------------
and  #in this everything should be true
or #in this any one  should be true 
not # in this, if it was true  it will return false , if it was false it will  return true """
#it will return the boolean values

"""------------MEMBERSHIP OPERATOR--------------------------------------------
in #its check  the value is in that variable if yes it will return  true
not in #its as usual like not """
#it will return boolean values

"""---------------------IDENTITY OPERATOR---------------------------------------
is #to check the two variable are in same memory location
is not  #it is opposite to is """
 
#-----------------ASCII-------------------------------------------
"""  ascii means AMERICAN STANDARD CODE FOR INFORMATION INTERCHANGE
to find the ascii value of the character  <syntax> : print(ord("A"))
from ascii value to  get  the character is <syntax>: print(chr(67))"""

#----------------------------------------------------------------------------------
""" spacing in front is called  as  intentation or white space """

#---------------------------------------------------------------------------------
#to check odd or even number

# num = int(input("Enter the  number: "))

# if num % 2 == 0:
#     print("it was a even number...")
# else:
#     print("it was odd......")

#it is syntax for finding value by index value
# s = "quest"
# print(s[2])

""".startswith() 
.endswith()
"""

# ars = ('arshad','malavika','aadhi','sreeraj')

# # name = 'arshad'
# # print(name.startswith('a')) #for this we only get it was true or false

# for i in ars:
#     if i.startswith('a'):
#         print(i)  #this start and end will done in only loop functions

#------------------------------------------------------------------------------
# ars = ('apple','aadhiyan','malavika','sreeraj','harshad','ashi')

# for i in ars:
#     if i.endswith('i'):
#         print(i)