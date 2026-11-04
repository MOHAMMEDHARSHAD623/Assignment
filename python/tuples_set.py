"""TUPLE IN PYTHON----------------------------------------------------------"""

# t = (5,"arsha",93449,[200,6,3])

# print(type(t))
# print(t[2])
# print(t[3][2])
# print(t[::-1])

# t = (10,20,30) #only tuple to tuple can concatenat
# t = t + (40,)  #one more method for this t += 40
# print(t)

"""converting the tuple to list to  add some charachters or 
values we cannot upadate  or add any values in tuple bcz it is immutable.
 at last  convert back to tuple"""

# t = ('arshad','malavika', 'adhi')
# add = list(t)
# add.append('sreeraj')
# t = tuple(add)

# print(t)
# print(dir(t))

"""----------------------------------------------------------------------------------"""
#t = ('a','a','r','a','s','h','i','r','a','b','r','h','y','a')
# print(t.count('a'))  #as usual it was used for count  a value how  many times oit was repeated 
# print(t.index('a', 2, 9)) #but in this... its order is (item , start , stop)

"""-----------------SET IN PYTHON------------------"""
# empty = {}
# print(type(empty))

# s ={ 1,2,3,1,2,3,1,2,3}
# print(s)   #it removes dublicate itself

# s ={ 1,2,3,"sreeraj",(1,2,3),[1,2,3]}
# print(s)  #we can't add list it  will returns error bcz unhashable type of set and list

# s ={0,1,True,False,""}
# print(s)

"""----IN-BUILD METHODS OF SET
.add() used to add
.update() used to update
.remove()
.discard() 
.pop() used to remove  random item
.clear()  used to remove all items"""

# y = {'arshad','malavika','adhi'}
# y.add('sreeraj') #we can't add multiple value
# print(y)

# a = [10,30,50,60]
# y.update(a)
# print(y)

# y.update("arsha")
# print(y) #iterable

# y.remove('malavika') 
# print(y)

# y.discard("arsh") #if we give unvalue for discard it  will not get error
# print(y)

# y.pop()
# print(y)

# y.clear()
# print(y)

"""-------SET OPERATION
.union() / |  to make a group avoids duplicates it was unordered
.intersection() / & it returns common values
.difference() / - it returns which value is  not in
.symmentric_difference() / ^"""

# r = {1,2,3,5,6,7}
# r1 ={2,3,4,6,9,0,3}

# r2 = r.union(r1)
# print(r2)
#---------------------------------------------
# r = {1,2,3,4,5}
# r2 = {2,4,6,}

# r1 = r&r2
# print(r1)
#-------------------------------------------
# r = {1,2,3,4}
# r1 = {4,5,6,7}

# r2 = r - r1
# r3 = r1 - r
# print(r2)
# print(r3)
#-------------------------------------------
# r = {1,2,3,4}
# r1 = {4,5,6,7}

# r2 = r^r1
# print(r2)
#---------------------------------------------

"""--------------------returns--------------------"""
#return function

# def add(x,y):
#     return x+y #return value used for call and used  to store in another value

# result = add(20,30) #in a block of code  we only use return function for one time  
# print(result)

"""-------------------------------------------------------------------------"""
# value = int(input(" enter the number: "))
# def check(value):
#     if value %2==0:
#        return  "even"
#     else: 
#         return "odd" #this return value will execute only when  we add  to another value

# result = check(value)
# print(result)

Python_students ={'Maya','Ravi','Anu','John'}
sql_students = {'Ravi','Maya','Sara'}
marks = {'Anu': 95,'Ravi': 80,'Maya':88}
average = sum(marks.values())/len(marks)
least = max(marks.values())

print(f"Students in either course: ",Python_students.union(sql_students))
print(f'Students in both course: ',sql_students.intersection(Python_students))
print(f'Marks',marks)
print(f'Average = ',average)
print(least)