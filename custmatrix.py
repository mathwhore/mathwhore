lst=[]
main=[]
prdct=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(2):
     if i==1:
        print('Now for second matrix')
     r=int(input('Enter the no. of rows you want: '))
     c=int(input('Enter the no. of columns you want: '))
     for i in range(r):
      lst=[]
      print('You are entering data for',i,'th row')
      for j in range(c):
          no=int(input('Enter the no: '))
          lst.append(no)
      main.append(lst)         
mtrx1=main[:c]
mtrx2=main[c:]
for j in range(len(mtrx1)):
    for i in range(len(mtrx2[0])):
      for k in range(len(mtrx2)):
        prdct[j][i]+=mtrx1[j][k]*mtrx2[k][i]

print('The product of the matrices is')     
for i in prdct:
   print(i)

# lst=[[23,4],
#      [5,6]]
# lst1=[[2,3],
#      [42,2]]
# prdct=[[0,0],
#       [0,0]]
# for j in range(len(lst)-1):
#     for i in range(len(lst)-1):
#      prdct[j][i]=(lst[j][i]*lst1[j][i])+(lst[j][i+1]*lst1[j+1][i])
# for i in prdct:
#    print(i) 

#lab5
# i=1
# while i<=8:
#      if i<=4:
#       print(14*"*")
#      else:
#       print(16*" ",14*"*")   
#      i+=1    
# i=7
# while i>=1:
#     print(i*"*")
#     i-=1/

