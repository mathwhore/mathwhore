def mult3(a):  
 for i in a:
  if int(i)%3==0:
     print(i, end=" ")
  
lst=list(input("Enter the no.s for the list:"))
print(lst)
mult3(lst)


