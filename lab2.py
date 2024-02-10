# n=int(input("Enter the no. of integers you want the sum of:"))
# print("The sum of the first",n,"integers is",(n*(n+1))/2) 
# age3=int(input("Enter Fatima's age"))   
# ht1=int(input("Enter Sara's height(in inches)"))
# ht2=int(input("Enter Mark's height(in inches)"))
# abs_diff=abs(ht1-ht2)
# print("The absolute difference between Sara and Mark's height is",abs_diff,"inches")
# import math
# n=73
# x=403
# print("The no. of times",x,"goes into",n,"is",math.floor(x/n))
# p1=float(input("Enter the price($):"))
# p2=float(input("Enter the price($):"))
# p3=float(input("Enter the price($):"))
# print("The lowest price among",p1,",",p2,"and",p3,"is",min(p1,p2,p3))
# name=input("Enter your name:")
# print("Hello"+name)
# prncpl=int(input("Enter the principal amount($):"))
# rate=int(input("Enter the interest rate(%):"))
# time=int(input("Enter the period of time(in years):"))
# intrst=(prncpl*rate*time)//100
# print("The simple interest is",str(intrst)+"$")
# callno=int(input("Enter the no. of calls:"))
# basic_bill=2000
# if callno<=100:
#     print("Your bill for this month is Rs",basic_bill)
# elif callno>100 and callno<=150:
#      diff=callno-100
#      print("Your bill for this month is Rs",basic_bill+(0.6*diff))
# elif callno>150 and callno<=200:
#      diff=callno-150
#      basic_bill+=30
#      print("Your bill for this month is Rs",basic_bill+(0.5*diff))
# elif callno>200:
#      diff=callno-200
#      basic_bill+=55
#      print("Your bill for this month is Rs",basic_bill+(0.4*diff))          
a=input("Enter the no. for the first variable a")
b=input("Enter the no. for the second variable b")
temp=a
a=b
b=temp
print("The no.s are now swapped\n a="+a+"\n b="+b)

