# for i in range(20,10,-3):
#     print(i,i,end=" ")
#assgn4
lst=[10,7,4,9,5,18,2,1,8,11,12,6,3,1,11,24]
sum=0
for i in lst:
    sum+=i
avg=sum/len(lst) 
lst[0]=avg
lst[len(lst)//2-1]=avg
lst[len(lst)//2]=avg
lst[-1]=avg
print(lst)
