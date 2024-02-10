# def stats():
#     fname=input("Enter filename: ")
#     infile=open(fname,'r')
#     f=infile.readlines()    
#     wrd_lst=[]
#     char=0
#     for i in f:
#         i=i[:len(i)-1]
#         wrd_lst+=i.split()
#     for j in wrd_lst:
#           char+=len(j)
#     print('The no. of lines in the file are',len(f))
#     print('The no. of words in the file are',len(wrd_lst))
#     print('The no. of characters in the file are',char)

# stats()
# def distribution():
#     lst=[6,2,3,2,2,4,1,2]
#     fname=input('Enter filename: ')
#     file=open(fname,"r")
#     f=file.read()
#     std_data=f.split()
#     for i in range(len(lst)):
#         print(lst[i],"students got",std_data[i])

# distribution()
def duplicate():
    fname=input('Enter filename: ')
    file=open(fname,'r')
    f=file.read()
    wrd=f.split()
    for i in wrd:
        wrd.remove(i)
        for j in range(len(wrd)):
         if i==wrd[j]:
           return True
    else:
       return False
print(duplicate())
# def abc():
#     fname=input('Enter filename: ')
#     file=open(fname,"r")
#     file1=open('abc.txt','a+')
#     f=file.read()
#     lst=f.split()
#     for i in lst:
#         if len(i)==4:
#            f=f.replace(i,'xxxx')  
#     file1.write(f)
# abc()
