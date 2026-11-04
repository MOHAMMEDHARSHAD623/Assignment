class Students:
    std = '10th'
    sec = 'c'

    def __init__(self,name,roll_num):
        self.name = name
        self.roll_num = roll_num
        self.total_mark = 0
        self.pass_fail_flag =  0

    def get_details(self):
        print('\n----STUDENTS DETAIL----')
        print(f'Student name:',self.name)
        print(f'Std/sec: "{Students.std}"/"{self.sec}"')
        print(f'Student roll number:',self.roll_num)
        

    def score(self):
        self.english = int(input("English: "))
        self.mathematics = int(input("Mathematics: "))
        self.science = int(input("Science: "))
        self.c_s = int(input("Computer: "))
        self.social = int(input("Social: "))

        if self.english > 31 and self.mathematics > 31 and self.science > 31  and self.c_s > 31 and self.social > 31:
            self.total_mark = sum([self.english,self.mathematics,self.science,self.c_s,self.social])
            self.pass_fail_flag = 1

        else:
            self.pass_fail_flag = 0
        
        print(f'Total mark:',self.total_mark )

        

    def perctng(self):
        if self.pass_fail_flag:
            self.percentage = self.total_mark / 500*100
            if self.percentage >= 90 and self.percentage <= 100 :
                print('Grade A+')
            elif self.percentage >= 80 :
                print('Grade A')
            elif self.percentage >= 70 :
                print('Grade B+')
            elif self.percentage >=60 :
                print('Grade B')
            elif self.percentage >=50 :
                print('Grade C')
            else:
                print('Grade D')

            print(f'percentage:',self.percentage)
        else:
            print('your are failed in 1 or more subject.\ndue to this reason we can\'t process your grade,total mark & percentage. And')

    def elgiblity(self):
        if self.pass_fail_flag:
            if self.total_mark > 250 and self.total_mark <=500 :
                print("you are elgible to your higher  studies")
            elif self.total_mark < 0 or self.total_mark > 500:
                print("invalid mark...!!!")
        else:
            print("You are not  elgible to your higher studies")

    


harshad = Students('Mohammed Harshad','2328c0120' )
malavika = Students('Malavika Rajesh','2328c0119')
adhithyan = Students('Adhithyan','2328c0118')
sreeraj = Students('Sreeraj Mathiyath','2328c0117')
anagha = Students('Anagha','2328c0116')
ashi = Students('Ashikka A.V','2320c0115')

harshad.get_details()
harshad.score()
harshad.perctng()
harshad.elgiblity()

malavika.get_details()
malavika.score()
malavika.perctng()
malavika.elgiblity()

adhithyan.get_details()
adhithyan.score()
adhithyan.perctng()
adhithyan.elgiblity()

sreeraj.get_details()
sreeraj.score()
sreeraj.perctng()
sreeraj.elgiblity()

anagha.get_details()
anagha.score()
anagha.perctng()
anagha.elgiblity()

ashi.get_details()
ashi.score()
ashi.perctng()
ashi.elgiblity()

s = {'harshad':harshad.total_mark ,
    'malavika':malavika.total_mark,
    'adhithyan':adhithyan.total_mark,
    'sreeraj':sreeraj.total_mark,
    'anagha':anagha.total_mark,
    'ashikka':ashi.total_mark}

print('\n----CLASS SUMMARY----')
print(f'Students  evaluated: ',len(s))


finding_topper = {
    name: mark for name, mark in s.items()
    if 0 <= mark <= 500 }

if finding_topper:
    topper =  max(finding_topper, key=finding_topper.get)
    print(f'Class topper:',topper)
    print(f'topper Mark:',finding_topper[topper])
else:
    print('Invalid marks available')

passed = 0
failed = 0
invalid = 0


for mark in s.values():

    if  mark < 0 or mark > 500:
        invalid += 1
    elif mark > 250 :
        passed += 1
    else:
        failed += 1

print('\n----pass & fail list----')
print(f'total number of pass:',passed)
print(f'total number of fail:',failed)
print(f'total number of invalid:',invalid)
