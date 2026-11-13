"""File - Named collection of related data
stored as a single  unit on a storage medium

OS treats it  as one object with:
1. a filename
2. extension - which denotes the stored data type like(jpg,.py,mkv,mp4,mp3,png,etc..)
3.metadata - data about data
4. contents"""

"""RAW STRING - r (in frnt like f string)
when we trying to open  file via path or like containg slash use r 
open(r'') -- syntax  
if that is image or wanted in binary type - use binary mode 'rb'-- read binary
open(r'',rb)
"""

"""Read - r
write - w
read + write - r+
write + read - w+
append - a
append + write - a+
read binary  = rb+ / r+b
write binary = wb+ / w+b
for checking cursor where it is use - tell()
for changing cursor position by using - seek(index  value)
to convert string to binary type use - ****.encode()
for remove('shorting the data') from unwanted data  from file - truncate - w , r+, a --

"""
""" cursur was in 0th position before read 
after read it will be in last position
when we write before  read it will write from 0th  position 
after read it will be in last position
"""

#example code------------------------------------------------------------------

# file = open('test_2.py')
# data  = file.read()

# print(data)  #change directory cd 

# file.close()       #these 2 eg will be access in same drive

#OR------------------------------------

# with open('test_2.py') as d: 
#     print(d.read()) 
                #when we use this type of code for read there is no need to close

#---------------------------------------------------------------------------------

# with open('test_2.py','w+') as t:
#     t.write('malavika loose.....')
#     print(t.tell())
#     t.seek(0)
#     print(t.read())

#----------------------------------------------------------------------------------

"""appent - a
appent + write - a+
seek
tell
read
write
close
read line
read lines
readable
seekable
writable
write lines"""

# with open('test.py','a+') as f:
#     f.write("\n#this is for checking\n#this.....")
#     f.seek(0)
#     print(f.read())

# with open('test.py','a') as f:
#     f.write("#this is also for checking\n")

# with open ('test.py','r') as f:
#     print(f.read())

# with open('employee_records.csv','r') as file:
#     file.seek(0)
#     print(file.tell())
#     print(file.readline())
#     print(file.readlines())

# with open('employee_records.csv','a') as f:
#     f.write('\nadhii....')
#     # f.seek(0)
#     # print(f.read())

# with open('employee_records.csv','r') as file:
#     print(file.read())

# with open('employee_records.csv','a') as f:
#     f.write('\nmaluuuuu')

# with open('employee_records.csv','r') as file:
    # print(file.read())
   
    # print(file.readline())
    # print(file.readlines()

# with open("employee_records.csv","ab") as f:
#     print(f.write("\nmaalu".encode()))
#     # f.seek(0)
#     print(f.seekable())

# import os
# print(os.path.exists("test_2.py"))

# import os
# os.rename('test_3.py','test.py')

# import os
# os.remove('arshad.txt')

# import os
# os.mkdir('arshad.txt')

# import os
# os.makedirs('arshad/adhi/malu')

# import os
# print(os.listdir('.'))

# import os
# print(f'\n------',os.getcwd())

# import os
# os.chdir(r"c:/Users/arshu/OneDrive/Desktop/Quest/py.ds_Module")

# print(os.getcwd())

# import os
# print(os.path.isfile('employee_records.csv'))

# import os
# print( os.path.isdir('arshhh'))
# print( os.path.isdir('test.py'))

# import os
# os.makedirs('arshad/adhi/malu')

# import shutil
# shutil.rmtree('arshhh')


""" os.path.exist - used for checking the file is exist or not.if yes,it will return  true using os.path.exist()
os.rename - used for rename the  file name using os.rename()
os.remove - used for remove or delete  the file using os.remove()
os.mkdir -  used for create a new folder using os.mkdir() existing couldn't support
os.makedirs - used for create inner file or folders using os.makedirs()
os.rmdir - used for remove folders using os.rmdir() if the  file is not empty is not works
shutil.rmtree - used for  remove multiple folders using shutil.rmtree()
os.listdir - used for listing the dir by using print(os.listdir('.'))
os.getcwd() - used for checking which directory user is in by using print(os.getcwd()) 
os.chdir() -  used for changing directory using os.chdir('path) but it only works  for that script
os.path.isfile() - used for checking the file is existing in this path if yes it return true- use print(os.path.isfile())
os.path.isdir() -used for checking the folder is existing in this path if yes it return true - use  print(os.path.isdir())
"""

# import os
# print(os.path.exists('python'))

# import os
# os.rename('test_3.py','test_2.py')

# import os
# os.remove('employee_records.csv')\

# import os
# os.mkdir('arshad')

# import os
# os.makedirs(r'arshad\adhi\malu')

# import os
# os.rmdir('arshhh')

# import os
# print(os.listdir())

# import os
# os.chdir(r'C:\Users\arshu\OneDrive\Desktop\Quest')

# print(os.getcwd())

# import os
# print(os.path.isfile('arshhh'))

# import os 
# print(os.path.isdir('file_handling.py'))
# print(os.path.isdir('arshhh'))

# import os
# os.chdir(r'C:\Users\arshu\OneDrive\Desktop\Quest')

# print(os.getcwd())

# os.mkdir('adhi')
