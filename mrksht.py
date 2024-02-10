name=input("Enter your name:")
f_name=input("Enter your father's name:")
r_no=input("Enter your roll no:")
sub_marks=[]
total_marks=0
for i in range(5):
 s_name=input("Enter subject name:")
 s_marks=int(input("Enter subject marks(out of 100):"))
 lst=[s_name,s_marks]
 sub_marks.append(lst)
print('Marks Statement:') 
print("Name:",name,", Father's name:",f_name,", Roll no:",r_no) 
for i in sub_marks:
 print(i[0],'=',i[1],'/100')
 total_marks+=i[1]
print('Your total marks are:',total_marks,'out of 500.')
prcntg=(total_marks/500)*100
print('Your marks percentage is',prcntg,'%')
if prcntg<=100 and prcntg>=87:
    print("Your grade is A")
elif prcntg<87 and prcntg>=75:
    print("Your grade is B")
elif prcntg<75 and prcntg>=65:
    print("Your grade is C")
elif prcntg<65:
    print("You have failed your exams")
else:
    print("Please enter the correct marks")
    


  