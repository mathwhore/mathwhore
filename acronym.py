# def acro(a):
#   x=[]
#   x+=a.split(" ")
#   acronym=""
#   for i in x:
#    acronym+=i[0].upper()
#   return acronym   
      
# word=input("Enter the word:")
# print("The acronym of",word,"is",acro(word))
# def count_substring(string, sub_string):
#         count=0
#         for i in range(len(string)-len(sub_string)+1):
#          if string[i:len(sub_string)+i]==sub_string:
#           count+=1    
#         return count
# string=input()  
# ss=input()    
# print(count_substring(string,ss))
s = input()
alph_lower="abcdefghijklmnopqrstuvwxyz"
alph_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
print(any(i in alph_upper+alph_lower+num for i in s))
print(any(i in alph_upper+alph_lower for i in s))
print(any(i in num for i in s))
print(any(i in alph_lower for i in s))
print(any(i in alph_upper for i in s))
             