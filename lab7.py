lst=[(2,3),(4,7),(8,11),(3,6)]
for i in range(len(lst)):
    a=min(lst[i])
    b=max(lst[i])
    print('For Tuple',i+1,'\nMax=',b,'\nMin=',a)
# from math import sqrt     
# tuple=((0,0),(10,10),(6,6),(7,8))  
# rds=10     
# for i in tuple:
#     dist=sqrt(i[0]**2+i[1]**2)
#     if dist<=rds:           
#         print(True)
#     else:
#         print(False)    

# dict=("anachronistically","counter","counterintuitive","counterrevolution",
#       "ﬂoccinaucinihilipiliﬁcation","misinterpretation","misrep-resentation","resolution")
# print(len(dict[0])==len(dict[2])+1)
# print(dict.index("misinterpretation")<dict.index("misrep-resentation"))
# print("e" not in dict[4])
# print(len(dict[3])==len(dict[1])+len(dict[-1]))
# tpl=()
# lst=list(tpl)
# for i in range(4):
#  prvncs=input("Enter the name of the province: ")
#  lst.append(prvncs)
# print(tuple(lst))  
# monthsL=['Jan','Feb','Mar','May']
# monthsT=('Jan','Feb','Mar','May')
# temp=list(monthsT)
# monthsL.insert(3,'Apr')
# temp.insert(3,'Apr')
# print(monthsL)
# print(tuple(temp))
# monthsL.append('Jun')
# temp.append('Jun')
# print(monthsL)
# print(tuple(temp))
# monthsL.pop(1)
# temp.pop(1)   
# print(monthsL)
# print(tuple(temp))
# print(monthsL[::-1])
# print(tuple(temp[::-1]))
# del monthsL
# del monthsT
