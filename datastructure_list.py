"""-----------------------------DATA STRUCTURE-----------------------------"""
#in a single variable stores multiple value
""" we can to  CRUD operator in data structure
C = create
R = read/retrive
U = update
D = delete """

# s="Malavika Rajesh"
# print(s[3])
# print(s[-3])

# s="python"
# print(s[2:5])

"""............case covertion methods...............
s="Python"
print(s.upper())
print('PYTHON'.lower())
print('my name is malu'.title())  #used to capitalize first letter in all word
print("this is a sentence".capitalize()) #used to capitalize only first letter in first word 
print("THIS is A swap CASE example".swapcase()) #used to change the capital to small and small to  capital"""

"....................searching and finding......................"
# sentence="This is a test sentence"
# print(sentence.find('t'))
# print(sentence.rfind('t'))
# print(sentence.index('s'))
# print(sentence.rindex('s'))
# print(sentence.count('t'))

"""Data Structure"""

# empty_list=[]
# print(type(empty_list))

# students=['malavika','Harshad','Adhi']
# print(students)
# print(len(students))

# for s in students:
#     print(s)
    
# print(students[1])

# sample=[2,3,4]
# sample+=[200,300,400]
# sample+='Quest' 
# sample+=234 #we will get error bcz it was iterable. If we use square braces we get output

# sample*=3     #repeat the value
# print(sample)

# # "Membership operator"
# sample=[2,3,4]
# print(3 in sample)

# sample2=[2,3,4]
# print(sample==sample2)
# print(sample is sample2)
# "sample and sample2 is refer to equal but sample and sample2 is not equal because their memory location is different in list type"

# numbers=[200,300,400,500]
# print(dir(numbers))
# numbers.append(700)
# numbers.insert(2,800)
# numbers.pop()
# numbers.pop(2)
# numbers.remove(200)
# numbers.clear()
# print(numbers)
# copy_list=numbers.copy()
# print(copy_list)

# numbers=[2,3,7,8,4,5,6,]
# print(numbers.count(4))
# print(numbers.index(4))
# numbers.reverse() #it  will reverse the  list
# numbers.sort(reverse=True) 
"""sort uses  for printing in ascending order(low to high) 
if we want to get in decending(high to low) use numbers.sort(reverse = true)"""

# print(numbers)
# num=[90,40,70]
# num.extend(numbers)  #use  for extend the value by adding new  value
# print(num)

# num=[30,40,50]
# num.extend([20,60,70,10,[1,2,3]])
# num.sort() when  we sorting  we cannot use nested if
# print(num)

"""-------------------------python inbuilt methods------------------------"""

# numbers=[200,300,400,500,600]
# total=sum(numbers)
# print(total)
# print(min(numbers)) 
# print(max(numbers))

# "NESTED LISTS"
# numbers=[20,30,40,[50,60,70,80]]
# print(numbers[3][2])

numbers=[20,30,40,[50,60,70,80,[90,100,110]]]
# print(numbers[3][4])

# "LIST COMPREHENSION"
# num=[i for i in range(1,11)]
# print(num) 
# square=[i**2 for i in numbers]
# print(square)

# list1=['malavika','Harshad','Adhi']
# list2=[i.upper() for i in list1]
# print(list2)

# list=[i for i in range(20)if i%2==0]
# print(list)
